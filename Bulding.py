import json
from Elevator import Elevator
class Building:
    def __init__(self,FileName):
        with open(FileName, "r") as fp:
            data = json.load(fp)
            self.minFloor = int(data["_minFloor"])
            self.maxFloor = int(data["_maxFloor"])
            self.elevators = [Elevator(i) for i in data["_elevators"]]

























