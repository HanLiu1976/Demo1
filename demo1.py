d = {'name': 'amy', 'age': 18}
t = (1, 2, 3)

def func(a, *args, **kwargs):
    print('结果：')
    print(f'位置参数：{a}')
    print(f'不定长元组参数：{args}')
    print(f'不定长元组参数：{args[0]}')
    print(type(args[0][0]))
    print(f'不定长键值对参数：{kwargs.get("age")}')

func(1, t, **d)

def increase(data):
    return [x*2 for x in data]


def increase(data):
    return [x**2 for x in data]




data=[1,2,3]
print(increase(data))


def numbers():
    a =0
    for i in range(3):
        yield a
    yield 100

for num in numbers():
    num

def blah():
	yield 0
	a = 1
	while a < 3:
		a = a + 1
		yield a
	yield a
nums = blah()
next(nums)
