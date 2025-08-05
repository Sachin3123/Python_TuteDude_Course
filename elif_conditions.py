operand_1 = int(input("Enter first operand: "))
operand_2 = int(input("Enter second operand: "))

operator = input("Enter operator (+, -, *, /): ")

# 

if operator== '+':
    print(operand_1 + operand_2)

elif operator=='-':
    print(operand_1 - operand_2)

elif operator=='*':
    print(operand_1 * operand_2)
elif operator=='/':
    print(operand_1 / operand_2)
else:
    print("Invalid operator. Please use +, -, *, or /.")