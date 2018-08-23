#怎样实现一个键对应多个值的字典（也叫 multidict）？
# 一个字典就是一个键对应一个单值的映射。如果你想要一个键映射多个值，
# 那么你就需要将这多个值放到另外的容器中， 比如列表或者集合里面。比如，你可以像下面这样构造这样的字典：
# a = {
#     "a": [1, 2, 3],
#     "b": [3, 4, 5],
#     "c": [7, 8]
# }
#
# b = {
#     "a": {1, 2, 3},
#     "b": {3, 4, 5},
#     "c": {7, 8}
# }
#
# for k in a:
#     print("[a]-->key: {0}     value: {1}".format(k, a[k]))
# print("-"*20)
# for k in b:
#     print("[b]-->key: {0}     value: {1}".format(k, b[k]))

# 你可以很方便的使用 collections 模块中的 defaultdict 来构造这样的字典。 defaultdict 的一个特征是它会自动初始化每个 key 刚开始对应的值，所以你只需要关注添加元素操作了。比如：
# from collections import defaultdict
#
# dict_li = defaultdict(list)
# dict_li["a"].append(1)
# dict_li["a"].append(2)
# dict_li["a"].append(3)
# dict_li["b"].append(4)
# dict_li["b"].append(5)
# dict_li["c"].append(6)
# dict_set = defaultdict(set)
# dict_set["a"].add(1)
# dict_set["a"].add(2)
# dict_set["a"].add(3)
# dict_set["b"].add(4)
# dict_set["b"].add(5)
# dict_set["c"].add(6)
#
# for li in dict_li:
#     print("[dict_li]--->key: {0}    value: {1}".format(li, dict_li[li]))
#
# print("-"*50)
#
# for s in dict_set:
#     print("[dict_set]--->key: {0}   value: {1}".format(s, dict_set[s]))





