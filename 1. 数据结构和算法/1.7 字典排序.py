# 你想创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序。

from collections import OrderedDict

d = OrderedDict()
d["a"] = "123"
d["b"] = "456"
d["c"] = "789"

for k in d:
    print("key: {0}---->value: {1}".format(k, d[k]))
