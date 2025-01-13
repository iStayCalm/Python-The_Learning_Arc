#_Conditions_

# if-else
age = int(input("Enter your age : "))

if age > 18:
    print(f"Your age is {age} that is greater than 18 :O ")

elif age == 18:
    print(f"Your age is {age} that is equals to 18 :/ ")

else:
    print(f"Your age is {age} that is less than 18 :( ")



# ternary
print("Big Boii") if age >= 18 else print("Minoooor")



# nesting
internal_marks = int(input("\nEnter your internal marks : "))

if age >= 18:

    print("you are an adult")

    if internal_marks > 22:
        print("and a topper :O ")

    else:
        print("but a dummy XD ")

else:
    print("you're a Minoo")

    if internal_marks > 22:
        print("but a topper")

    else: 
        print("and also a dummy")
