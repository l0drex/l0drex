from random import randrange
key = [randrange(10) for i in range(0,16)]
num = ""
for n in key: num = num + str(n)
print(num)
