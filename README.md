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
2)class Elevator:this class to input the information about every elevator in his variables
 the variables



