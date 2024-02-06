num1 = int(input("Enter number 1: "))
op = input("Enter the operator: ")
num2 = int(input("Enter number 2: "))

if op == "+":
    total = num1 + num2
    print(f"{num1} + {num2} = {total}")

elif op == "-":
    total = num1 - num2
    print(f"{num1} - {num2} = {total}")

elif op == "*":
    total = num1 * num2
    print(f"{num1} * {num2} = {total}")

elif op == "/":
    if num2 != 0:
        total = num1 / num2
        print(f"{num1} / {num2} = {total}")
    else:
        print("You can't divide by 0")

elif op == "**":
    total = num1 ** num2
    print(f"{num1} ** {num2} = {total}")

elif op == "//":
    total = num1 // num2
    print(f"{num1} // {num2} = {total}")

elif op == "%":
    total = num1 % num2
    print(f"{num1} % {num2} = {total}")

else:
    print("Invalid operator") 
