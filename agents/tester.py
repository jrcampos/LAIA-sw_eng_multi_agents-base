# agents/tester.py

import agents.common
import openhands.tools.terminal
import openhands.tools.file_editor
import openhands.sdk

def run(task: str):
    prompt_path = agents.common.project_root / "agents" / "tester.prompt.md"
    prompt = prompt_path.read_text()

    tools = [
        openhands.sdk.Tool(name=openhands.tools.terminal.TerminalTool.name),
        openhands.sdk.Tool(name=openhands.tools.file_editor.FileEditorTool.name),
    ]
    agents.common.run_conversation(prompt, task, agents.common.project_root, tools)

    agents.common.run_pytest("tests")