# 下面展示两个集合间的运算

a = {'北京', '上海', '天津'}
b = {'北京', '深圳', '广州'}

print(a - b)  # 找出a集合有，b集合没有的元素
print(a | b)  # 找出a集合有，或者b集合有的元素
print(a & b)  # 找出a集合和b集合共同拥有的元素
print(a ^ b)  # 找出a集合独有和b集合独有的元素

