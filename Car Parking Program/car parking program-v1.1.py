#Check card for registered staff and students

RFID = 12345
total_spaces = 100
parked_cars = 0

print (RFID)
print (parked_cars)
cardreader = input("Please swipe your card: ")

print(parked_cars)
if cardreader == RFID:
    print("Access granted. Welcome!")
    parked_cars += parked_cars +1
    print(parked_cars)

#record the number of cars in the parking lot

def count_cars():
    
    print(parked_cars)

    
#display the number of available parking spaces 

#triger an alert if the car park is full