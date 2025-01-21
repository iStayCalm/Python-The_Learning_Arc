import math 

city1 = input("Enter Start Location : ")
city2 = input("Enter Final Location : ")

dist = int(input("The distance Between two location : "))
print("\n")

num_check = math.ceil(dist/20)
print(num_check)

check_list = [0] * num_check
print(check_list)
timetaken = 0

for i in range (0,num_check):
   check_list[i] = int(input("Enter speed for checkpoint now : "))
   print(check_list)

avg_sum = 0 
for i in range (0,num_check):
    avg_sum = avg_sum + check_list[0]

avg_speed = avg_sum / num_check

print(f"Average Speed from {city1} to {city2} is : {int(avg_speed)}km/h")
timetaken = (dist / avg_speed) *60
print(f"Time taken to reach {city2} from {city1} is : {timetaken}")
