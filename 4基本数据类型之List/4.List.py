cities = ['北京', '上海', '深圳', '广州']

# 访问数组的第1个元素
print("cities[0]: ", cities[0])

# 访问数组的第1个到第3个元素
print("cities[0:3]: ", cities[0:3])

# 访问数组的第1个到第-3个元素
print("cities[0:-2]: ", cities[0:-2])

# 将这个数组重复两遍，形成一个新的数组
cities = cities * 2
print(cities)

# 遍历这个数组
for city in cities:
    print(city)
