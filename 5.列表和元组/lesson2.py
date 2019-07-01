import random

# 列表

#列表的创建和删除
"""
1.使用赋值运算符直接创建列表
语法: listname = [element 1, element 2, element 3, ..., element n]
listname 表示列表名称,可以是任何符合python命名规范的标识符
element 表示列表中的元素，个数没有限制，并且只要是python支持的数据类型就可以
"""

# 下列定义都是合法的
num = [7, 14, 3, 28]
verse = ["史提芬库里", "克莱汤普森", "马努吉诺比利", "凯文杜兰特"]
untitle = ['Python', 28, '人生苦短，我用Python', ['爬虫', '自动化运维', '云计算', 'web开发']]

# 2.创建空列表
emptylist = []

"""
3.创建数值列表
语法: list(data)
data表示可以转化为列表的数据，其类型可以是range对象, 字符串，元组或其他可以迭代类型的数据
"""
# 创建一个10~20之间(不包含20)所有偶数列表
list(range(10, 20, 2))  # [10, 12, 14, 16, 18]

"""
4.删除列表
对于已经创建的列表，不再使用时，可以使用del语句删除, del语句实际开发并不常用，Python自带垃圾回收机制自动销毁不使用列表
语法: del listname
"""
team = ["皇马", "罗马", "利物浦", "拜仁"]
del team


# 访问列表元素
untitle = ['Python', 28, '人生苦短，我用Python', ['爬虫', '自动化运维', '云计算', 'web开发']]
# 输出列表
print(untitle)
# 输出指定字符
print(untitle[2])

# 遍历列表
# 1.直接使用for循环实现，只能输出元素的值
# 定义一个保存2018年俄罗斯世界杯四强列表
print('2018年俄罗斯世界杯四强:')
team = ['法国', '比利时', '英格兰', '克罗地亚']
for item in team:
    print(item)

# 2.使用for循环和enmerate()函数实现,可以同时输出索引值和元素内容
print('2018年俄罗斯世界杯四强:')
team = ['法国', '比利时', '英格兰', '克罗地亚']
for index,item in enumerate(team):
    print(index + 1, item)

# 添加、修改和删除列表元素
# 1.append在末尾添加元素
phone = ["摩托罗拉", "诺基亚", "三星", "OPPO"]
len(phone) # 获取列表长度
phone.append("iPhone")
len(phone)
print(phone)
# 将一个列表中的全部元素添加到另一个列表中，使用extend方法实现
phone.extend(['华为', 'Vivo', '荣耀'])
print(phone)

# 2.修改元素
verse = ["德国队小组赛回家", "西班牙传控打法还有未来吗？", "C罗一人抵抗西班牙队"]
print(verse)
verse[2] = "梅西, C罗相约回家"  # 修改列表中的第三个元素
print(verse)

# 3.删除元素
# 根据索引删除
verse = ["德国队小组赛回家", "西班牙传控打法还有未来吗？", "C罗一人抵抗西班牙队"]
del verse[-1]  # 删除列表中最后一个元素
print(verse)
# 根据元素值删除
team = ["火箭", "勇士", "开拓者", "爵士", "鹈鹕", "马刺", "雷霆", "森林狼"]
value = "勇士"
# count方法用于判断指定元素出现的次数，如果为0，表示不存在
if team.count(value)>0:
    team.remove(value)
print(team)

# 对列表进行统计计算
# count,获取指定元素出现的次数
player = ["莫德里奇", "梅西", "C罗", "苏亚雷斯", "内马尔", "格列兹曼", "莫德里奇"]
num = player.count('莫德里奇')
print(num)

# 获取指定元素出现的下标
team = ["西班牙", "阿根廷", "葡萄牙", "德国", "法国", "瑞典", "克罗地亚"]
position = team.index("阿根廷")
print(position)

"""
统计数值列表的元素和
语法: sum(iterable[,start])
iterable要统计的列表, start表示统计结果从那个数开始,可选,默认为0
"""
grade = [98, 99, 97, 100, 95, 96, 91, 92, 93, 95]
total = sum(grade)
print(total)


"""
对列表进行排序
语法: listname.sort(key=None, reverse=False)
listname表示要进行排序的列表, key表示指定一个从每个列表元素中提取一个用于比较的值
reverse 可选参数,如果为True则表示降序排列,反之升序，默认升序排列
"""
grade = [98, 99, 97, 100, 95, 96, 91, 92, 93, 95]
print('愿列表: ', grade)
grade.sort()
print("升 序: ", grade)
grade.sort(reverse=True)
print("降 序: ", grade)

# 对字符串列表排序，不区分大小写
char = ['cat', 'Tom', 'Angela', 'pet']
char.sort()
print("区分字符大小写: ", char)
char.sort(key=str.lower)
print("不区分大小写: ", char)

"""
使用内置的sorted函数实现,使用该函数后,原列表的元素顺序不变
语法：sorted(iterable, key=None, reverse=False)
listname表示要进行排序的列表, key表示指定一个从每个列表元素中提取一个用于比较的值
reverse 可选参数,如果为True则表示降序排列,反之升序，默认升序排列
"""
grade = [98, 99, 97, 100, 95, 96, 91, 92, 93, 95]
grade_as = sorted(grade)
print("升序: ", grade_as)
grade_des = sorted(grade, reverse = True)
print("降序: ", grade_des)
print("原系列: ", grade)

"""
列表推导式
使用列表推导式可以快速生成一个列表，或者根据某个队列生成满足指定需求的列表。
"""

"""
(1)生成指定范围的数值列表, list = [Experssion for var in range]
list表示生成的列表名称, Experssion 表达式，用于计算新列表的元素, var 循环变量, range采用range()函数生成range对象
"""
# 生成一个包括10个随机数的列表, 要求范围在10-100之间
randomnumber = [random.randint(10, 100) for i in range(10)]
print("生成的随机数为: ", randomnumber)

"""
(2)根据列表生成指定需求的列表，newlist = [Experssion for var in list]
newlist表示新生成的列表名称, Experssion 表达式,用于计算新的列表,var变量,值为后面列表的每个元素值，list用于生成新猎豹的原列表
"""
# 定义一个记录商品价格的列表，然后应用列表推导式生成一个将全部商品价格打五折的列表
price = [1200, 5330, 9880, 7680, 8888]
sale = [int(x*0.5) for x in price]
print("原价格: ", price)
print("打五折的价格: ", sale)

"""
(3)从列表中选择符合条件的元素组成新的列表, newlist = [Experssion for var in list if condition]
newlist表示新生成的列表名称, Experssion 表达式,用于计算新的列表, var变量,值为后面列表的每个元素值
list用于生成新列表的原列表, condition条件表达式，用于指定筛选条件
"""
# 定义一个记录商品价格的列表, 然后应用列表推导式生成一个商品价格高于5000的列表
price = [1200, 5330, 9880, 7680, 8888]
sale = [x for x in price if x > 5000]
print("原列表: ", price)
print("价格高于5000的: ", sale)