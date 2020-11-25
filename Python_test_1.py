# Tuple :
def get_info():
    name="alex"
    age =6
    return name,age

name,age=get_info()

print(type(get_info()))
print(name)
print(age)

# "Modify" Tuple:
temp = ("龙猫","泰迪","叮当猫")
print(temp)
temp = temp[:1] + ("小猪佩奇",)+temp[1:]
print(temp)

# Silce:
a='python'
b=a[::-1]
print(b)
#nohtyp

a = [1, 2, 3,4, 5]
print(a)
# [1 2 3 4 5]

print(a[-1])
#取最后一个元素
#结果：[5]

print(a[:-1])
#除了最后一个取全部
#结果：[1 2 3 4]

print(a[::-1])
#取从后向前（相反）的元素
#结果：[5 4 3 2 1]

print(a[2::-1])
#取从下标为2的元素翻转读取
#结果：[3 2 1]

print(a[1:])
#取第二个到最后一个元素
#结果：[2 3 4 5]

a = 'a','b','c' #<class 'tuple'>
b = "a","b","c" #<class 'tuple'>
print(type(a))
print(type(b))

mylist =['a','b','c']
mytup =('1','2','3')
mystr = 'my name is'

for p in mylist:
    print(p)


for r in mytup:
    print(r)


for ch in mystr:
    print(ch,end=' ')

seq = ['one', 'two', 'three']
for i, element in enumerate(seq):

    print (i, element)

import time

struct_time = time.strptime("30 Nov 00", "%d %b %y")
print ("返回的元组:",  struct_time)

from struct import Struct
values = 7,6,42.3,b'Guido'
demo = Struct('iif10s')
print ("ffff".format(demo.size))




