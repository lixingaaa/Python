# 使用input输入

tip = input('请输入文字: ')

# Python3中，input接收的都被作为字符串读取，使用int接收数值
num = int(input('请输入你的幸运数字: '))

# 使用ord函数将字符的ASCLL码值转换为数字
name = input('请输入字符: ')
print(name + " 的ASCLL码为: ", ord(name))