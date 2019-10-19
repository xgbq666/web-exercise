f = open("data.txt", "r")
str = f.read()
f.close()
i = 1
m = 0
str1 = -1
a = input("查找的单词是")
while i <= len(str):
    str1 = str.find(a, i, i + len(a) + 1)
    if str1 >= 0:
        m = m + 1
    i = i + 1
print(a, "出现的次数为", m)
