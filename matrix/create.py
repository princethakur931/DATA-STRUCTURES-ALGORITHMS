def matrix(row,col):
    res = []
    for i in range(row):
        r = []
        for j in range(col):
            r.append(int(input(f'enter row {i}th col {j}th element: ')))
        res.append(r)
    return res

row = int(input('enter total numbers of rows: '))
col = int(input('enter total numbers of cols: '))
print(matrix(row,col))