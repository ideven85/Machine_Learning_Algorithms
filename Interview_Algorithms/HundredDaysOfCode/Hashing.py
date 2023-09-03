def zigzagTraverse(array):
    # Write your code here.
    n = len(array)
    m = len(array[0])
    output = []
    total = 0
    max_total = n+m
    for i in range(n):
        for j in range(m):
            if i+j<=total:
                if i==j:
                    output.append(array[i][j])

                if j>i:
                    output.append(array[j][i])
                else:
                    output.append(array[i][j])




        total+=1
    return output

if __name__ == '__main__':
    matrix = [[1,3,4,10],
              [2,5,9,11],
              [6,8,12,15],
              [7,13,14,16]
              ]
    print(zigzagTraverse(matrix))

