# agents/reviewer.py

import agents.common
import openhands.tools.terminal
import openhands.tools.file_editor
import openhands.sdk
from pathlib import Path


def run(task: str):
    prompt_path = agents.common.project_root / "agents" / "reviewer.prompt.md"
    prompt = prompt_path.read_text()

    tools = [
        openhands.sdk.Tool(name=openhands.tools.terminal.TerminalTool.name),
        openhands.sdk.Tool(name=openhands.tools.file_editor.FileEditorTool.name),
    ]

    agents.common.run_conversation(
        prompt=prompt,
        task=task,
        root=agents.common.project_root,
        tools=tools,
    )

    print("\nReview generated under reviews/ directory.\n")