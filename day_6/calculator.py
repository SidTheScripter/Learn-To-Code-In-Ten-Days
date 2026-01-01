#!/usr/bin/env python3
import sys

def compute(a, b, op):
    ops = {
        'add': lambda x, y: x + y,
        '+': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        '-': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        '*': lambda x, y: x * y,
        'divide': lambda x, y: x / y,
        '/': lambda x, y: x / y,
    }
    key = op.lower()
    if key not in ops:
        raise ValueError(f"Unknown operation: {op}")
    if key in ('divide', '/') and b == 0:
        raise ZeroDivisionError("Division by zero")
    return ops[key](a, b)

def parse_number(s):
    try:
        if '.' in s or 'e' in s.lower():
            return float(s)
        return int(s)
    except Exception:
        return float(s)

def main():
    if len(sys.argv) == 4:
        s1, s2, op = sys.argv[1], sys.argv[2], sys.argv[3]
    else:
        s1 = input("Enter first number: ").strip()
        s2 = input("Enter second number: ").strip()
        op = input("Enter operation (add, subtract, multiply, divide or + - * /): ").strip()

    try:
        a = parse_number(s1)
        b = parse_number(s2)
    except Exception:
        print("Invalid number input")
        sys.exit(1)

    try:
        result = compute(a, b, op)
    except ZeroDivisionError:
        print("Error: division by zero")
        sys.exit(1)
    except ValueError as e:
        print(e)
        sys.exit(1)

    if isinstance(result, float) and result.is_integer():
        result = int(result)
    print(result)

if __name__ == "__main__":
    main()