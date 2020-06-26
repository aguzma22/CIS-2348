# Anthony Guzman        5.19                    CIS2348
def automobile():
    print("Davy's auto shop services")

    print("Oil change -- $35")

    print("Tire rotation -- $19")

    print("Car wash -- $7")

    print("Car wax -- $12\n")


changeOil = 35;

rotationTire = 19;

washCar = 7;

waxCar = 12;

t = 0;

service1 = 0;

service2 = 0;

automobile()

first_ser = input("Select first service:\n")

if (first_ser == "Oil change" or first_ser == "oil change"):

    t = t + changeOil;

    service1 = changeOil;

elif (first_ser == "Tire rotation" or first_ser == "tire rotation"):


    t = t + rotationTire;

    service1 = rotationTire;


elif (first_ser == "Car wash" or first_ser == "car wash"):

    t = t + washCar;

    service1 = washCar;

elif (first_ser == "Car wax" or first_ser == "car wax"):

    t = t + waxCar;

    service1 = waxCar;


elif (first_ser == "-"):

    first_ser = "No service";

    t = t + 0;


secondService = input("Select second service:\n")

if (secondService == "Oil change" or secondService == "oil change"):

    t = t + changeOil;

    service2 = changeOil;

elif (secondService == " Tire rotation" or secondService == " tire rotation"):

    t = t + rotationTire;

    service2 = rotationTire;

elif (secondService == "Car wash" or secondService == "car wash"):


    t = t + washCar;

    service2 = washCar;

elif (secondService == "Car wax" or secondService == "car wax"):

    t = t + waxCar;

    service2 = waxCar;

elif (secondService == "-"):

    secondService = " No service";

    service2 = 0;

    t = t + 0;

print()

print("Davy's auto shop invoice")

print()

if (first_ser == " No service") and (secondService == " No service"):

    print("Service 1:" + first_ser)

    print("Service 2:" + secondService)

    print()


elif (secondService == " No service"):

    print("Service 1: " + first_ser + ", $" + str(service1))

    print("Service 2:" + secondService)

    print()

elif (first_ser == "No service"):

    print("Service 1: " + first_ser)

    print("Service 2: " + secondService + ", $" + str(service2))

    print()

else:

    print("Service 1: " + first_ser + ", $" + str(service1))

    print("Service 2: " + secondService + ", $" + str(service2))

    print()

print("Total: $" + str(t))