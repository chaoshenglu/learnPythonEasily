# 'hello world'[a:b]
# 这种写法可截取字符串中一部分

# [a:b]表示截取第a位到第b-1位
# 注意，前包后不包
print('hello world'[2:4])
print('hello world'[1:-1])

# [a:]表示截取第a位到末位
# [:b]表示截取从首位到第b-1位
print('hello world'[1:])
print('hello world'[:-1])

# Python中的字符串有两种索引方式，
# 从左往右以0开始，从右往左以-1开始。
print('hello world'[-2:-1])
print('hello world'[-1])


