#!/usr/bin/env python3
def say_cool_times(name, count, coolness):
    for _ in range(count):
        print(f"{name} is {coolness} cool!")


def usage():
    print("Usage: python3 hello.py <count> <name> <coolness>")
    print("  count: float (number of times, will be floored)")
    print("  coolness: float")
    print("Or run without args to be prompted.")


if __name__ == "__main__":
    import sys

    count = None
    name = None
    coolness = None

    if len(sys.argv) >= 4:
        try:
            count = float(sys.argv[1])
        except ValueError:
            print("Error: count must be a float.")
            usage()
            sys.exit(1)
        name = sys.argv[2]
        try:
            coolness = float(sys.argv[3])
        except ValueError:
            print("Error: coolness must be a float.")
            usage()
            sys.exit(1)
    else:
        try:
            count_input = input("Count (number of times, float): ")
            count = float(count_input)
        except ValueError:
            print("Error: count must be a float.")
            sys.exit(1)
        name = input("Your name: ")
        try:
            coolness_input = input("Coolness level (float): ")
            coolness = float(coolness_input)
        except ValueError:
            print("Error: coolness must be a float.")
            sys.exit(1)

    say_cool_times(name, int(count), coolness)
