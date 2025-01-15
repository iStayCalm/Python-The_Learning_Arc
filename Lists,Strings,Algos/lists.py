int_list = [6,12,18,25]

print(f"printing val at index 0 : {int_list[0]}")
print(f"Printing list : {int_list}")

int_list.remove(25)
print(f"Removed an item : {int_list}")

int_list.append(24)
print(f"Appended an item : {int_list}")

int_list.insert(4,30)
print(f"Inserted an item : {int_list}")

int_list.extend([36,42,48])
print(f"Extended items : {int_list}")





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
print("\n")





#Create a list [2, 2, 2, 2, 2]
a = [3] * 7

#Create a list [0, 0, 0, 0, 0, 0, 0]
b = [0] * 5

print(a)
print(b)
print("\n")





#Updating,Removing, Popping - elements into List

alist = [10,20,30,40,50]
print(f"Before Updating : {alist}")
alist[0] = 11
print(f"After updating : {alist}")

alist.remove(11)
print(f"After Removing : {alist}")

pop_ele = alist.pop(1)
print(f"After Popping : {alist}")
print(f"The popped element : {pop_ele}")
print("\n")





#Iteration of Lists

ilist = ["strawberry", "banana" , "mango", "apple" , "pineapple"]

for i in ilist:
    print(i , end=" : ")
print("\n")




    
#Matrix List

mlist = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in mlist:
    print(i)
    
print(f"element at index (1,2) : {mlist[1][2]}")