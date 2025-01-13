print("A Calculator using UDFs")

def sub(num1:int,num2:int):
    num3 = num1 - num2
    print(num3)
def mul(num1:int,num2:int):
    num3 = num1 * num2
    print(num3)
def div(num1:int,num2:int):
    num3 = num1 / num2
    return num3
def add(num1:int,num2:int):
    num3 = num1 + num2
    return num3
    
number1 = int(input("Enter first number : "))
number2 = int(input("Enter second number : "))

func = input("Enter the thing you wanna do (+,-,x,/) : ")

if func == "+":
    add(number1,number2)
elif func == "-":
    sub(number1,number2)
elif func == "x":
    print(mul(number1,number2))
elif func == "/":
    print(div(number1,number2))
else:
    print("Invalid ;)")    

    