import random

num = random.randint(1,100)

#print(f"{num}")



inum = int(input("Enter your 1st guess : "))
guess_count=1

while True:

    if inum < num:
        guess_count += 1
        print(f"{inum} is lower than the number\n")
        print(f"attempt {guess_count}:")
        tempnum = int(input("Try guessing another number : "))
        print(f"\n")
        inum = tempnum

    elif inum > num:
        guess_count += 1
        print(f"{inum} is higher than the number\n")
        print(f"attempt {guess_count}:")
        tempnum = int(input("Try guessing another number : "))
        print(f"\n")
        inum = tempnum
    
    else:
        print(f"{num} Guessed in {guess_count} attempts")
        break