#!/usr/bin/env python3
import sys
import os
import subprocess
import tempfile
import anthropic

SYSTEM = (
    "You are a game developer. When the user describes a game, write complete, "
    "runnable Python code for a terminal-based game and call the create_game tool "
    "with that code. The game must be self-contained and playable entirely in the "
    "terminal. Do not explain the code — just call the tool."
)

TOOLS = [
    {
        "name": "create_game",
        "description": "Write and launch a terminal game with the provided Python code.",
        "input_schema": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string",
                    "description": "Complete, runnable Python code for the terminal game.",
                }
            },
            "required": ["code"],
        },
    }
]


def main():
    client = anthropic.Anthropic()

    try:
        prompt = input("Describe the game you want to play: ").strip()
    except (EOFError, KeyboardInterrupt):
        print()
        sys.exit(0)

    if not prompt:
        sys.exit(0)

    print("\nGenerating your game...\n")

    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=8192,
        system=SYSTEM,
        tools=TOOLS,
        tool_choice={"type": "tool", "name": "create_game"},
        messages=[{"role": "user", "content": prompt}],
    )

    for block in response.content:
        if block.type == "tool_use" and block.name == "create_game":
            code = block.input["code"]
            with tempfile.NamedTemporaryFile(
                mode="w", suffix=".py", delete=False
            ) as f:
                f.write(code)
                tmp_path = f.name
            try:
                print("Starting game...\n")
                subprocess.run([sys.executable, tmp_path])
            finally:
                os.unlink(tmp_path)
            return

    print("No game was generated. Try describing it differently.")


if __name__ == "__main__":
    main()
