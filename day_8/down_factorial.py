
def down_factorial(n):
    if n == 0:
        return 1
    else:
        return n * down_factorial(n - 1)  
def factorial_forloop(n):
    result = 1
    for i in range(n, 0, -1):
        result = result * i
    return result   
if __name__ == "__main__":
    number = int(input("Enter a non-negative integer:\n "))
    result = down_factorial(number)
    print(f'The down factorial of {number} is {result}')