## Elevator Algorithm Offilne: 
![102921667-bf2bdb80-445a-11eb-8eb2-2e6bbdf9beff](https://user-images.githubusercontent.com/86603326/142636372-d7367604-5a9c-4f01-88bc-24d4bf77de60.png)

 an introduction-->[elevator](https://en.wikipedia.org/wiki/Elevator_algorithm)
## Algorithm offline:
 an offline algorithm is given the whole problem data from the beginning and is required to output an answer which solves the problem at hand.
## Algorthim online:
An online algorithm is one that can process its input piece-by-piece in a serial fashion, i.e., in the order that the input is fed to the algorithm, without having the entire input available from the beginning.
## My algorithm:
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
#ResultTest:
|file.json|file.csv|uncomoleted|average waiting time per call|
|---------|--------|-----------|-----------------------------|
|B1.json  |Call_a  |     0     |           112.92            |
|B2.json  |Call_a  |     0     |           50.02             |
|B3.json  |Call_b  |     132   |           543.0             |
|B3.json  |Call_c  |    126    |           561.28            |
|B3.json  |Call_d  |    110    |           528.93            |
|B4.json  |Call_b  |    23     |           211.90            |
|B4.json  |Call_c  |     2     |           206.36            |
|B4.json  |Call_d  |     0     |           199.36            |
|B5.json  |Call_a  |     0     |           14.39             |
|B5.json  |Call_b  |     0     |           39.06             |
|B5.json  |Call_c  |     0     |           41.86             |
|B5.json  |Call_d  |     0     |            43.55            |


## Diagram:
![WhatsApp Image 2021-11-19 at 17 04 44](https://user-images.githubusercontent.com/86603326/142645539-03aac0f7-98a2-43f1-b808-0b4f4b36ae9f.jpeg)


## Source:
https://www.geeksforgeeks.org/online-algorithm/

https://www.youtube.com/watch?v=FptCbX7fRHw

https://www.youtube.com/watch?v=TDww3MjL-0A
