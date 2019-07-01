# 字符串常用操作

"""
拼接字符串
使用"+"运算符可以完成多个字符串的拼接,"+"运算符可与连接多个字符串并产生一个字符串对象
"""
mot_en = 'Remembrance is a form of metting. Frgetfulness is a form of freedom.'
mot_cn = '记忆是一种相遇。 遗忘是一种自由。'
print(mot_en + "--" + mot_cn)
# 字符串不允许直接与其他类型的数据拼接
str1 = "我今天一共走了"
num = 12098
str2 = "步"
# print(str1 + num + str2) 报错
# 解决方法: 使用str()函数将整数转化为字符串
print(str1 + str(num) + str2)


"""
计算字符串长度, 使用len函数
不同的字符所占的字节不同，在Python中, 数字,英文,小数点,下划线和空格占一个字节
汉字在GBK/GB2312编码占2个字节，在UTF-8/Unicode中一般占3个字节或4个字节
"""
str1 = "人生苦短，我用Python!"
length = len(str1)
# 在默认情况下，通过len()函数计算字符串长度时,不区分英文, 数字和汉字, 所有字符都认为是一个字节
print(length) # 14
# 获取UTF-8编码实际所占字节
length = len(str1.encode())
print(length) # 28
# 获取GBK编码实际所占字节
length = len(str1.encode('gbk'))
print(length) # 21

"""
截取字符串
字符串也属于序列，要截取字符串，可以采用切片方式实现
语法： sname[start: end : step]
参数说明:
    * sname 表示序列的名称
    * start 表示切片开始的位置包括该位置，如果不指定，默认为0
    * end   表示切片截止的位置，不包括该位置，如果不指定默认为序列的长度
    * step  表示切片的步长，如果省略默认为1，当省略该步长时，最后一个冒号也可以省略
字符串的索引同序列一样从0开始，并且每个字节占一个位置
"""
str1 = "人生苦短，我用Python!"
substr1 = str1[1]    # 截取第二个字符
substr2 = str1[5:]   # 从第6个字符截取
substr3 = str1[:5]   # 从左边开始截取5个字符
substr4 = str1[2:5]  # 截取第三到第五个字符
print('原字符串:', str1)
print(substr1 + '\n' + substr2 + '\n' + substr3 + '\n' + substr4)
# 截取字符串时, 若指定的索引不存在，则会抛出 string index out of range 异常
# 解决方案: 使用try...except语句捕获异常
try:
    substr1 = str1[15]
except IndexError:
    print('指定的索引不存在')


"""
分割字符串
分割字符串是把字符串分割为列表, 字符串的split()方法可以实现字符串分割, 就是把一个字符串按照指定的分割符切分为字符串列表
该列表的元素中，不包含分割符.
语法: str.split(sep, maxsplit)
参数说明:
    * str: 表示要分割的字符串
    * sep: 用于指定分割符, 可以包含多个字符, 默认为None, 即所有空字符(包括空格, 换行"\n", 制表符"\t"等)
    * maxsplit: 可选参数, 用于指定分割次数, 如果不指定或者为-1, 则分割次数没有限制否则返回列表元素最多为maxsplit+1
    * 返回值: 分割后的字符串列表
说明: 如果不指定sep参数, 那么也不能指定maxsplit参数
"""
str1 = '明 日 学 院 官 网  >>>  www.mingrisoft.com'
print("原字符串: ", str1)
list1 = str1.split()          # 采用默认分割方式
list2 = str1.split(">>>")     # 采用多个字符进行分割
list3 = str1.split(".")       # 采用"."进行分割
list4 = str1.split(" ", 4)    # 采用空格分割, 并且只分割前4个
print(str(list1) + '\n' + str(list2) + '\n' + str(list3) + '\n' + str(list4))
list5 = str1.split('>')       # 采用">"分割
print(list5)


"""
检索字符串
"""
"""
1.count()方法, 用于检索字符串在另一个字符串中出现的次数, 不存在返回0, 否则返回次数
语法: str.count(sub[, start[, end]])
参数说明:
    * str: 表示原字符串
    * sub: 表示要检索字符串
    * start: 可选参数, 表示检索范围起始位置索引, 不指定从头开始
    * end: 可选参数, 表示检索范围的结束位置索引, 不指定一直检索到结尾
"""
str1 = '@明日科技 @扎克伯格 @雷军'
print('字符串 "', str1, '" 中包括',str1.count('@'), '个@符号')

"""
2.find()方法, 用于检索是否包含指定的子字符串。如果检索的字符窜不存在则返回-1, 否则返回索引
语法: str.find(sub[, start[, end]])
参数说明:
    * str: 表示原字符串
    * sub: 表示要检索字符串
    * start: 可选参数, 表示检索范围起始位置索引, 不指定从头开始
    * end: 可选参数, 表示检索范围的结束位置索引, 不指定一直检索到结尾
说明: Python的字符串对象还提供了rfind方法，与find方法类似, 只是从右边开始查找
"""
str1 = '@明日科技 @扎克伯格 @雷军'
print('字符串 "', str1, '" 中@符号首次出现的索引为:',str1.find('@'))
