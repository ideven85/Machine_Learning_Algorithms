from typing import List

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


def airportConnections(airports, routes, startingAirport):
    # Write your code here.
    airportGraph = createAirPortGraph(airports, routes)
    unReachableAirPortNodes = getUnReachableAirPortNodes(
        airportGraph, airports, startingAirport
    )
    markUnReachableConnections(airportGraph, unReachableAirPortNodes)
    return getMinimumConnections(airportGraph, unReachableAirPortNodes)


def createAirPortGraph(airports, routes):
    airportGraph = {}
    for e in airports:
        airportGraph[e] = AirPortNode(e)
    for route in routes:
        origin, destination = route
        airportGraph[origin].connections.append(destination)
    return airportGraph


def getUnReachableAirPortNodes(airPortGraph, airPorts, startingAirPort):
    visitedAirPorts = {}
    depthFirstSearch(airPortGraph, startingAirPort, visitedAirPorts)
    unReachableAirPortNodes = []
    for airPort in airPorts:
        if airPort in visitedAirPorts:
            continue
        airPortNode = airPortGraph[airPort]
        airPortNode.isReachable = False
        unReachableAirPortNodes.append(airPortNode)
    return unReachableAirPortNodes


def depthFirstSearch(airPortGraph, startingAirPort, visitedAirPort):
    if startingAirPort:
        if startingAirPort in visitedAirPort:
            return
        visitedAirPort[startingAirPort] = True
        connections = airPortGraph[startingAirPort].connections
        for connection in connections:
            depthFirstSearch(airPortGraph, connection, visitedAirPort)


def markUnReachableConnections(airPortGraph, unReachableAirPortNodes):
    for airPortNode in unReachableAirPortNodes:
        airPort = airPortNode.airport
        unReachableConnections = []
        depthFirstSearchUnReachableConnections(
            airPortGraph, airPort, unReachableConnections, {}
        )
        airPortNode.unReachableAirPorts = unReachableConnections


def depthFirstSearchUnReachableConnections(
    airPortGraph, airPort, unReachableConnections, visitedAirPorts
):
    if airPortGraph[airPort].isReachable:
        return
    if airPort in visitedAirPorts:
        return
    visitedAirPorts[airPort] = True
    unReachableConnections.append(airPort)
    connections = airPortGraph[airPort].connections
    for connection in connections:
        depthFirstSearchUnReachableConnections(
            airPortGraph, connection, unReachableConnections, visitedAirPorts
        )


def getMinimumConnections(airportGraph, unReachableAirPortNodes):
    unReachableAirPortNodes.sort(
        key=lambda airPort: len(airPort.unReachableAirPorts), reverse=True
    )
    numberOfNewConnections = 0
    for airPortNode in unReachableAirPortNodes:
        if airPortNode.isReachable:
            continue
        numberOfNewConnections += 1
        for connection in airPortNode.unReachableAirPorts:
            airportGraph[connection].isReachable = True
    return numberOfNewConnections


class AirPortNode:
    def __init__(self, airport):
        self.airport = airport
        self.connections = []
        self.isReachable = True
        self.unReachableAirPorts = []


def findItinerary(tickets: List[List[str]]) -> List[str]:
    pass


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
