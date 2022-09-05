

def hanoi(n, a, b, c):
    """
    汉诺塔问题
    :param n:盘子数
    :param a: 柱子a
    :param b: 柱子b
    :param c: 柱子c
    :return: 移动次数
    """
    if n > 0:
        hanoi(n-1, a, c, b)
        print(f'将第{n}个盘子从{a}移到{c}')
        hanoi(n-1, b, a, c)


if __name__ == "__main__":
    hanoi(3,'A','B','C')