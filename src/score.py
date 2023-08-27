import numpy as np
from src.entropy import encode


def checkSimilarity(username, password):
    str1 = username
    str2 = password

    size_1 = len(str1)
    size_2 = len(str2)
    matrix = np.zeros((size_1 + 1, size_2 + 1))
    for i in range(size_1 + 1):
        for j in range(size_2 + 1):
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                matrix[i][j] = i
            elif str1[i-1] == str2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = 1 + min(matrix[i][j-1],
                                       matrix[i-1][j],
                                       matrix[i-1][j-1])
    return 1 - matrix[size_1][size_2] / max(size_1, size_2)


def TotalProbability(encode, checkSimilarity):
    if (encode > checkSimilarity):
        return (encode - checkSimilarity) * 100
    else:
        return (checkSimilarity - encode) * 100


if __name__ == '__main__':
    TotalProbability()
    checkSimilarity()
