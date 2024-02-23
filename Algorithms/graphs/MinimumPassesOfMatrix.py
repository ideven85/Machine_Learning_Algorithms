def minimumPassesOfMatrix(matrix):
    # Write your code here.
    passes = getMinimumPasses(matrix)
    print(matrix)
    return passes-1 if notContainsNegative(matrix) else -1

def getMinimumPasses(matrix):
    nextPassQueue = getAllPositives(matrix)

    passes = 0

    while len(nextPassQueue)>0:
        currentPassQueue = nextPassQueue
        nextPassQueue = []

        while len(currentPassQueue)>0:
            curRow,curCol = currentPassQueue.pop(0)
            adjacentPositions = getAdjacent(matrix,curRow,curCol)
            for p in adjacentPositions:
                row,col=p
                if matrix[row][col]<0:
                    matrix[row][col]*=-1
                    nextPassQueue.append([row,col])
        passes+=1
    return passes

def getAllPositives(matrix):
    positives = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col]>0:
                positives.append([row,col])
    return positives

def notContainsNegative(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col]<0:
                return False
    return True

def getAdjacent(matrix,row,col):
    adjacents = []
    m = len(matrix)
    n = len(matrix[row])
    if row+1<m :
        adjacents.append([row+1,col])
    if row>0:
        adjacents.append([row-1,col])
    if col+1<n :
        adjacents.append([row,col+1])
    if col>0 :
        adjacents.append([row,col-1])
    return adjacents


if __name__ == '__main__':
    m = [[1, 0, 0, -2, -3],
         [-4, -5, -6, -2, -1],
         [0, 0, 0, 0, -1],
         [1, 2, 3, 0, -2]]
    m1 = [[0]]
    print("Min passes:", minimumPassesOfMatrix(m))
    print("M1", minimumPassesOfMatrix(m1))