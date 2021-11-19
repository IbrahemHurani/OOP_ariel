
class Calls:
    def __init__(self, data):
        self.name = data[0]
        self.time = float(data[1])
        self.src = int(data[2])
        self.dest = int(data[3])
        self.state = int(data[4])
        self.AllocateToChange = int(data[5])
        self.Done=0

    #this function for know the call which elevator is coming
    def ChangeAllocate(self, elevator, building):
        for elev in building.elevators:
            if elevator.id == elev.id:
                break
        self.AllocateToChange = elevator.id
