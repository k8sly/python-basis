from sys import argv, path  # 导入特定的成员
print()
print('================python from import===================================')
for i in argv:
    print (i)
print()
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path