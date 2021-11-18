import csv
import subprocess
import sys
from Building import Building
from Calls import Calls
def get():
    if len(sys.argv) == 4:
        InFile = {
            "building": sys.argv[1],
            "calls": sys.argv[2],
            "out": sys.argv[3]
        }
    else:
        InFile = {
            "building": "C:\\Users\\HP\\Desktop\\Ex1_input\\Ex1_Buildings\\B5.json",
            "calls": "C:\\Users\\HP\\Desktop\\Ex1_input\\Ex1_Calls\\Calls_a.csv",
            "out": "output.csv"
        }
    return InFile

#this function for read from Csv
def ReadCsvCalls(file_name):
    calls = []
    with open(file_name) as f:
        data = csv.reader(f)
        for i in data:
            if (int(i[2]) < building.minFloor or int(i[2]) > building.maxFloor) and(int(i[3]) < building.minFloor or int(i[3]) > building.maxFloor):
                raise Exception("Error Check The Floor")
            calls.append(Calls(i))
    return calls
#this function to write new csv output
def writeCsvCalls():
    data = []
    for i in calls:
        data.append(i.__dict__.values())
    with open(file["out"], 'w', newline="") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(data)

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



#tester for check
def runTester(building, out):
    subprocess.Popen(["powershell.exe", "java -jar C:\\Users\\HP\\Desktop\\Ex1_input\\Ex1_checker_V1.2_obf.jar 316203405,212187256 "+ building + "  "+ out + "  " + "Test.log"])
if __name__ == "__main__":
    file = get()
    building = Building(file["building"])
    calls = ReadCsvCalls(file["calls"])
    Allocate()
    writeCsvCalls()
    runTester(file["building"],file["out"])
