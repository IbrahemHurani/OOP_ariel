import json

from Elevetor import Elevetor
class Buliding:
    def __init__(self,maxFloor:int=0,minFloor:int=0):
        self.maxFloor=maxFloor
        self.minFloor=minFloor
        self.Elevetors=[]

    def Read_json(self,FileName)->None:
         try:
            with open(FileName,"r+")as f:
                data_buliding=json.load(f)
                elevetor=[]
                self.maxFloor=data_buliding["_maxFloor"]
                self.minFloor=data_buliding["_minFloor"]
                elev=data_buliding["_elevators"]
                for i in elev:
                    el=Elevetor(id=i["_id"],speed=i["_speed"],minFloor=i["_minFloor"],maxFloor=i["_maxFloor"],closeTime=i["_closeTime"],openTime=i["_openTime"],
                                startTime=i["_startTime"],stopTime=i["_stopTime"])
                    elevetor.append(el)
                    self.Elevetors=elevetor
         except IOError as e:
             print(e)












