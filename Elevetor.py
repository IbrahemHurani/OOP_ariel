from Calls import *

class Elevator:
    def __init__(self, data):
        self.id = int(data["_id"])
        self.speed = float(data["_speed"])
        self.minFloor = int(data["_minFloor"])
        self.maxFloor = int(data["_maxFloor"])
        self.closeTime = float(data["_closeTime"])
        self.openTime = float(data["_openTime"])
        self.startTime = float(data["_startTime"])
        self.stopTime = float(data["_stopTime"])
        self.position=0
        self.CallisHave=[]
    #this function to know how mush Time take the elevtor for coming
    def howMushTime(self, call):
        pos = self.position
        time = 0
        for c in self.CallisHave:
            time += self.Culc_Time(pos, c.src)
            pos = c.src
        if not self.CallisHave.__len__() == 0:
            time += self.Culc_Time(pos, self.CallisHave[-1].dest)
            pos = self.CallisHave[-1].dest
        time += self.Culc_Time(pos, call.src)
        return time

    #this function to calculate the time
    def Culc_Time(self, pos, dest):
        if pos == dest:
            TimeQuick=self.stopTime + self.openTime
            return TimeQuick
        else:
            Time = self.startTime + self.stopTime + self.openTime + self.closeTime
            return (abs(dest - pos)) / self.speed + Time
    #this function Remove all calls is done
    def removed(self,):
        for c in self.CallisHave:
            if 0 > c.Done:
                c.state=0
                self.CallisHave.remove(c)
                self.position = c.dest
