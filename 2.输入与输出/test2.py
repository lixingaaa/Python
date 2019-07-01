# 输出当前年分别和当前日期时间

# 调用日期模块
import  datetime
# 输出当前年份
print('当前年份: ' + str(datetime.datetime.now().year))
# 输出当前日期
print('当前日期时间: ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))