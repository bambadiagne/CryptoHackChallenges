state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def matrix2bytes(matrix):
    n=len(matrix)
    return "".join(chr(matrix[i][j]) for i in range(n) for j in range(n))

def add_round_key(s, k):
    n=len(k)
    return matrix2bytes([[s[i][j]^k[i][j] for j in range(n)] for i in range(n) ])


print(add_round_key(state, round_key))

