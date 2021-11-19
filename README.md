# Elevator Algorithm Offilne: 
# Algorithm offline:
 an offline algorithm is given the whole problem data from the beginning and is required to output an answer which solves the problem at hand.
# Algorthim online:
An online algorithm is one that can process its input piece-by-piece in a serial fashion, i.e., in the order that the input is fed to the algorithm, without having the entire input available from the beginning.
# My algorithm:
is working with algorithm offline that is the algorithm have all the data form the beginnig.
my algorithm have four class:

1)class Building:this class for read from the file.json and input to Variables,the file.json have all the information about the elevator in the building and the max floor in the bulid and the min floor.
```python
 def __init__(self,FileName):
    with open(FileName, "r") as fp:
        data = json.load(fp)
         self.minFloor = int(data["_minFloor"])
         self.maxFloor = int(data["_maxFloor"])
         self.elevators = [Elevator(i) for i in data["_elevators"]]
```        
2)class Elevator:this class to input the information about every elevator in his variables and have function calculate the time to know which elevator coming faster and function calculate How long does the elevator take to get there
The variables:
```python
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
```
this the important functions:

function one:
```python
    def Culc_Time(self, pos, dest):
        if pos == dest:
            TimeQuick=self.stopTime + self.openTime
            return TimeQuick
        else:
            Time = self.startTime + self.stopTime + self.openTime + self.closeTime
            return (abs(dest - pos)) / self.speed + Time
```
function two:
```python
    def howMushTime(self, call):
        currPos = self.position
        time = 0
        for c in self.CallisHave:
            time += self.Culc_Time(currPos, c.src)
            currPos = c.src
        if not self.CallisHave.__len__() == 0:
            time += self.Culc_Time(currPos, self.CallisHave[-1].dest)
            currPos = self.CallisHave[-1].dest
        time += self.Culc_Time(currPos, call.src)
        return time
```



