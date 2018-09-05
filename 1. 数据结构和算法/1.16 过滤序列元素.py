# 你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列

# 最简单的过滤序列元素的方法就是使用列表推导。比如：
mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# print([n for n in mylist if n > 0])

# 使用列表推导的一个潜在缺陷就是如果输入非常大的时候会产生一个非常大的结果集，占用大量内存。 如果你对内存比较敏感，那么你可以使用生成器表达式迭代产生过滤的元素。比如：
# pos = (n for n in mylist if n > 0)
# for i in pos:
#     print(i, end=" ")

# 有时候，过滤规则比较复杂，不能简单的在列表推导或者生成器表达式中表达出来。 比如，假设过滤的时候需要处理一些异常或者其他复杂情况。这时候你可以将过滤代码放到一个函数中， 然后使用内建的 filter() 函数。示例如下：
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


# def is_int(val):
#     try:
#         num = int(val)
#         return True
#     except ValueError as e:
#         return False
#
#
# res = list(filter(is_int, values))
# print(res)


