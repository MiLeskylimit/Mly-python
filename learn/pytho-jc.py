name = "mile"
print('Your name is {my_name}'.format(my_name=name))

strdd = ' ab cd '
strdd.strip()
print(strdd.strip())

float_nm = 0.1 + 0.2
print(float_nm)

age = 22
message = "Happy " + str(age) + "rd birthday!"
print(message)

print(5 + 3)
print(4 * 2)
print(12 - 4)
print(int(24 / 3))

test2 = '  \n  languages:\nc\npython\nJava'
print("\nlanguages:\nc\npython\nJava")
print(test2.strip())
print("\n")

# import this

list_test = ['test1', 'test2', 'test3', 'test4', 'test5']
print(list_test[0].title())
print("You think " + list_test[-1].title() + " in where?")

# 列表
print("---------------------------")
liebiao = ['asd', 'dfds', 'darfe', 'dafeief']
print(liebiao[-3])

for i in liebiao:
    print(i.title()  + ", This is name!")
    #print ("序号：%s   值：%s" % (liebiao.index(i) + 1, i))
mototest = []
mototest.append('123')
print(mototest)
mototest.insert(0,'test')
print(mototest)

del mototest[1]
print(mototest)

print('\n')
print('\033[1;31m # POP \033[0m')
pop_tanchu = liebiao.pop(0)
print(liebiao)
print(pop_tanchu)

print("\n")
print('\033[0;31m # REMOVE \033[0m')
remove_test = ['13dfaf', '123dfiafieef', 'fdoafjeifa', 'fia93a']
print(remove_test)
remove_test.remove('123dfiafieef')
print(remove_test)

print('\033[1;31m # Laern ! \033[0m')
jiabin_name = ['lisi','zhangsan','wangwu','zhaoer']
for i in jiabin_name:
    print("Hello! Dear " + i + " Welcome on!" )
print("\n")
number = jiabin_name.index('wangwu')
jiabin_tihuan = jiabin_name.pop(number)
jiabin_name.insert(2,'wangmazi')
for i in jiabin_name:
    print("Hello! Dear " + i + " Welcome on!")

print("\n")
jiabin_name.insert(0,"zhaoqiansun")
print(jiabin_name[0] + " Find big a table!")
len_num = len(jiabin_name)
print(len_num)
print("\n")

for i in jiabin_name:
    if len_num > 2:
        person = jiabin_name.pop()
        print(person,'很抱歉，不能邀请您！')
else:
    for i in jiabin_name:
        print("Hello! Dear " + i + " Welcome on!")

print("\n")






