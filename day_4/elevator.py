#!/usr/bin/env python3
"""Elevator direction helper.

Prompts for the current floor and the floor you want to go to,
then prints the direction to move: "Up <n>", "Down <n>", or
"You are already on that floor" when the floors are equal.
"""

def get_int(prompt: str) -> int:
    try:
        val = input(prompt)
        return int(val.strip())
    except Exception:
        print("Invalid input; please enter an integer.")
        raise SystemExit(1)


def get_int_optional(prompt: str) -> int | None:
    try:
        val = input(prompt)
        if val.strip() == "":
            return None
        return int(val.strip())
    except Exception:
        print("Invalid input; please enter an integer.")
        raise SystemExit(1)


def main() -> None:
    current = get_int("Current Floor: ")
    target = get_int("Floor you want to go: ")
    ignore = get_int_optional("Floor to ignore (press enter to skip): ")
    diff = target - current
    
    # Account for ignored floor when crossing it
    if ignore is not None and ((current < ignore and target > ignore) or (current > ignore and target < ignore)):
        diff -= 1
    
    if diff > 0:
        print(f"Up {diff} floor(s)")
    elif diff < 0:
        print(f"Down {abs(diff)} floor(s)")
    else:
        print("You are already on that floor")


if __name__ == "__main__":
    main()
