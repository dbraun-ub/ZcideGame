## In Zombicide, a game map is composed of zones. Each zone can be separated by walls, doors or open path. actors can move through zones. 
## This class is objective is to handle the connexion between zones and how they are connected.

from .zone import Zone

class GameMap:
    def __init__(self, connections={}):
        self.zones = {}
        self.addConnections(connections)

    ## Getters
    def getZone(self, zoneId: int): 
        if zoneId in self.zones:
            return self.zones[zoneId]    
        return None
    
    ## Methods
    def addZone(self, newZone: Zone):
        self.zones[newZone.getId()] = newZone

    def connectZones(self, zone1: Zone, zone2: Zone):
        zone1.addConnection(zone2)
        zone2.addConnection(zone1)

    def connectZonesWithId(self, id1, id2):
        if id1 not in self.zones.keys():
            self.addZone(Zone(id1))

        if id2 not in self.zones.keys():
            self.addZone(Zone(id2))

        self.connectZones(self.zones[id1], self.zones[id2])

    # generate the map from a connection dictionary. 
    def addConnections(self, connections: map):
        for k in connections.keys():
            for c in connections[k]:
                self.connectZonesWithId(k, c)

    # Shortest path from a to b. 
    # Return the distance and each valid solution. 
    # If no valide solution, return distance -1 and empty list.
    def shortestPathZones(self, zone1: Zone, zone2: Zone):
        if (zone1.getId() not in self.zones.keys()) or (zone2.getId() not in self.zones.keys()):
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
    
    def shortestPathZonesPerId(self, zoneId1, zoneId2):
        if (zoneId1 not in self.zones.keys()) or (zoneId2 not in self.zones.keys()):
            return [[]]
        
        return self.shortestPathZones(self.zones[zoneId1], self.zones[zoneId2])

    # A TESTER
    def findZonePerId(self, id):
        # for zone in self.zones:
        #     if zone.id == id:
        #         return zone

        if id in self.zones.keys():
            return self.zones[id]
            
        return None