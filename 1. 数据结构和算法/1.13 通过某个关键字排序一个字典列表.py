# 你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表。
# 通过使用 operator 模块的 itemgetter 函数，可以非常容易的排序这样的数据结构。 假设你从数据库中检索出来网站会员信息列表，并且以下列的数据结构返回：
from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

order_fname = sorted(rows, key=itemgetter("fname"))
order_uid = sorted(rows, key=itemgetter("uid"))

print(order_fname)
print(order_uid)

print("*"*50)
# itemgetter() 函数也支持多个 keys，比如下面的代码
rows_by_lfname = sorted(rows, key=itemgetter("fname", "lname"))
print(rows_by_lfname)

# 不要忘了这节中展示的技术也同样适用于 min() 和 max() 等函数
min_by_fname = min(rows, key=itemgetter("fname"))
print("min: ", min_by_fname)
