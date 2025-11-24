# agents/coder.py

import agents.common
import openhands.tools.terminal
import openhands.tools.file_editor
import openhands.sdk


def run(task: str):
    prompt_path = agents.common.project_root / "agents" / "coder.prompt.md"
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

    agents.common.run_pytest("tests")