import doctest
from collections import defaultdict, deque
from typing import List


# https://leetcode.com/problems/bus-routes/description/ LeetCode Hard
def numBusesToDestination(routes: List[List[int]], source: int, target: int) -> int:
    """
        You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

    For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
    You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target.
     You can travel between bus stops by buses only.

    Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.
        >>> numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6)
        2
        >>> numBusesToDestination(routes = [[7,12],[4,5,15],[6],[15,9],[9,12,13]], source = 4, target = 12)
        3
    """
    num_buses = len(routes)
    if source == target:
        return 0
    paths = 1
    min_paths = 0
    stations_to_buses = defaultdict(list)
    buses_to_stations = defaultdict(set)
    queue = deque()
    for i in range(num_buses):
        for j in range(len(routes[i])):
            if routes[i][j] == source:
                queue.append((i, source))
            stations_to_buses[i].append((i, routes[i][j]))
            # buses_to_stations[routes[i][j]].add(i)
    # print(buses_to_stations)
    visited = {source}

    # print(stations_to_buses)
    while queue:
        current_bus, current_station = queue.pop()
        print(current_bus, current_station)

        if current_station == target:
            return paths
        # for connected_bus,connected_station in stations_to_buses[current_bus]:
        #     if connected_station not in visited:
        #         visited.add(connected_station)
        #         queue.append((connected_bus,connected_station))
        paths += 1

        # for connected_bus,connected_station in stations_to_buses[current_bus]:
        #     if current_station not in visited:
        #         if connected_station == target:
        #             return paths
        #         visited.add(connected_station)
        #         queue.append((connected_bus, connected_station))

        for i in range(num_buses):
            current_bus = queue.popleft()
            for connected_station in stations_to_buses[current_station]:
                pass

    return -1


if __name__ == "__main__":
    print(doctest.testmod(verbose=True))
