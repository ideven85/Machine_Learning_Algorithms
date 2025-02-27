from collections import deque


def topologicalSort(jobs, deps):
    if jobs[0] != 0:
        V = len(jobs) + 1
    else:
        V = len(jobs)
    adj = []
    if jobs[0] != 0:
        in_degree = [0 for _ in range(len(jobs) + 1)]
    else:
        in_degree = [0 for _ in range(len(jobs))]

    adj = [list() for _ in range(V)]

    for e in deps:
        adj[e[1]].append(e[0])
    print(adj)
    visited = 0
    queue = deque()
    for vertex in range(len(in_degree)):
        for x in adj[vertex]:
            in_degree[x] += 1

    for i in range(len(in_degree)):
        if jobs[0] != 0 and i == 0:
            continue

        if in_degree[i] == 0:
            queue.append(i)

    answer = []

    while queue:
        current = queue.popleft()
        answer.append(current)

        visited += 1

        for adjacent in adj[current]:
            in_degree[adjacent] -= 1
            if in_degree[adjacent] == 0:
                queue.append(adjacent)
    answer.reverse()
    return answer if visited == len(jobs) else []


def topologicalSortToCheck(jobs, deps):
    # Write your code here.
    V = len(jobs)
    adj = [list() for _ in range(V + 1)]
    for e in deps:
        adj[e[0]].append(e[1])
    print(adj)
    in_degree = [0 for _ in range(V + 1)]
    for u in range(len(jobs)):
        for x in adj[u]:
            in_degree[x] += 1
    print(in_degree)
    queue = deque()
    for i in range(len(jobs)):
        if in_degree[i] == 0:
            queue.append(i)
            break
    count = 0
    result = []
    while queue:
        current = queue.popleft()
        count += 1
        result.append(current)
        for vertex in adj[current]:
            in_degree[vertex] -= 1
            if in_degree[vertex] == 0:
                queue.append(vertex)
    print(count)
    print(result)
    if count != V:
        return []
    return result


if __name__ == "__main__":
    jobs = [1, 2, 3, 4]
    deps = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
    print(topologicalSort(jobs, deps))
