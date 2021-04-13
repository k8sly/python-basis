# 1、标准数据类型
# Python有五个标准的数据类型：
#    Numbers（数字）：int, long, float, complex(复数)
#    String（字符串）
#    List（列表）
#    Tuple（元组）
#    Dictionary（字典)

# 2、基本数据类型
counter = 100          # 整型变量
miles = 1000.0         # 浮点型变量
name = "runOob"        # 字符串

print(counter)
print(miles)
print(name)

# 3、多个变量赋值
a = b = c = 1
print(a)
print(b)
print(c)

a1, b1, c1 = 2, 2.0, "Join"
print(a1)
print(b1)
print(c1)

# 4、Python字符串
string = "Hello World!"
print(string)
print(string[0])
print(string[2:5])
print(string[2:])
print(string * 2)        # 输出字符串两次
print(string + " Oye")   # 拼接字符串

# 5、Python列表
lists = ['runOob', 786, 2.23, 'john', 70.2]
tinyLists = [123, 'john']
lists[2] = 'LY'
print(lists)
print(lists[0])
print(lists[1:3])        # 输出第二个至第三个元素
print(lists[2:])
print(tinyLists * 2)     # 输出列表两次
print(tinyLists + lists)     # 组合列表


# 6、Python元组：元组是不允许更新，而列表允许更新
tuples = ('runOob', 786, 2.23, 'john', 70.2)
tinyTuples = (123, 'john')
# 非法：tuples[1] = 'LY'
print(tuples)
print(tuples[0])
print(tuples[1:3])
print(tuples[2:])
print(tinyTuples * 2)         # 输出元组两次
print(tinyTuples + tuples)    # 组合元组

# 7、Python字典
dicts = {'one': "This is one", 2: "This is two"}
dicts[3.00] = "This is three"
tinyDicts = {'name': 'runoob', 'code': 6734, 'dept': 'sales'}
print(dicts[3.00])
print(tinyDicts)
print(tinyDicts.keys())
print(tinyDicts.values())
print(tinyDicts.items())

# 8、Python数据类型转换
print('###### 将 x 转换为一个整数 ########')
x = '9'
print(int())
print(int(x))
print(int(x, base=10))   # base: 进制数，默认是十进制

y = 666.66
print(int(y))
z = '666'
print(int(z, base=16))
print(int('0xa', base=16))
print(int('10', base=8))

print('###### 将 x 转换到一个浮点数 ########')
print(float())
print(float(112))
print(float(-123.2))
print(float("-66.6"))

# complex() 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数
print('###### 创建一个复数 ########')
print(complex(1, 2))
print(complex(1))
print(complex("1"))
print(complex("1+2j"))

print('###### 将对象 x 转换为字符串 ########')
s = 'RunOOB'
print(str(s))
dicts = {'RunOob': 'RunOob.com', 'google': 'google.com'}
print(str(dicts))

print('###### 将对象x转换为表达式字符串 ########')
string = 'RunOOB'
print(repr(s))
dictOne = {'runOob': 'runOob.com', 'google': 'google.com'}
print(repr(dictOne))

print('###### 用来计算在字符串中的有效Python表达式,并返回一个对象 ########')
x = 7
print(eval('3 * x'))
print(eval('pow(2, 2)'))
print(eval('2 + 2'))
n = 81
print(eval('n + 2'))

print('###### 将序列 s 转换为一个元组 ########')
print(tuple([1, 2, 3, 4, 5]))
print(tuple({1: 2, 3: 4, 5: 6}))
print(tuple((1, 2, 3, 4, 5, 6, 7)))
aList = [123, 'xyz', 'zara', 'abc']
aTuple = tuple(aList)
print("Tuple elements : ", aTuple)

print('###### 将序列 s 转换为一个列表 ########')
aTuple = (123, 'runoob', 'google', 'abc')
aList = list(aTuple)
print("List Element : ", aList)

print('###### 转换为可变集合 ########')
x = set('runOob')
y = set('google')
print(x, y)
print(x & y)
print(x | y)
print(x - y)

print('###### 创建一个字典：d 必须是一个序列 (key,value)元组 ########')
print(dict())
print(dict(a='a', b='b', c='c'))
print(dict(zip(['one', 'two', 'three'], [1, 2, 3])))
print(dict([('one', 1), ('two', 2), ('three', 3)]))

print('###### 转换为不可变集合 ########')
print('###### 转换为不可变集合 ########')
a = frozenset(range(10))
print(a)
b = frozenset('runOob')
print(b)

print('###### 将一个整数转换为一个字符 ########')
print(chr(0x30), chr(0x31), chr(0x61))  # 十六进制
print(chr(48), chr(49), chr(97))        # 十进制

print('###### 将一个字符转换为它的整数值 ########')
print(ord('a'))
print(ord('b'))
print(ord('c'))

print('###### 将一个整数转换为一个十六进制字符串 ########')
print(hex(255))
print(hex(-42))
print(type(hex(12)))

print('###### 将一个整数转换为一个八进制字符串 ########')
print(hex(10))
print(hex(20))
print(hex(15))