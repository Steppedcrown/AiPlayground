#!/usr/bin/env python3
import sys
import anthropic

def main():
    client = anthropic.Anthropic()
    messages = []

    while True:
        try:
            prompt = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            sys.exit(0)

        if not prompt:
            continue

        messages.append({"role": "user", "content": prompt})

        print("\nClaude: ", end="", flush=True)
        response_text = ""
        with client.messages.stream(
            model="claude-opus-4-7",
            max_tokens=4096,
            messages=messages,
        ) as stream:
            for text in stream.text_stream:
                print(text, end="", flush=True)
                response_text += text
        print()

        messages.append({"role": "assistant", "content": response_text})

if __name__ == "__main__":
    main()
