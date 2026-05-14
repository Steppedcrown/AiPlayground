#!/usr/bin/env python3
import sys
import anthropic

def main():
    if len(sys.argv) > 1:
        prompt = " ".join(sys.argv[1:])
    else:
        prompt = ""
        while not prompt:
            try:
                prompt = input("Enter your prompt: ").strip()
            except EOFError:
                print()
                sys.exit(0)
            except KeyboardInterrupt:
                print()
                sys.exit(0)

    client = anthropic.Anthropic()

    with client.messages.stream(
        model="claude-opus-4-7",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
    
    print()  # Ensure we end with a newline

if __name__ == "__main__":
    main()
