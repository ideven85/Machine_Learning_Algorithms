

def twoEdgeConnectedGraph(edges):
    # Write your code here.
    """
    edges=[
  [1],
  [0]
]
    """
    V = len(edges)
    if V == 0:
        return True

    arrivalTimes = [-1 for _ in range(V)]

    if getArrivalTime(edges,0,-1,V,0,arrivalTimes) == -1:
        return False
    print(arrivalTimes)
    if -1 in arrivalTimes:
        return False
    return True

def getArrivalTime(edges,start,parent,vertices,arrivalTime,arrivalTimes):

    arrivalTimes[start]=arrivalTime
    minArrivalTime=arrivalTime
    for destination in edges[start]:

        if arrivalTimes[destination]==-1:
            minArrivalTime = min(minArrivalTime,getArrivalTime(edges,destination,start,vertices,arrivalTime+1,arrivalTimes))
        elif destination!=parent:
            minArrivalTime = min(minArrivalTime,arrivalTimes[destination])

    print(arrivalTimes,minArrivalTime)

    if minArrivalTime == arrivalTime and parent!=-1:
        return -1
    return minArrivalTime

# Todo
def twoColorableV2(edges):
    colors = [None for _ in edges]
    colors[0]=True
    stack = [0]

    while len(stack):
        current = stack.pop()
        if edges[current]:
            for connection in edges[current]:
                if colors[connection] is None:
                    colors[connection]=not colors[current]
                    stack.append(connection)
                elif colors[connection]==colors[current]:
                    return False
        else:
            #print(colors)
            return False
    print(colors)
    return False if None in colors else True



if __name__ == '__main__':
    edges =[[1],[],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
    graph = [[3],[2],[1,3],[0,2]]
    g = [[4],[],[4],[4],[0,2,3]]
    print(twoEdgeConnectedGraph(edges))
    print(twoColorableV2(edges))
    print(twoColorableV2(graph))
    print(twoEdgeConnectedGraph(graph))
    print(twoEdgeConnectedGraph(g))
    print(twoColorableV2(g))

