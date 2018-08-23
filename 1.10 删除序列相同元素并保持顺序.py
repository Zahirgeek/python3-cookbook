# 怎样在一个序列上面保持元素顺序的同时消除重复的值？
# 如果序列上的值都是 hashable 类型，那么可以很简单的利用集合或者生成器来解决这个问题。比如：


def dedupe(items):
    set_tmp = set()
    for item in items:
        if item not in set_tmp:
            yield item
            set_tmp.add(item)


li = [1, 2, 3, 4, 5, 1, 2, 6, 7]
print(list(dedupe(li)))
