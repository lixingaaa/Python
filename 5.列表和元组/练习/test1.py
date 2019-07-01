# 千年虫问题
year = [89, 98, 00, 75, 68, 37, 59, 90]
for index, value in enumerate(year):
    if str(value) != '0':
        year[index] = int('19' + str(value))
    else:
        year[index] = int('200' + str(value))
year.sort()
print(year)