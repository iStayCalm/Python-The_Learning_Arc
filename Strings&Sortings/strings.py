#declare string
str1 = "saad is calm ofcourse"

#NPC String Methods
print(f" -:-: NPC String Methods :-:- \n")

print(str1.upper())         #Convert to Upper
print(str1.lower())         #Convert to Lower
print(str1.capitalize())    #First letter capital
print(str1.title())         #First letter capital of every word
print(str1.swapcase())      #change case: lower->upper __ upper->lower


#Searching in String
print(f"\n\n\n -:-: Searching in String :-:- \n")

print(str1.find("calm"))        # 8     <- index of 'c'
print(str1.count("a"))          # 3     <- number of 'a'
print(str1.startswith("saad"))  # True
print(str1.index("c"))          # 8     <- Returns index of first 'c' OR throw ERROR if not present


#Modification of String
print(f"\n\n\n -:-: Modification of String :-:- \n")

saad = "      saaad      "

print(saad.lstrip())                               #Remove Spaces from left
print(saad.rstrip())                               #Remove Spaces from right
print(saad.strip())                                #Remove Spaces

saad = "saaad"
print(saad.replace("aa","o"))                      
print(saad.replace("a","o"))                       #Replace (old, new)
print(saad.replace("aaa","a"))

print("_".join(["saad","is","calm"]))               #join a string aaju baaju

#Splitting and Combining
print(f"\n\n\n -:-: Splitting and Combining :-:- \n")

str2 = "saad.is.calm"

print(str2.split("."))          #split each words split(separator)
print(str2.rsplit("."))         #split each words split(separator) from right
print(str2.partition("."))      #seperates [ word before separator , separator , word after separator ]

str3 = "saad\nis\ncalm"
print(str3.splitlines())

#Checkin Stringss
print(f"\n\n\n -:-: Checkin Stringss :-:- \n")

nstr = "69"

print(nstr.isalpha())           #checks if string is Alphabet 
print(nstr.isdigit())           #checks if string is Number
print(nstr.isalnum())           #checks if string is alpha or numeric / alphanumeric
print(nstr.isspace())           #checks if string is white space



#String Slicing 
print(f"\n\n\n -:-: Strings Slicingg *shu *shu :-:- \n")

yo = "Hello, CalmZ"

print(yo[0:5])      #from 0 to 4
print(yo[:5])       #from 0 (default) to 4
print(yo[7:])       #from index 7 to default end of string

#negative index
print(yo[-5:])      #last 5 chars

#stepping (BIG STEPPAA)

print(yo[::2])      #prints every 2nd char
print(yo[::3])      #prints every 3rd char
print(yo[::-1])     #Reverse printing







# -:-: STRING FORMATTING :-:-
print(f"\n\n\n\n\n\n -:-: STRING FORMATTING :-:- \n")

name = "halka halka"
age = 9

#old
print("Name : %s ,Roll : %d" %(name, age))

#mid
print("\nMy name is {} and I am {} years old.".format(name, age))

#I AM NOT MID
print(f"\nname {name}, age is {age}")

pi=3.1428
print(f"\nPI : {pi:.2f}")



