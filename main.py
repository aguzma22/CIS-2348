from Item import Item
from Inventory import Inventory

print("Inventory System...")


inv = Inventory()
inv.loadItems('test.csv')
# TODO: if you want to print all inventories here
#       call inv.printByType for each type
inv.printByType("laptop")

print("Iventory loaded. " + str(len(inv.items)))

flag = 1
while (flag > 0):
   print ('Enter 1 to print output.')
   print ('Enter 2 to query inventory.')
   print ('Enter 3 to exit.')
   
   selection = input()

   if selection == "1":
       print('1')
   elif selection == "2":
       print('2')
   else:
        flag = -1


print('flag: ' + str(flag))
  