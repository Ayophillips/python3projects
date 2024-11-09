age = int(input("How old are you?\n")) #converts input string to integer

decades = age // 10 #two backslashes is a whole number division
years =  age % 10

print("You are " + str(decades) + " decades and " + str(years) + " years old" ) #converts float to string