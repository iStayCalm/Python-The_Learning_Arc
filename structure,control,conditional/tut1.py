print("Saad is Calm")                # Printttttttt

### VARIABLES ###

a = 4                               # int
b = 5.3                             # float
c = 4j                              # complex number
d = "yoo "                          # string

### PRINTING VARIABLES AND TYPES ###
# 
# 
print(a)                            # prints variables
print(type(a))                      # prints type of variable

### ARITHMETIC OPERATIONS ###

add = 5 + 3                         #  M  
sub = 5 - 3                         #  E
mul = 5 * 3                         #  T        
div = 5 / 3                         #  H

### FLOOR DIVISION AND MODULUS ###

floor_division = 5 // 3             # output = 1 ( ans 1.66 and floor function applied so '1' )
modulus = 5 % 3                     # modulus you know
power = 5 ** 3                      # 5 raised to 3
absolute = -53                      # absolute value ( removes - )
round_off = (5.32934578 , 2)        # round off to 2 digits

### STRING MANIPULATION ###

String = "saad"
string2 = String + String[0] + String[2:4] # indexing from 0 , 2:4 takes from 2 to 4-1
print(string2)


String_niga = "saad is sad"
print(String_niga[-2])              # 2nd letter from the back (index starts from -1 from the back)
print("S" + String_niga[1:])        # take everything from index 1


del String_niga                     # delete niga string

strg = "Saad is Calm"
strg2 = strg.replace("is" , "stays") # replace ofcourse
print(strg)
print(strg2)

print(strg.upper())                  # upper      () is neccesary
print(strg.lower())                  # lower        when ANYY . function is called

strgspace = "   CALM   "
print(strgspace + "unstripped")           
print(strgspace.strip() + "stripped")      # Strips XD