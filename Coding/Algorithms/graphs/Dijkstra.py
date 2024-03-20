def dijstrasAlgorithm(start,edges):
    V = len(edges)

    minDistances = [float('inf') for _ in range(V)]
    minDistances[start]=0
    vertices = []
    visited = set()

    while len(visited) != V:
        vertex,minDistance = getVertexWithMinDistance(minDistances,visited)
        if minDistance == float('inf'):
            break
        visited.add(vertex)
        vertices.append(vertex)
        for edge in edges[vertex]:
            destination, distance_to_destination = edge
            if destination in visited:
                continue

            newDistance = minDistance + distance_to_destination
            currentNewDistance = minDistances[destination]
            if newDistance < currentNewDistance:
                minDistances[destination]=newDistance
    print(vertices)
    return list(map(lambda x: -1 if x==float('inf') else x,minDistances))




def getVertexWithMinDistance(distances,visited):
    currentMinDistance = float('inf')
    vertex = None

    for vertexIndex,distance in enumerate(distances):
        if vertexIndex in visited:
            continue
        if distance <=currentMinDistance:
            vertex = vertexIndex
            currentMinDistance = distance
    return vertex,currentMinDistance


if __name__ == '__main__':
    start = 0
    edges = [
        [
            [1, 7]
        ],
        [
            [2, 6],
            [3, 20],
            [4, 3]
        ],
        [
            [3, 14]
        ],
        [
            [4, 2]
        ],
        [],
        []
    ]
    print(dijstrasAlgorithm(start,edges))