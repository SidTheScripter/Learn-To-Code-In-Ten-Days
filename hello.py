#!/usr/bin/env python3
"""Interactive hello script.

This script prompts the user for a name and a count, then prints
"<name> is cool" that many times.
"""

def prompt_int(prompt: str, default: int) -> int:
    try:
        val = input(prompt)
        if val.strip() == '':
            return default
        return int(val)
    except ValueError:
        print('Invalid number, using default:', default)
        return default


def main():
    name = input('Enter name (default: sid): ').strip() or 'sid'
    count = prompt_int('Enter count (default: 5): ', 5)
    count = max(0, count)
    for _ in range(count):
        print(f"{name} is cool")


if __name__ == '__main__':
    main()
if __name__ == '__main__':
