def widthOfBinaryTree(root):
    end = len(root)
    level = 1
    while end > 1:
        end //= 2
        level += 1
    if end == 0:
        width = findwith(root[:-1], level - 1)
        return width
    elif end == 1:
        width = findwidth(root, level)
        return width



def findwidth(root, level):
    last = len(root) - 1
    first = pow(2, level - 1) - 1
    i = last
    while i >= first:
        if root[i] != '':
            return i - first + 1 + nullwidth(root,level)
        else:
            i -= 1


def nullwidth(root,level):
    add = 0
    thelen = len(root)
    for i in range(1, level + 1):
        if i < level:
            for j in range(pow(2, i - 1) - 1, pow(2, i - 1) - 1):
                if root[j] == 'null':

                    add += pow(2,level-i)
        elif i == level:  # 最后一行，可能不满
            for j in range(pow(2, i - 1) - 1, thelen):
                pass



if __name__ == "__main__":
    root = [1,3,2,5,'null','null',9,6,'null',7]
    result = widthOfBinaryTree(root)
    print(result)