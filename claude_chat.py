#!/usr/bin/env python3
import sys
import anthropic

def main():
    if len(sys.argv) > 1:
        prompt = " ".join(sys.argv[1:])
    else:
        print("Enter your prompt (Ctrl+D to submit):")
        prompt = sys.stdin.read().strip()

    if not prompt:
        print("No prompt provided.", file=sys.stderr)
        sys.exit(1)

    client = anthropic.Anthropic()

    with client.messages.stream(
        model="claude-opus-4-7",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)

    print()

if __name__ == "__main__":
    main()
