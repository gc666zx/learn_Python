def transpose(matrix):
    a = len(matrix)
    b = len(matrix[0])
    turn = []
    for i in range(b):
        turn.append([])
        for j in range(a):
            turn[i].append(matrix[j][i])
    return turn


if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6]]
    result = transpose(matrix)
    print(result)