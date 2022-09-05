from random import randrange
from cal_time import  cal_time


# def cal_time(func):
#     def wrapper(*args,**kwargs):
#         start_time = time.time()
#         result = func(*args,**kwargs)
#         end_time = time.time()
#         print(f'{func}的运行时间为：', end_time - start_time)
#         return result
#     return wrapper

@cal_time
def linear_search(li, val):
    """
    线性查找
    时间复杂度 O(n)
    :param li:列表
    :param val: 要查找的值
    :return: 找到则返回下标，未找到则返回None或-1
    """
    for ind, v in enumerate(li):
        if v == val:
            return ind
    else:
        return None


@cal_time
def binary_search(li, val):
    """
    二分查找
    时间复杂度 O(logn)
    :param li:
    :param val:
    :return:
    """
    left, right = 0, len(li) - 1
    while left <= right:  # 保证候选区有值
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        elif li[mid] < val:
            left = mid + 1
    else:
        return None


if __name__ == "__main__":
    li = range(100000000)
    val = randrange(10000000)
    # position1 = linear_search(li, val)
    position2 = binary_search(li, val)
    print(val)
    # print(position1)
    print(position2)