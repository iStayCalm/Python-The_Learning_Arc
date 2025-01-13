def prime(num: int):
    flag:int

    for i in range(2,num-1):
        
        if num==1:
            flag=1
            break
        elif num==2:
            flag=1
            break
        elif num%i == 0:
            print(f"checking with {i}")
            flag = 0
            break
        else:
            print(f"checking with {i}")
            flag = 1
    return flag

number = int(input("Enter Your number : "))

if prime(number):
    print(f"{number} is a prime :O ")

else:
    print(f"{number} isnt a prime :/ ")
