# 怎样从一个集合中获得最大或者最小的 N 个元素列表？
import heapq
# 1
# nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# print("The largest number: ", heapq.nlargest(1, nums))
# print("The smallest number: ", heapq.nsmallest(1, nums))

# 2
# portfolio = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# cheap = heapq.nsmallest(1, portfolio, key=lambda p: p["price"])
# expensive = heapq.nlargest(1, portfolio, key=lambda p: p["price"])
#
# for item in cheap:
#     print("Cheap portfolio: ", item["name"])
#
# for item in expensive:
#     print("Expensive portfolio: ", item["name"])

# 3

