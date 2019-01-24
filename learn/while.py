'''
# input use
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
'''
numb = input("Please input a number:  ")
numbs = int(numb) % 10
if  numbs == 0:
    print("是10的整倍数")
else:
    print("不是10的整倍数")
'''
'''
# while
while_numb = 1
while while_numb <= 5:
    print(while_numb)
    while_numb += 1
'''
'''
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

messges = ""
while messges != 'quit':
    messges = input(prompt)
    if messges != 'quit':
        print(messges)
'''
'''
# break use
active = True
while active:
    messges = input(prompt)
    if messges == "quit":
        break
    else:
        print(messges)
'''
'''
# continue use
current_numb = 0
while current_numb <10:
    current_numb += 1
    if current_numb % 2 == 0:
        continue
    print(current_numb)
'''
# list
'''
part = "\nHello,Please input pizz parts:  "
parts = ""
while parts != 'quit':
    parts = input(part)
    if parts != 'quit':
        print("你的pizz中有" + parts)
'''
'''
moves = "1"
while moves != "":
    move = input("Hello,Please input your years:  ")
    moves = int(move)
    if moves < 3 :
        print("请免费观看")
        continue
    if moves >= 3 and moves <= 12 :
        print("您的票价为10美元")
        continue
    if moves > 12 :
        print("您的票价为15美元")
        continue
    if move = "quit":
        break

'''








