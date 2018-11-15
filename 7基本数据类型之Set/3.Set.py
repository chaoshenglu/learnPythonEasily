a = {'北京', '上海'}

# 添加一个元素
a.add('广州')
print(a)

# 将列表中的元素加入Set
a.update(['深圳', '天津'])
print(a)

# 将元祖中的元素加入Set
a.update(('重庆', '南京'))
print(a)

# 将字典中的key加入Set
a.update({'武汉': '湖北省'})
print(a)

# 移除元素
a.remove('武汉')
print(a)

# 更安全地移除元素(即使这个元素并不存在，也不会报错)
a.discard('天津')
print(a)

# 清空集合
a.clear()
print(a)
