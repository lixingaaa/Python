# 根据输入的年份计算年龄大小
import datetime
birth = int(input('请输入年份: '))
print('你的年龄是%d岁' % (datetime.datetime.now().year - birth))