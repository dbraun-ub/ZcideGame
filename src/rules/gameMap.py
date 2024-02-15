## In Zombicide, a game map is composed of zones. Each zone can be separated by walls, doors or open path. actors can move through zones. 
## This class is objective is to handle the connexion between zones and how they are connected.

class GameMap:
    def __init__(self, connections={}):
        self.zonesConnections = connections

    def writeConnections(self, connections):
        # It will erase previous connections
        for key in connections.keys():
            self.zonesConnections[key] = connections[key]

    def resetConnections(self):
        self.zonesConnections = {}

    # Shortest path from a to b. 
    # Return the distance and each valid solution. 
    # If no valide solution, return distance -1 and empty list.
    def shortestPath(self, a: int, b: int):
        if (a not in self.zonesConnections) or (b not in self.zonesConnections):
            return [[]]

        # Distance one between each zone.
        N = len(self.zonesConnections)
        visitedZones = [a]
        memoPath = [[]]*N
        memoPath[0] = [[a]]

        # Loop at most until every zone has been explored. It can be shorter.
        i = 0
        while (b not in visitedZones) and (i < N):
            memoPath[i+1] = []
            for p in memoPath[i]:
                # look for the next destination
                for neighbor in self.zonesConnections[p[-1]]:
                    if neighbor in p:
                        continue
                    memoPath[i+1] += [p + [neighbor]]
                    visitedZones.append(neighbor)
            i += 1

            
        outputPath = [validPath for validPath in memoPath[i] if b in validPath]
        return outputPath


