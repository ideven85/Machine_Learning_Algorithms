from collections import defaultdict


def graph(data):
    adj = defaultdict(list)
    for i in range(len(data)):
        for j in range(len(data[i])):
            adj[i + 1].append(adj[i][j])
    return adj


def main():
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(graph(isConnected))
