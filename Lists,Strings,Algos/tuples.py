# TUPLES ARE NON-EDITABLE LISTS in short but there is more to it

tup = (123, 53, 132, 54)

print(tup)
print(type(tup), "\n")

n = len(tup)

for i in range(0, n):
    print(f"Elements at index {i}: {tup[i]}")

print(f"\nPrinting with negative index:")
print("Value in tup[-3] = ", tup[-3])
print("Value in tup[-1] = ", tup[-1])
print("Value in tup[-4] = ", tup[-4])
print("Value in tup[-2] = ", tup[-2], "\n")

print(f"\nPrinting tuple in a line:")
for i in tup:
    print(i, end=" ")
print("\n")

# String Tuple:
print("String Tuple:")
str_tup = ("hello", "saad")
for i in str_tup:
    print(i, end=" ")
print(f"\n")

# Tuple addition (Concatenation)
print(f"Tuple addition:")
add_tup = tup + str_tup
print(add_tup, "\n")

# Tuple Nesting
print(f"Nesting in Tuples:")
nest_tup = (tup, str_tup)
print(nest_tup, "\n")

# Repetition in tuples
print("\nRepetition in Tuples:")
rep_tup = ("saad",) * 4
print(rep_tup)

# Slicing and reverse printing:
print("\nSlicing and reverse printing:")
t = [634, 465, 343256, 5323, 65]
print(t[1:])  # prints from index 1
print(t[::-1])  # prints in reverse
print(t[2:4])  # from index 2 to 3

# Can delete tuple with del(*tuple_name*)
del(tup)

# Multi-DataType Tuples
print("\nMulti-DataType Tuples:")
mul_tup = (12, "yoo", False, 7.69)
print(mul_tup)

# List to Tuple
print("\nList to Tuple:")
listo = [53, 245, 446, 25]
list_tup = tuple(listo)
print(list_tup)
print(type(list_tup))

# Looping in Tuples
print(f"\nLooping in Tuples:")
looptup = ('saad',)

for i in range(5):
    looptup = (looptup,)
    print(looptup)
# something KWRAEZY!! i couldn't understand

# Different Ways of Creating a Tuple
# 1. Using round brackets - normal

# 2. Without Brackets
print("\nWithout brackets:")
tup2 = 3, 4, 5, 5
print(tup2)

# 3. Tuple Constructor
print(f"Tuple Constructor (from a list):")
tup3 = tuple([6, 34, 2, 443522, 2])  # useful when you don't know the data and want to make a tuple out of a list
list3fortup3 = [32, 56345, 342, 23]
tup3fromlist3 = tuple(list3fortup3)
print(tup3fromlist3)

# 4. Empty Tuple
print(f"Empty Tuple:")
tup4 = ()
print(tup4)

# 5. Single Element Tuple
print("1 element tuple:")
tup5 = (10,)  # can't put only (10) because it will just be an integer then...
print(tup5)

# 6. Using Tuple Packing
print("Using Tuple Packing")
a, b, c = 6, 3, 41
tup6 = (a, b, c)  # data can be packed into tuple
print(tup6)
