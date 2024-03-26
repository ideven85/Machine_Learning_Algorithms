# airports=["BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN", "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD"]
# routes=[
#   ["DSM", "ORD"],
#   ["ORD", "BGI"],
#   ["BGI", "LGA"],
#   ["SIN", "CDG"],
#   ["CDG", "SIN"],
#   ["CDG", "BUD"],
#   ["DEL", "DOH"],
#   ["DEL", "CDG"],
#   ["TLV", "DEL"],
#   ["EWR", "HND"],
#   ["HND", "ICN"],
#   ["HND", "JFK"],
#   ["ICN", "JFK"],
#   ["JFK", "LGA"],
#   ["EYW", "LHR"],
#   ["LHR", "SFO"],
#   ["SFO", "SAN"],
#   ["SFO", "DSM"],
#   ["SAN", "EYW"]
# ]
# startingAirport="LGA"


class AirPortNode:
    def __init__(self, airPort=None):
        self.airPort = airPort
        self.connections = []
        self.is_Reachable = True
        self.unReachableNodes = []


def airportConnections(airports, routes, startingAirport):

    airPortGraph = {}
    createAirPortGraph(airPortGraph, airports, routes)
    unReachableNodes = getUnReachableConnections(
        airPortGraph, airports, routes, startingAirport
    )
    markUnReachableNodes(airPortGraph, unReachableNodes)
    return minimumConnectionsNeeded(airPortGraph, unReachableNodes)


def createAirPortGraph(airPortGraph, airPorts, routes):
    for airPort in airPorts:
        airPortGraph[airPort] = AirPortNode(airPort)

    for route in routes:
        origin, destination = route
        airPortGraph[origin].connections.append(destination)


def getUnReachableConnections(airPortGraph, airPorts, routes, startingAirport):
    visited = set()
    depthFirstSearchForUnReachableNodes(airPortGraph, visited, startingAirport)
    unReachableNodes = []
    for airPort in airPorts:
        if airPort in visited:
            continue
        airPortNode = airPortGraph[airPort]
        airPortNode.is_Reachable = False
        unReachableNodes.append(airPortNode)
    return unReachableNodes


def depthFirstSearchForUnReachableNodes(airPortGraph, visited, current):
    if current:
        if current in visited:
            return
        visited.add(current)
        connectedAirPorts = airPortGraph[current].connections
        for connection in connectedAirPorts:
            depthFirstSearchForUnReachableNodes(
                airPortGraph=airPortGraph, visited=visited, current=connection
            )


def markUnReachableNodes(airPortGraph, unReachableNodes):

    for unReachableNode in unReachableNodes:
        airPort = unReachableNode.airPort
        unReachableConnections = []
        depthFirstSearchForUnReachabeConnections(
            airPortGraph, airPort, unReachableConnections, {}
        )
        unReachableNode.unReachableNodes = unReachableConnections


def depthFirstSearchForUnReachabeConnections(
    airPortGraph, airPort, unReachableConnections, visited
):
    if airPortGraph[airPort].is_Reachable:
        return
    if airPort in visited:
        return
    visited[airPort] = True
    unReachableConnections.append(airPort)
    # print(unReachableConnections)
    connections = airPortGraph[airPort].connections
    for connection in connections:
        depthFirstSearchForUnReachabeConnections(
            airPortGraph, connection, unReachableConnections, visited
        )


def minimumConnectionsNeeded(airPortGraph, unReachableNodes):
    unReachableNodes.sort(key=lambda x: len(x.unReachableNodes), reverse=True)
    connections = 0
    for unReachableNode in unReachableNodes:
        if unReachableNode.is_Reachable:
            continue
        connections += 1
        for connected in unReachableNode.unReachableNodes:
            airPortGraph[connected].is_Reachable = True
    return connections


if __name__ == "__main__":
    airports = [
        "BGI",
        "CDG",
        "DEL",
        "DOH",
        "DSM",
        "EWR",
        "EYW",
        "HND",
        "ICN",
        "JFK",
        "LGA",
        "LHR",
        "ORD",
        "SAN",
        "SFO",
        "SIN",
        "TLV",
        "BUD",
    ]
    routes = [
        ["DSM", "ORD"],
        ["ORD", "BGI"],
        ["BGI", "LGA"],
        ["SIN", "CDG"],
        ["CDG", "SIN"],
        ["CDG", "BUD"],
        ["DEL", "DOH"],
        ["DEL", "CDG"],
        ["TLV", "DEL"],
        ["EWR", "HND"],
        ["HND", "ICN"],
        ["HND", "JFK"],
        ["ICN", "JFK"],
        ["JFK", "LGA"],
        ["EYW", "LHR"],
        ["LHR", "SFO"],
        ["SFO", "SAN"],
        ["SFO", "DSM"],
        ["SAN", "EYW"],
    ]
    print(airportConnections(airports, routes, "LGA"))
