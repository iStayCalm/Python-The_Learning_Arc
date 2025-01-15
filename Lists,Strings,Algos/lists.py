int_list = [23,53,124,523]

print(f"printing val at index 0 : {int_list[0]}")
print(f"Printing list : {int_list}")

int_list.append(313)
print(f"appended an item : {int_list}")

int_list.remove(523)
print(f"Removed an item : {int_list}")

print(f"\nList can be mix of different data types")

l1 = [1,2,3,4,5]
l2 = ["saad","is","calm","hehe ;)"]
l3 = [1,"saad",6.9,True]

print(f"list 1 integers       : {l1}")
print(f"list 2 strings        : {l2}")
print(f"list 3 mixed elements : {l3}")

print("\n")

#list can be created with tuple

atup = 123,4235,234,4,313

alist = list(atup)
print(alist)
