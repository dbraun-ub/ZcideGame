import actorTests
import gameMapTests
import zoneTests

if __name__ == "__main__":
    print("Test class GameMap:")
    gameMapTests.main()
    print("---")
    print("Test class Zone:")
    zoneTests.main()
    print("---")
    print("Test class Actor:")
    actorTests.main()
    print("---")
    print("All tests completed successfully!")