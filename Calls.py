import csv
class Calls:
     def __init__(self)->None:
        self.AllTheCalls=[]

     def ReadFrom_Csv(self,FileName)->None:
        with open(FileName,"r+")as f:
            My_dataReader=csv.reader(f)
            for i in My_dataReader:
                call_elevetor=Call(Time=float(i[1]),src=int(i[2]),dst=int(i[3]))
                self.AllTheCalls.append(call_elevetor)

     def Get_AllTheCalls(self):
         return self.AllTheCalls

class Call:
    def __init__(self,Time:float=0,src: int=0,dst:int=0)->None:
        self.Time=Time
        self.src=src
        self.dst=dst
        self.elevetor="Elevetor Call"

    def Get_TimeForElev(self)->float:
        return self.Time

    def Get_SrcForElev(self)->int:
        return self.src

    def Get_DstForElev(self)->int:
        return self.dst

    def __str__(self)->str:
        return f"{self.elevetor},Time:{self.Time},src:{self.src},dst:{self.dst}"

    def __repr__(self)->str:
        return self.__str__()

