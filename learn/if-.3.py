color_alien = ('green','yellow','red')
if 'green' in color_alien:
    print("kill one is green! ")
else:
    print("null")

print("\033[1;32m-------------------------------\033[0m")
users = ()
if users:
    for user in users:
        if user == "admin":
            print("Hello,admin!")
        else:
            print("Hello,user!")
else:
    print("We need to find some users!")
print("\n")
print("\033[1;32m-------------------------------\033[0m")
current_users = ("zhangsan","lisi","Zhaoer","aZHu","zhaoqiansun")
new_users = ("madayuan","Wangyuyan","azhu","muwanqing","ZHAOer")
for i in new_users:
    for A in current_users:
        if i.lower() in A.lower():
            print("用户名已注册333，请重新输入:")
        else:
            print("此用户可以使用")
print("\n")
print("\033[1;32m-------------------------------\033[0m")
list = []
for i in range(1,10):
    list.append(i)
print(list)
for i in list:
    if i==1:
        print(str(i) + 'st')
    elif i==2:
        print(str(i) + 'nd')
    elif i==3:
        print(str(i) + 'rd')
    else:
        print(str(i) + 'th')


