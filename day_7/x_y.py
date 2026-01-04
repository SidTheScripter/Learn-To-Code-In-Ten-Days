def compare_x_and_y(x, y): 
    if x > y:
       return "x is greater than y"
    elif y > x:
        return "y is greater than x"
    else:
        return "Both values are equal"
if __name__ == "__main__":
    x = int(input("Enter value for x: "))
    y = int(input("Enter value for y: "))
    answer = compare_x_and_y(x, y)
    print(answer)
    print("all done")