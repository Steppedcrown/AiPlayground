# AiPlayground

A terminal-based game generator powered by Claude. Describe any game you want to play, and Claude will write and immediately launch it — all within your terminal.

## How it works

You type a description of a game (e.g. "a snake game" or "a text-based dungeon crawler"), and Claude generates complete Python code for it and runs it on the spot. When the game exits, the temporary file is automatically cleaned up.

## Requirements

- Python 3.8+
- `anthropic` Python package

```bash
pip install anthropic
```

- An **Anthropic API key**. You can get one at [console.anthropic.com](https://console.anthropic.com). Set it as an environment variable before running:

```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

## Usage

```bash
python claude_chat.py
```

You'll be prompted to describe the game you want. Enter a description and press Enter — Claude will generate and launch the game immediately.

**Example prompts:**
- `a snake game`
- `a text adventure where I explore a haunted house`
- `a two-player number guessing game`
- `tetris`

Press `Ctrl+C` at the description prompt to exit without generating a game.
