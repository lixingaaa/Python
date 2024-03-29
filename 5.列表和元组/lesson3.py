import random

"""
元组
与列表类似，由一系列特定顺序排列的数组组成，但是他是不可变序列
形式上元祖的所有元素都放在一对"()"中,两个相邻元素使用逗号","分隔
内容上可以将整数，实数，字符串，列表，元组等任何内容放到元组中.
通常情况下，元组用于保存程序中不可修改的内容。
"""

# 元组的创建和删除

"""
1.使用赋值运算符直接创建元组
语法： tuplename = (element 1, element 2, element3, ..., element n)
tuplename表示元组的名称 element表示元组的元素，个数没限制，且只要是python支持的数据类型就可以.
注意: 创建列表和元组语法类似，创建列表使用"[]", 创建元组使用"()"
"""
num = (4, 14, 5, 84, 18)
team = ("马刺", "勇士", "火箭", "湖人")
untitle = ('Python', 27, [1, 4, 9], ('人生苦短', "我学Python"))
language = ('Pyhton', "C#", "Java")

# 元组的括号不是必要的，只要将一组值用逗号分隔开，Python就认为它是元组
team = "马刺", "勇士", "火箭", "湖人"
print(team)

# 如果创建的元组只包含一个元素，则需要在定义元组时，在元素后面添加一个","
# 不加逗号则表示定义一个字符串
verse1 = ("世界杯冠军")
print(type(verse1))
# 加逗号表示元组
verse2 = ("世界杯冠军",)
print(type(verse2))


"""
2. 创建空元组
空元组可以应用在为函数传递一个空值或者返回空值时
"""
emptytuple = ()


"""
3. 创建数值元组
在Python中，可以使用tupl()函数直接将range()函数循环出来的结果转换为数值元组
语法: tuple(data)
data表示可以转换为元组的数据, 其类型可以是range对象,字符串,元组或者其他可迭代类型的数据
"""

# 创建一个10～20之间(不包含20)所有偶数的元组
even = tuple(range(10, 20, 2))
print(even)


"""
4.删除元组
对于已经创建的元组，不再使用时，可以使用del语句将其删除
语法: del tuplename
tuplename为要删除的元组名称
del语句在实际开发中不常使用，因为Python自带垃圾回收机制会自动销毁不使用的元组
"""
team = ("西班牙", "德国", "阿根廷", "葡萄牙")
del team


"""
5.修改元组元素
元组是不可变序列，不能对它的单个元素值进行修改，可以对元组进行重新赋值
"""
player = ("梅西", "C罗", "伊涅斯塔")
player = ("梅西", "C罗", "苏亚雷斯")
print(player)
# 可以对元组进行连接组合,进行连接时,连接的内容必须都是元组,连接一个元素的元组时需要在后面加",",否则判定为字符串
player1 = ("梅西", "C罗")
player2 = player1 + ("格列兹曼", "莫德里奇")
print(player2)


"""
6.元组推导式
使用元组推导式可以快速生成一个元组,和列表推导式一样，只是将列表的"[]"替换成"()"
"""
randomnumber = (random.randint(10, 100) for i in range(10))
# 元组推导式生成的结果是一个生成器对象,可以将其转换为元组或列表
print(randomnumber)
# 转换为元组
randomnumber = tuple(randomnumber)
print(randomnumber)


"""
元组与列表的区别
* 列表属于可变序列, 它的元素可以随时修改或者删除, 而元组属于不可变序列，其中的元素不可修改，除非整体替换
* 列表可以使用append(), extend()，insert(), remove()和pop()等方法添加和修改列表元素, 元组没有这几个方法
* 列表可以使用切片访问和修改列表中的元素，元组也支持切片，但只能访问不能修改
* 元组比列表的访问和处理速度快,如果只需要对其元素访问而不进行修改可以使用元组
* 列表不能作为字典的键，而元组可以
"""