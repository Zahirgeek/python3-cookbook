# 怎样在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）？
# 考虑下面的股票名和价格映射字典：
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# 为了对字典值执行计算操作，通常需要使用 zip() 函数先将键和值反转过来。 比如，下面是查找最小和最大股票价格和股票值的代码：
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print(min_price[0])
print(max_price[0])
# 类似的，可以使用 zip() 和 sorted() 函数来排列字典数据
sorted_prices = sorted(zip(prices.values(), prices.keys()))
print(sorted_prices)
# 执行这些计算的时候，需要注意的是 zip() 函数创建的是一个只能访问一次的迭代器
