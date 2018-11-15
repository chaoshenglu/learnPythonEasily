a = {'张三': 82, '李四': 84, '王五': 56}

# 如何遍历班上所有学生的成绩？
# 方法一：
for student in a.keys():
    score = a[student]
    print(student + ':' + '%d' % score)

# 方法二：
for student, score in a.items():
    print(student + ':' + '%d' % score)

# 如何获取分数不及格的学生？
for student in a.keys():
    score = a[student]
    if score < 60:
        print('不及格的学生：%s' % student)

# 如何计算班上学生的平均分数？
scores = a.values()  # 将所有分数提取为一个列表
num = len(scores)  # 获取列表元素的个数
total = 0.0  # 定义一个浮点数，用来存储所有人的总分数
for score in scores:
    total = total + score  # 依次加上每个人的分数
average = total/num  # 总分数除以人数，得到平均分
print('平均分：%.2f' % average)



