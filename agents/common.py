# agents/common.py

import os
import subprocess
from pathlib import Path

from dotenv import load_dotenv

from openhands.sdk import LLM, Agent, Conversation, Tool
from openhands.tools.file_editor import FileEditorTool
from openhands.sdk.event import ObservationEvent

import requests

from pathlib import Path
from dotenv import load_dotenv
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s %(name)s %(message)s"
)
project_root = Path(__file__).resolve().parent.parent
env_path = project_root / ".env"

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("openhands").setLevel(logging.DEBUG)
logging.getLogger("openhands_sdk").setLevel(logging.DEBUG)

# ---------------------------------------------------------
# Load .env at import time (fail if missing)
# ---------------------------------------------------------
if not env_path.exists():
    raise FileNotFoundError(
        f".env file not found at expected location:\n  {env_path}\n"
        "Please create the file with: LLM_API_BASE, LLM_API_KEY, and LLM_MODEL"
    )

# Actually load the environment
load_dotenv(env_path)


# -------------------------------------------------
# ENV / CONFIG
# -------------------------------------------------

def load_env() -> Path:
    """Load .env and return the project root directory.

    Raises:
        FileNotFoundError: if .env does not exist at the project root.
    """
    project_root = Path(__file__).resolve().parent.parent
    env_path = project_root / ".env"

    if not env_path.exists():
        raise FileNotFoundError(
            f".env file not found at expected location: {env_path}\n"
            "Please create a .env file containing LLM_API_BASE, LLM_API_KEY, and LLM_MODEL."
        )

    load_dotenv(env_path)
    return project_root


# -------------------------------------------------
# LLM / AGENT FACTORIES
# -------------------------------------------------

def build_llm() -> LLM:
    model = os.getenv("LLM_MODEL")
    base_url = os.getenv("LLM_API_BASE")
    api_key = os.getenv("LLM_API_KEY", "dummy")

    if not model:
        raise RuntimeError("LLM_MODEL missing in environment variables")
    if not base_url:
        raise RuntimeError("LLM_API_BASE missing in environment variables")

    # --- Minimal, quiet connectivity check ---
    try:
        # We just care that *something* is listening there.
        # Status code can be anything; this is only a reachability probe.
        requests.get(base_url, timeout=2)
    except requests.exceptions.RequestException:
        # `from None` prevents the giant chained traceback from requests/urllib3
        raise RuntimeError(
            f"Cannot connect to LLM endpoint at {base_url}. "
            "Is the server running and reachable from inside the container?"
        ) from None

    # --- If reachable, build the LLM instance ---
    return LLM(
        model=model,
        api_key=api_key,
        base_url=base_url
    )

# ---------------------------------------------------------
# Conversation runner (shared by all agents)
# ---------------------------------------------------------
def run_conversation(prompt: str, task: str, root: Path, tools: list):
    llm = build_llm()

    agent = Agent(
        llm=llm,
        tools=tools,
    )

    conversation = Conversation(
        agent=agent,
        workspace=str(root)
    )

    # Load project-wide rules
    project_rules_path = root/"docs"/"project-architecture.md"
    if project_rules_path.exists():
        project_rules = project_rules_path.read_text()
    else:
        project_rules = ""
        print("[WARNING] project-architecture.md not found")

    # Build the full effective prompt
    system_header = (
        "# PROJECT SYSTEM RULES (PREPENDED)\n"
        "The following content defines the global architecture rules for this project.\n"
        "You MUST follow these rules strictly, and they override any defaults.\n\n"
    )

    full_prompt = (
            system_header
            + project_rules
            + "\n\n# AGENT INSTRUCTIONS\n"
            + prompt
            + "\n\n# USER TASK\n"
            + task
    )
    conversation.send_message(full_prompt)
    conversation.run()

    '''
    # Review all events
    for i, event in enumerate(conversation.state.events):
        print(f"#{i}{type(event).__name__}: {event}")
        if isinstance(event, ObservationEvent):
            print(f"Tool: {event.tool_name}")
            print(f"Result: {event.observation}")

    from openhands.sdk.conversation.state import ConversationExecutionStatus, ConversationState

    # Check if waiting for confirmation
    if conversation.state.execution_status == ConversationExecutionStatus.WAITING_FOR_CONFIRMATION:
        # Get pending actions
        pending = ConversationState.get_unmatched_actions(conversation.state.events)
        print(pending)
        # Approve: just call run() again
        conversation.run()

        # Or reject with feedback
        conversation.reject_pending_actions("User rejected - try a different approach")
    '''

# -------------------------------------------------
# PYTEST EXECUTION
# -------------------------------------------------

def run_pytest(path: str = "tests"):
    """
    Run pytest and print results.
    This is used ONLY by developer agents.
    """
    print("\n--- Running pytest ---\n")
    result = subprocess.run(
        ["pytest", path],
        text=True
    )
    print("\n--- Pytest finished ---\n")
    return result.returncode