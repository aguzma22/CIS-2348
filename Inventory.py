import csv
from Item import Item

class Inventory:
    def __init__(self, items=[]):
        self.items=items

    def printByType(self,type):
        fn = type + "Inventory.csv"
        f= open(fn,"w+")
        for i in self.items:
            if i.itemType == type:
                f.write(str(i.itemId) + "," + str(i.manufacturer) + "," + str(i.price) + "," + str(i.serviceDate) + "," + str(i.condition))

    def printInventory(self):
        print('Implement print all logic')

    def printByCondition(self,condition):
        fn = condition + "Inventory.csv"
        f= open(fn,"w+")
        for i in self.items:
            if i.condition == condition:
                f.write(i.itemId + "," + i.manufacturer + "," + i.price + "," + i.serviceDate + "," + i.condition)
     
    def loadItems(self,filename):
        with open(filename,'r') as csvfile:
                csvreader = csv.reader(csvfile)
                counter = 0
                for row in csvreader:
                    self.items.append(Item(row[0],row[2],row[1]))                   

    def queryItems(self,manufacturer,type):
        print('Implement query logic')