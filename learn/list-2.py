print("\033[1;31m # SORT \033[0m")
cars = ['bmw','audi','toyota','subaru']
# 按字母排序
cars.sort()
print(cars)
# 按字母相反排序
cars.sort(reverse=True)
print(cars)
# 字母排序不影响原有list
print(sorted(cars))
print(cars)
# 倒序排列
cars.reverse()
print(cars)
a = [1,2,3]
print(a[-2])
print("\033[1;31m-------------------------------- \033[0m")
# range()
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)
print("\033[1;31m--------------------------------\033[0m")
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

print("\033[1;31m--------------------------------\033[0m")
number = [i+0  for i in range(1,22)]
print(number)
print(sum(number))
# 奇数
num = list(range(1,20,2))
for i in num:
    print(i,end= " ")
    print()
# 3的倍数

num = [ i+0 for i in range(3,30,3)]
print(num)

# 立方
num = [ i**3 for i in range(1,10)]
print(num)

print("\033[1;31m--------------------------------\033[0m")
# 切片
num = list(range(1,14))
print(num[-1:])

# 遍历切片

players = ['jemase', 'lilade', 'baoluo.qiaozhi','weide']
for player in players[:3]:
    print(player.title())

# 复制列表
players_copy = players[:]
print(players)

print("\033[1;31m----------------------------------------------\033[0m")
# 元祖
tuple_test = (1,2,3,4,5,6)
print(tuple_test[3])

word = 'Abc'
print(word.lower() == 'abc')

car = 'audi'
if car == 'audi':
    print("Is car == 'audi'? True")
else:
    print("Is car == 'audi'? Flase")

cars = ["aodi","BMW","Aotuo","dazhou","hafo"]
if 'bmw' in cars:
    print(True)
else:
    print(False)