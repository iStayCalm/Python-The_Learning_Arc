item_list = ["Strawberry","banana","apple"]
item_price = [70,60,50]

hit = 0     
n=len(item_list)
total = 0

print("\nEnter the index_no of item you wanna buy ;) ")

for i in range(0,n):
    print(f"{i+1}. {item_list[i]} - price = ${item_price[i]}")

print(f"{n+1}. for bill\n")
while hit != n+1:
    hit = int(input("Enter index: "))

    if hit < n+1:
        print(f"{item_list[hit-1]}-price:${item_price[hit-1]}: Added to cart.")
        total = total + item_price[hit-1]

    elif hit == n+1:
        print(f"\nYour total is ${total}")
        
    else:
        print(f"Invalid index , Kal ana ")