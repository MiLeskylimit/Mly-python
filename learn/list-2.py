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