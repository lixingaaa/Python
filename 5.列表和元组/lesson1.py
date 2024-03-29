"""
序列
序列是一块用于存放多个值的连续存储空间，并且按一定顺序排列，每一个值(元素)都分配一个数字，称为索引或位置，通过该索引取出相应的值。
在Python中，序列结构主要有列表，元组，集合，字典和字符串。
"""

"""
索引
序列中每一个元素都有一个编号，也称为索引，索引从0递增，0表示第一个元素
python中的索引可以是负数，这个索引从右向左计数，最后一个元素的索引是-1
通过索引可以访问序列中的任何元素
"""
verse = ["马刺", "湖人", "火箭", "勇士"]
print(verse[0])
print(verse[-1])

"""
切片
切片是访问序列中元素的另一种方法，它可以访问一定访问内的元素，通过切片操作可以生成一个新的序列
语法： sname[start: end : step]
    * sname 表示序列的名称
    * start 表示切片开始的位置包括该位置，如果不指定，默认为0
    * end   表示切片截止的位置，不包括该位置，如果不指定默认为序列的长度
    * step  表示切片的步长，如果省略默认为1，当省略该步长时，最后一个冒号也可以省略
在进行切片操作时，如果指定了步长，那么将按照步长遍历序列的元素，否则一个个遍历
"""
nba = ['迈克尔乔丹', '比尔拉塞尔', '卡里姆阿卜杜勒贾巴尔', '威尔特张伯伦', '艾尔文约翰逊', '科比布莱恩特', '蒂姆邓肯', '勒布朗詹姆斯', '拉里伯德', '沙奎尔奥尼尔']
print(nba[1:5])
print(nba[0:5:2])
print(nba[1:10:2])

"""
序列相加
在python中，支持两种相同类型的序列相加操作，即将两个序列进行连接，使用(+)运算符实现
在进行序列相加是,相同的序列是指，同为列表，元组或集合等，序列中的元素类型可不同
"""
nba1 = ["史提芬库里", "克莱汤普森", "马努吉诺比利", "凯文杜兰特"]
nba2 = ['迈克尔乔丹', '比尔拉塞尔', '卡里姆阿卜杜勒贾巴尔', '威尔特张伯伦', '艾尔文约翰逊', '科比布莱恩特', '蒂姆邓肯', '勒布朗詹姆斯', '拉里伯德', '沙奎尔奥尼尔']
print(nba1+nba2)
# 序列内不同类型
num = [7, 14, 21, 25, 79]
nba3 = ["史提芬库里", "克莱汤普森", "马努吉诺比利", "凯文杜兰特"]
print(num+nba3)
# 不能是列表和元组或者列表和字符串
# print(num + "python")

"""
乘法
在python中，使用数字m乘以一个序列会生成新的序列,新序列的内容为原来序列被重复n次的结果
"""
phone = ['华为mate 10', 'Vivo X21']
print(phone * 3)
# 在序列的乘法运算时，还可以实现初始化指定长度列表的功能
emptylist = [None]*5
print(emptylist)

"""
检查某个元素是否是序列的成员(元素)
在python中，可以使用in关键字检查某个元素是否是序列的成员，即检查某个元素是否包含在序列中
语法: value in sequence
    * value 要检查的元素
    * sequence 表示指定的序列 
"""
nba4 = ["史提芬库里", "克莱汤普森", "马努吉诺比利", "凯文杜兰特"]
print("凯文杜兰特" in nba4)
# 使用 not in 关键字检查不包含在指定的序列中
print("比尔拉塞尔" not in nba4)

"""
计算序列的长度,最大值和最小值
"""
number = [7, 3, 2, 9, 6]
# 计算序列的长度
print(len(number))
# 最大值
print(max(number))
# 最小值
print(min(number))
# 计算元素和
print(sum(number))
# 对元素进行排序
print(sorted(number))
# 反向序列中的元素
print(reversed(number))


"""
其他内置函数
list()     将序列转化为列表
str()      将序列转化为字符串
sum()      计算元素和
sorted()   对元素进行排序
reversed() 反向序列中的元素
enumerate()  将序列组合为一个索引序列,多用在for循环
"""