import timeit

short = 10
long = 1000

csArray = list(range(short))
csArrayLen = len(csArray)
icsArray = [None] * short

clArray = list(range(long))
iclArray = [None] * long


def c_s():
    arr = csArray
    count = 0
    for i in arr:
        count += 1
    # print(count)


def ic_s():
    arr = icsArray
    count = 0
    for i in arr:
        count += 1
    # print(count)


def f_ic_s():
    count = 0
    for i in range(csArrayLen):
        count += 1
    # print(count)


def c_l():
    arr = clArray
    count = 0
    for i in arr:
        count += 1
    # print(count)


def ic_l():
    arr = iclArray
    count = 0
    for i in arr:
        count += 1
    # print(count)


times = 10000
print("連續短陣列", timeit.timeit(lambda: c_s(), number=times))
print("不連續短陣列", timeit.timeit(lambda: ic_s(), number=times))
print("不連續短陣列 使用index", timeit.timeit(lambda: f_ic_s(), number=times))
print("連續長陣列", timeit.timeit(lambda: c_l(), number=times))
print("不連續長陣列", timeit.timeit(lambda: ic_l(), number=times))

# 用for in 走訪[空/不空 list]都差不多快
# 但是如果用range去走，就會比較慢
