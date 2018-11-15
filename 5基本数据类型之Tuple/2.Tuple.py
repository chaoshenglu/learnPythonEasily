# 如何用元祖来表示全班同学的姓名？
students = ('小明', '小红', '小强')

# 如何获取元祖中第三个同学的姓名？
print(students[2])

# 如何获取元祖中倒数第二个同学的姓名？
print(students[-2])

# 如何获取元祖的第1个到第3个元素？
print(students[0:3])

# 如何获取元祖的第1个到第-3个元素
print(students[0:-2])

# 将这个元祖重复两遍，形成一个新的元祖
students = students * 2  # 方法一
# students = students + students  # 方法二
print(students)





