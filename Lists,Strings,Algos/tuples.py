#TUPLES ARE NON_EDITABLE LISTS inshort but there is more to it

tup = (123,53,132,54)

print(tup)
print(type(tup), "\n")

n = len(tup)

for i in range(0,n):
    print(f"elements at index {i}: {tup[i]}")

print("\nValue in tup[-3] = ", tup[-3])
print("Value in tup[-1] = ", tup[-1])
print("Value in tup[-4] = ", tup[-4])
print("Value in tup[-2] = ", tup[-2], "\n")

for i in tup:
    print(i, end=" ")

str_tup = ("hello","saad")
print(f"\n")
#tuple addition (Concatenation)
add_tup = tup + str_tup
print("\n",add_tup)

#tuple Nesting
nest_tup = (tup,str_tup)
print("\n",nest_tup)

#repetation in tuples
rep_tup = ("saad",)*4
print("\n",rep_tup)

#Slicing and shi
print("\n")
t = [634,465,343256,5323,65]
print(t[1:]) #prints from index 1
print(t[::-1]) #prints in reverse
print(t[2:4])  #from index 2 to 3