import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from rules import GameMap

# Create simple connections
def simpleCase_writeConnections():
    simpleMap = {0:[1,2], 1:[0,3], 2:[0,3], 3:[1,2]}

    myMap = GameMap()
    myMap.writeConnections(simpleMap)
    assert(myMap.zonesConnections == simpleMap)

    myMap2 = GameMap(simpleMap)
    assert(myMap.zonesConnections == simpleMap)

    print("simpleCase_writeConnections: OK")

# reset the gamemap
def simpleCase_resetConnections():
    myMap = GameMap()
    simpleMap = {0:(1,2), 1:(0,3), 2:(0,3), 3:(1,2)}
    myMap.writeConnections(simpleMap)
    myMap.resetConnections()
    assert(myMap.zonesConnections == {})
    print("simpleCase_resetConnections: OK")

def simpleCase_findPath(trueShortestPath: list, connections: map, startPosition: int, endPosition: int):
    myMap = GameMap(connections)
    shortestPath = myMap.shortestPath(startPosition,endPosition)
    for i in range(len(trueShortestPath)):
        for j in range(len(trueShortestPath[i])):
            assert(shortestPath[i][j] == trueShortestPath[i][j])

    print("simpleCase_findPath: OK")




if __name__ == "__main__":
    simpleCase_writeConnections()
    simpleCase_resetConnections()
    simpleCase_findPath([[0,1]], {0:[1], 1:[0]}, 0, 1)
    simpleCase_findPath([[0,3,4,7]], {0:[1,2,3], 1:[0,3], 2:[0,5], 3:[0,1,4], 4:[3,7], 5:[2,6], 6:[5,7], 7:[4,6]}, 0, 7)
    simpleCase_findPath([[1,2,4,8,7],[1,3,4,8,7]], {0:[1], 1:[0,2,3], 2:[1,4], 3:[1,4], 4:[2,3,8], 5:[6], 6:[5,7], 7:[6,8], 8:[4,7,9], 9:[8]}, 1, 7)