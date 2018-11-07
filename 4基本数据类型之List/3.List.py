# 如何用列表表示小强的姓名，年龄，身高，体重？
xiaoQiang = ['小强', 9, 120, 40.3]
print(xiaoQiang)

# 如何将小强的年龄改成10岁？
xiaoQiang[1] = 10
print(xiaoQiang)

# 如何将小强的性别（男），爱好（打球）补充到列表中？
xiaoQiang = xiaoQiang + ['男', '打球']
print(xiaoQiang)

# 如何将小强的身高和体重抽出来，单独成为一个列表？
height_weight = xiaoQiang[2:4]
print(height_weight)

# 如何从列表中删除小强的身高和体重这两个数据？
xiaoQiang.remove(120)
xiaoQiang.remove(40.3)
print(xiaoQiang)

# 如何清空这个列表？
xiaoQiang.clear()
print(xiaoQiang)



