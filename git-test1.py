def calcute():
    print("Simple Math Calculator")
    print("Choose an operation: +  -  *  /")

    op = input("Operation: ")
    a = float(input("First number: "))
    b = float(input("Second number: "))

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        if b == 0:
            print("Error: division by zero")
        else:
            print("Result:", a / b)
    else:
        print("Invalid operation")

calcute()
