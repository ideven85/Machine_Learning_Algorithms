def removeIslands(matrix):
    # Write your code here.
    onesConnectedToBorder = [[False for col in row] for row in matrix]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            rowIsBorder = row == 0 or row == len(matrix)-1
            colIsBorder = col == 0 or col == len(matrix[row])-1
            isBorder = rowIsBorder or colIsBorder
            if isBorder:
                if matrix[row][col]==1:
                    getOnesConnectedToBorder(matrix,row,col,onesConnectedToBorder)
    for row in range(1,len(matrix)-1):
        for col in range(1,len(matrix[row])-1):
            if onesConnectedToBorder[row][col]:
                continue
            matrix[row][col]=0
    return matrix


def getOnesConnectedToBorder(matrix,startRow,startCol,onesConnectedToBorder):
    stack = [(startRow,startCol)]
    while len(stack):
        current = stack.pop()
        currRow,currCol = current
        if onesConnectedToBorder[currRow][currCol]:
            continue
        onesConnectedToBorder[currRow][currCol]=True
        adjacentNodes = getAdjacentNodes(matrix,currRow,currCol)
        for adj in adjacentNodes:
            row,col=adj
            if matrix[row][col]==1:
                stack.append((row,col))



def getAdjacentNodes(matrix,row,col):
    adjacents = []
    rows = len(matrix)
    cols = len(matrix[row])
    if row+1<rows:
        adjacents.append((row+1,col))
    if row-1>=0:
        adjacents.append((row-1,col))
    if col+1<cols:
        adjacents.append((row,col+1))
    if col-1>=0:
        adjacents.append((row,col-1))
    return adjacents


if __name__ == '__main__':
    m = [
  [1, 0, 0, 0, 0, 0],
  [0, 1, 0, 1, 1, 1],
  [0, 0, 1, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 1, 1, 0, 0],
  [1, 0, 0, 0, 0, 1]
]
    print(removeIslands(m))