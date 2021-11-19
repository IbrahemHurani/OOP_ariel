# Elevator Algorithm Offilne: 
# Algorithm offline:
 an offline algorithm is given the whole problem data from the beginning and is required to output an answer which solves the problem at hand.
# Algorthim online:
An online algorithm is one that can process its input piece-by-piece in a serial fashion, i.e., in the order that the input is fed to the algorithm, without having the entire input available from the beginning.
# My algorithm:
is working with algorithm offline that is the algorithm have all the data form the beginnig.
my algorithm have four class:

1)class Building:this class for read from the building.json and input to Variables,the building.json have all the information about the elevator in the building and the max floor in the bulid and the min floor.
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

this the important function in the class Elevator:

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
3)class Calls:this class for reader form calls.csv and input the information in variables.the information about all the calls (requests) for elevator

4)class Ex1:this class is the main in this project because this class check what the best elevator need to come for every call and in this class do the print.

the main funtion:
```python
def Allocate():
    Time = 0
    for c in calls:
        first = building.elevators[0]
        for i in building.elevators:
            i.removed()
            if first.howMushTime(c) > i.howMushTime(c):
                first = i
        first.CallisHave.append(c)
        c.Done = Time + first.howMushTime(c)
        Time = c.time
        c.ChangeAllocate(first, building)
``` 



# Source:
https://www.geeksforgeeks.org/online-algorithm/

https://www.youtube.com/watch?v=FptCbX7fRHw

https://en.wikipedia.org/wiki/Elevator_algorithm


