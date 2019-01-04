# DICT
a = {'name1': 'zhagnsan','name2': 'lisi','name3': 'wangmazi'}
print(a['name1'])
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")
print("\n")
print("\033[1;32m-------------------------------\033[0m")

alien_0 ={'color': 'green', 'points':5}
print(alien_0)
alien_0['color'] = 'green12123';
alien_0['number'] = 3434
print(alien_0)
print ("CSTEST" + '.' + alien_0['color'])

print("\n")
print("\033[1;32m-------------------------------\033[0m")
person = {
          "first_nmae": "zhangsan",
          "last_name": "lisi",
          "age": 18,
          "city": "chengdu",
          }
print(person)
print(person['last_name'])

for i,m in person.items():
    print("\nKey:" + i)
    print("value:" + str(m))

print("/n")
favorite_languages = {
    'jie': 'python',
    'wan': 'UE',
    'ting': 'UI',
    'super': 'ruby',
    'nanyi': 'python',
}
friends =  ['wan', 'ting']
for name in favorite_languages:
    print(name.title())

    if name in friends:
        print("HI " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

print("\n")
for i in set(favorite_languages.values()):
    print(i)
print("\n")
for i in  sorted(favorite_languages.keys()):
    print(i)
# values-sorted-keys-set(剔除重复值)-itmes(遍历所有的键值对）

print("\n")
rivers = {
    'niluo': "gangguo",
    'Amazon': "nanmei",
    'changjiang': "chognqing",
}
for i,m in rivers.items():
    print("\nThe " + i.title() + " run " + m.title() + "!" )
    if 'niluo' in rivers:
        print("true")












