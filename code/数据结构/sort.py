"""
Low B 三人组：冒泡排序、选择排序、插入排序
NB三人组：快速排序、堆排序、归并排序
其他：希尔排序、计数排序、基数排序
"""
import random
import sys
import time
import copy
from cal_time import  cal_time
sys.setrecursionlimit(1000000)

@cal_time
def bubble_sort(li):
    """
    冒泡排序
    时间复杂度，O(n2）
    :param li:输入的列表
    :return:
    """
    for i in range(0, len(li) - 1):  # 第i趟排序，总趟数为i-1    搞清楚边界条件
        for j in range(0, len(li)-i-1):  # 每一趟排序，箭头的终点为倒数第二个，即len(li)-i-1
            exchange = False  # 小优化，对是否排好序的记录，排好序 则 exchange为 True，不再继续冒泡
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        if not exchange:
            return

@cal_time
def select_sort(li):
    """
    选择排序，冒泡排序的优化，减小了交换次数
    时间复杂度不变，空间复杂度降低
    :param li:
    :return:
    """
    for i in range(len(li)-1):  # 第i趟排序
        min_pos = i  # 记录最小值所在位置坐标
        for j in range(i+1,len(li)):
            if li[j] < li[min_pos]:
                min_pos = j
        if min_pos != i:
            li[i], li[min_pos] = li[min_pos], li[i]

@cal_time
def insert_sort(li):
    """
    插入排序
    时间复杂度，O(n2）
    :param li:
    :return:
    """
    for i in range(1, len(li)):  # 摸取第i张牌
        j = i - 1  # 手里的最后一张牌
        tem = li[i]  # 摸取的牌（待排序）
        while tem < li[j] and j >= 0:
            li[j+1] = li[j]  # 手中的牌向右移，腾出空格
            j -= 1
        li[j+1] = tem  # 把摸到的牌插下去


def _quick_sort(data, left, right):
    """
    快速排序
    :param data:
    :param left:
    :param right:
    :return:
    """
    if left < right:
        mid = partition(data, left, right)
        _quick_sort(data, left, mid-1)
        _quick_sort(data, mid+1, right)


def partition(data, left, right):
    tem = data[left]  # 将比对值取出来
    while left < right:
        while left < right and li[right] >= tem:  # 从右边比对，大于tem则过，直至比对结束或找到比tem小的数
            right -=1  # 往左走一步
        li[left] = li[right]  # 将右边较小的值写在左边空位上
        while left < right and li[left] <= tem:  # 从左边开始对比
            left += 1  # 往右走一步
        li[right] = li[left]  # 将左边较大的值写在右边空位上
    li[left] = tem  # 将取出去的tem归位
    return left

@cal_time
def quick_sort(li):
    return _quick_sort(li, 0, len(li)-1)


def sift(li, low, high):
    """
    堆排序

    :param li:列表
    :param low: 堆的第一个元素（根节点）
    :param high: 堆的最后一个元素
    :return:
    """




if __name__ == "__main__":
    # li = []
    # for i in range(10):
    #     li.append(randrange(0,100))
    # li = [random.randint(0,10000) for i in range(10)]
    li = list(range(5000))
    random.shuffle(li)
    li1 = copy.deepcopy(li)
    li2 = copy.deepcopy(li)
    li3 = copy.deepcopy(li)
    li4 = copy.deepcopy(li)

    bubble_sort(li1)

    select_sort(li2)

    insert_sort(li3)

    quick_sort(li4)

