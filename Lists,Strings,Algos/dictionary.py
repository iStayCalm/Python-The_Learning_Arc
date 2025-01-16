#defining dictionary
base = {1 : "saad" , 2: 177 , 3: "sem-2", 4: 9.4}
print(base)
print("\n")

#other way
base2 = dict(
    name = "saad",
    roll = 177,
    stdy = "sem 2",
    cgpa = 9.4
)

print("Print Keys : ")
for i in base2:
    print(i, end=" ")
print("\n")

print("Print values : ")
for i in base2.values():
    
    print(i, end=" ")
print("\n")
  
print("Print Both :") 
for i in base2:
    print(i ,":", base2.values)
print("\n")

#accesing dict. with keys
print(base[1])

print(base2["stdy"])
print("\n")



#Updating and Adding into Dictionary

base2["age"] = 19
base2["name"] = "CalmZ"
print(base2)