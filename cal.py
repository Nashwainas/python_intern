def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b if b != 0 else 0

def call():
    while True:
        a = float(input("Enter your first number for calculation: "))
        b = float(input("Enter your second number for calculation: "))
        x = int(input("Enter 1 to add, 2 to subtract, 3 to multiply, 4 to divide: "))
        if 1 <= x <= 4:
            switch_case(x, a, b)
        else:
            print("Invalid choice.Exiting.")
            break

def switch_case(key, a, b):
    if key == 1:
        print("Addition:", add(a, b))
    elif key == 2:
        print("Subtraction:", sub(a, b))
    elif key == 3:
        print("Multiplication:", mul(a, b))
    elif key == 4:
        print("Division: ")
        s=div(a,b)
        if s==0:
            print("Attempting to divide by zero")
        else:
            print(s)

call()
