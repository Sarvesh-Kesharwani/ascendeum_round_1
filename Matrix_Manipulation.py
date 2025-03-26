import numpy as np

def mat(n):
    matrix = np.zeros((n, n), dtype=int)
    count = 1
    top, left = 0,0
    bottom, right = n-1, n-1

    while top <= bottom and left <= right:
        # fill tp row
        for i in range(left, right+1):
            matrix[top, i] = count
            count += 1
        top += 1

        # fill rt column
        for i in range(top, bottom+1):
            matrix[i, right] = count
            count += 1
        right -= 1

        # ill btm row
        if top <= bottom:
            for i in range(right, left-1, -1):
                matrix[bottom, i] = count
                count += 1
            bottom -= 1

        # filling left column
        if left <= right:
            for i in range(bottom, top-1, -1):
                matrix[i, left] = count
                count += 1
            left += 1

    return matrix

mat(6)
