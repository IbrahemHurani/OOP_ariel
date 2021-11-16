import json

class Elevetor:
    def __init__(self,id: int = 0, speed: float = 0, minFloor:int = 0, maxFloor: int = 0, closeTime: float = 0,openTime: float = 0, startTime: float = 0,stopTime: float = 0)->None:
        self.id = id
        self.speed = speed
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.closeTime = closeTime
        self.openTime = openTime
        self.startTime = startTime
        self.stopTime = stopTime
        self.curr=0


    def __str__(self)->str:
        return f"id:{self.id},speed:{self.speed},minFloor:{self.minFloor},maxFloor:{self.maxFloor},closeTime:{self.closeTime},openTime:{self.openTime}" \
               f",startTime:{self.startTime},stopTime:{self.stopTime}"
    def __repr__(self)->str:
         return self.__str__()

