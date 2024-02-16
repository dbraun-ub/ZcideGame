## In Zombicide, a game map is composed of zones. Each zone can be separated by walls, doors or open path. actors can move through zones. 
## This class is objective is to handle the connexion between zones and how they are connected.

from .zone import Zone

class GameMap:
    def __init__(self, connections={}):
        self.zones = []
        self.addConnections(connections)

    def addZone(self, newZone: Zone):
        self.zones.append(newZone)

    def connectZones(self, zone1: Zone, zone2: Zone):
        zone1.addConnection(zone2)
        zone2.addConnection(zone1)

    def connectZonesWithId(self, id1, id2):
        id1Exists = False
        id2Exists = False
        for z in self.zones:
            if z.id == id1: 
                id1Exists = True
                zone1 = z
            if z.id == id2: 
                id2Exists = True
                zone2 = z
            if id2Exists and id1Exists: 
                break

        if not id1Exists: 
            zone1 = Zone(id1)
            self.addZone(zone1)
        if not id2Exists: 
            zone2 = Zone(id2)
            self.addZone(zone2)

        self.connectZones(zone1, zone2)

    # generate the map from a connection dictionary. 
    def addConnections(self, connections: map):
        for k in connections.keys():
            for c in connections[k]:
                self.connectZonesWithId(k, c)

    # Shortest path from a to b. 
    # Return the distance and each valid solution. 
    # If no valide solution, return distance -1 and empty list.
    def shortestPathZones(self, zone1: Zone, zone2: Zone):
        if (zone1 not in self.zones) or (zone2 not in self.zones):
            return [[]]

        # Distance one between each zone.
        N = len(self.zones)
        visitedZones = [zone1]
        memoPath = [[]]*N
        memoPath[0] = [[zone1]]

        # Loop at most until every zone has been explored. It can be shorter.
        i = 0
        while (zone2 not in visitedZones) and (i < N):
            memoPath[i+1] = []
            for p in memoPath[i]:
                # look for the next destination
                for neighbor in p[-1].connectedZones:
                    if neighbor in p:
                        continue
                    memoPath[i+1] += [p + [neighbor]]
                    visitedZones.append(neighbor)
            i += 1

        outputPath = [validPath for validPath in memoPath[i] if zone2 in validPath]
        return outputPath

