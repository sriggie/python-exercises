import math
# Create a scientific calculator which displays an interactive menu to the user, to allow them pick an operation(option). Operations -> addition, subtraction, multiplication, division, modulus, power, sqrt, log, sine, cosine, tangent -> math module.

while True:
    # Display the menu options to the user
    print("\nChoose Math Operation From The Menu\n\n1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Modulus\n6 - Raising To A Number\n7 - Square Root Of A Number\n8 - Logarithm\n9 - Sine\n10 - Cosine\n11 - Tangent")

    # Prompt the user to enter their choice
    oper = input("\nEnter Your Option From The Menu: \n")

    # Addition
    if oper == "1":
        print("\t\t\t\t\tAddition")
        num1 = float(input("\nFirst Number: "))
        num2 = float(input("\nSecond Number: "))
        print(f"\nThe sum of {num1} and {num2} is: {(num1 + num2)}")

        back = input("\nGo Back To The Main Menu? (y/n): ")
        if back.lower() == "y":
            continue
        else:
            break

    # Subtraction
    elif oper == "2":
        print("\t\t\t\t\tSubtraction")
        num1 = float(input("\nFirst Number: "))
        num2 = float(input("\nSecond Number: "))
        print(f"\nThe difference of {num1} and {num2} is: {(num1 - num2)}")

        back = input("\nGo Back To The Main Menu? (y/n): ")
        if back.lower() == "y":
            continue
        else:
            break

    # Multiplication
    elif oper == "3":
        print("\t\t\t\t\tMultiplication")
        num1 = float(input("\nFirst Number: "))
        num2 = float(input("\nSecond Number: "))
        print(f"\nThe Product of {num1} and {num2} is: {(num1 * num2)}")

        back = input("\nGo Back To The Main Menu? (y/n): ")
        if back.lower() == "y":
            continue
        else:
            break

    # Division
    elif oper == "4":
        print("\t\t\t\t\tDivision")
        num1 = float(input("\nFirst Number: "))
        num2 = float(input("\nSecond Number: "))
        print(f"\nThe Quotient of {num1} and {num2} is: {(num1 / num2)}")

        back = input("\nGo Back To The Main Menu? (y/n): ")
        if back.lower() == "y":
            continue
        else:
            break

    # Modulus
    elif oper == "5":
        print("\t\t\t\t\tModulus")
        num1 = float(input("\nFirst Number: "))
        num2 = float(input("\nSecond Number: "))
        print(f"\nThe Modulo of {num1} and {num2} is: {(num1 % num2)}")

        back = input("\nGo Back To The Main Menu? (y/n): ")
        if back.lower() == "y":
            continue
        else:
            break

    # Raising To A Power
    elif oper == "6":
        print("\t\t\t\t\tPower Of A Number")
        num1 = float(input("\nEnter The Base Number: "))
        num2 = float(input("\nEnter The Exponent/Power: "))
        # print(f"The power of {num1} raised to {num2} is: {num1 ** num2}")
        # print(f"The power of {num1} raised to {num2} is: {pow(num1, num2)}")
        print(f"The power of {num1} raised to {num2} is: {math.pow(num1, num2)}")

        back = input("\nGo Back To The Main Menu? (y/n): ")
        if back.lower() == "y":
            continue
        else:
            break

    # Square Root A Number
    elif oper == "7":
        print("\t\t\t\t\tPower Of A Number")
        num = float(input("\nEnter the number for finding the square root: "))
        print(f"The Square Root of {num} is:  {math.sqrt(num)}")

        back = input("\nGo Back To The Main Menu? (y/n): ")
        if back.lower() == "y":
            continue
        else:
            break

    # Log Of A Number
    elif oper == "8":
        print("\t\t\t\t\tLogarithm Of A Number")
        num = float(input("\nEnter the number To Calculate the Logarithm To Base 2: "))
        print(f"\nThe Logarithm of {num} is:  {math.log(num, 2)}")

        back = input("\nGo Back To The Main Menu? (y/n): ")
        if back.lower() == "y":
            continue
        else:
            break
    # Trigonometry - SINE
    # Sine Of A Number
    elif oper == "9":
        print("\t\t\t\t\tSine Of A Number")
        num = float(input("\nEnter the number(Degrees) To Calculate it's Sine: "))
        print(f"\nThe Sine of {num} is:  {math.sin(math.radians(num))}")

        back = input("\nGo Back To The Main Menu? (y/n): ")
        if back.lower() == "y":
            continue
        else:
            break
    # Trigonometry - SINE
    # Sine Of A Number
    elif oper == "10":
        print("\t\t\t\t\tCosine Of A Number")
        num = float(input("\nEnter the number(Degrees) To Calculate it's Coine: "))
        print(f"\nThe Sine of {num} is:  {math.cos(math.radians(num))}")

        back = input("\nGo Back To The Main Menu? (y/n): ")
        if back.lower() == "y":
            continue
        else:
            break
    # Trigonometry - SINE
    # Sine Of A Number
    elif oper == "11":
        print("\t\t\t\t\tTangent Of A Number")
        num = float(input("\nEnter the number(Degrees) To Calculate it's Tangent: "))
        print(f"\nThe Sine of {num} is:  {math.tan(math.radians(num))}")

        back = input("\nGo Back To The Main Menu? (y/n): ")
        if back.lower() == "y":
            continue
        else:
            break
