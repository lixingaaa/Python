# QQ运动周报
# 第一题
thisweek = [4235, 10111, 8447, 9566, 9788, 8951, 9808]
print("本周运动步数: ", thisweek)

# 第二题
lastweek = [3211, 5612, 8123, 11294, 9312, 9973, 3812]
print("上周运动步数: ", lastweek)

# 第三题
sumweek = []
# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
for a,b in zip(thisweek, lastweek):
    sum = a + b
    sumweek.append(sum)
print("汇总结果: ", sumweek)
sumweek.sort()
print("升序: ", sumweek)
sumweek.sort(reverse=True)
print("降序: ", sumweek)

# 第四题
day = ["周日", "周一", "周二", "周三", "周四", "周五", "周六"]
print("星期列表: ", day)

# 第五题
maxStep = thisweek.index(max(thisweek))
minStep = thisweek.index(min(thisweek))
day.insert(maxStep+1, max(thisweek))
day.insert(minStep+1, min(thisweek))
print("本周最大步数和最小步数: ", day)

# 第六题
weekday = ["周日", "周一", "周二", "周三", "周四", "周五", "周六"]
thislist1 = []
thislist2 = []
for item in thisweek:
    if item > 8000:
        thislist1.append(item)
        i = thisweek.index(item)
        thislist2.append(weekday[i])
print("本周高于8000步数值: ", thislist1)
print("本周高于8000步日期: ", thislist2)