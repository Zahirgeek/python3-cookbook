# 如果你的程序包含了大量无法直视的硬编码切片，并且你想清理一下代码。
# 假定你要从一个记录（比如文件或其他类似格式）中的某些固定位置提取字段：
record = '....................100 .......513.25 ..........'
# cost = int(record[20:23]) * float(record[31:37])

# 与其那样写，为什么不想这样命名切片呢：
SHARE = slice(20, 23)
PRICE = slice(31, 37)

cost = int(record[SHARE]) * float(record[PRICE])
print(cost)

print("*"*50)

# 另外，你还可以通过调用切片的 indices(size) 方法将它映射到一个已知大小的序列上。 这个方法返回一个三元组 (start, stop, step) ，所有的值都会被缩小，直到适合这个已知序列的边界为止。 这样，使用的时就不会出现 IndexError 异常。比如：
a = slice(5, 50, 2)
s = "HelloWorld"
# a.indices(len(s))
# print("a = {0}".format(a))
for i in range(*a.indices(len(s))):
    print(s[i])
