'''
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

print("\033[1;32m ------------------------------------- \033[0m")

promt = "feifjieafeffffffffffffffffffffffffffffffffffffffffffl;adfiefaifoefjiafji"
promt += "\nwhat is your first name?"

name = input(promt)
print("Hello, " + name + "!")
print("\n")s
'''
'''
age = input("How old are you? ")
print(age)
nb = int(age)
print(nb  >= 18)
print(7 % 3)
'''
'''
car_lease = input("Hello, what car do you want to lease?  ")
car_lease += "\nLet me see if I can find you a Subaru!"
print(car_lease)
'''
'''
person = input("Hell, How many people are there altogether?  ")
person = int(person)
if person > 8:
    print("Sorry,not Empty position.")
else:
    print("Please be seated.")
'''
numb = input("Please input a number:  ")
numbs = int(numb) % 10
if  numbs == 0:
    print("是10的整倍数")
else:
    print("不是10的整倍数")

