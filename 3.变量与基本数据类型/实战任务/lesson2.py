# 十进制转二进制，八进制，十六进制
number = int(input('请输入一个十进制数字: '))
# 十进制转二进制，通过bin转换为二进制,取第二位之后的值
two = bin(number)[2:]
print('二进制:', two)
# 十进制转八进制
eight = oct(number)[2:]
print('八进制:', eight)
# 十进制转十六进制
sixteen = hex(number)[2:]
print('十六进制:', sixteen)