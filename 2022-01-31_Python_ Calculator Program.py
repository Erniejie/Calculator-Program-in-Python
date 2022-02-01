# Calculator Program in Python
#Computer Programming Tutor- Jan 31 2022
operation = input("""
Please Type in the Math Operation you would like to Carry out:
+ For Addition
- For Substraction
* For Multilication
/ For Division
"""
    )


num1 =int(input("Enter Your First Number:"))
num2 =int(input("Enter Your Second Number:"))


if operation == "+":
    print("{}+{}".format(num1,num2))
    print(num1 + num2)

elif operation == "-":
    print("{}-{}".format(num1,num2))
    print(num1-num2)

elif operation == "*":
    print("{}*{}".format(num1,num2))
    print(num1*num2)

elif operation == "/":
    print("{}/{}".format(num1,num2))
    print(num1/num2)

else:
    print("Invalid Operator")
