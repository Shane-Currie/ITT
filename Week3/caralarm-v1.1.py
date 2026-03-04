DRIV = []
PASS = []
IGN = []
BELTP = []
BELTD = []
ALARM = []

def main():
    sitindriverseat = input("sit in driver seat [y] [n]: ")
    if sitindriverseat == "n":
        print ("goodbye")
        exit()  
    elif sitindriverseat == "y":
        DRIV.append(1)    
        print("DRIV", DRIV, "PASS", PASS, "IGN", IGN, "BELTP", BELTP, "BELTD", BELTD, "ALARM", ALARM)
    driverfastenseatbelts = input("fasten driver seatbelt [y] [n]: ")
    if driverfastenseatbelts == "n":
        BELTD.append(0)
    elif driverfastenseatbelts == "y":
        BELTD.append(1) 
    passengerseat = input("is there a passenger [y] [n]: ")
    if passengerseat == "n":   
        PASS.append(0)
    elif passengerseat == "y":
        PASS.append(1)              
        passengerfastenseatbelts = input("fasten passenger seatbelt [y] [n]: ")   
        if passengerfastenseatbelts == "n":
            BELTP.append(0)
        elif passengerfastenseatbelts == "y":
            BELTP.append(1)
            print("DRIV", DRIV, "PASS", PASS, "IGN", IGN, "BELTP", BELTP, "BELTD", BELTD, "ALARM", ALARM)

    ignition = input("put key in ignition [y] [n]: ")

    if ignition == "n":
        print ("goodbye")
        exit()
    elif ignition == "y":
        IGN.append(1)
    print("DRIV", DRIV, "PASS", PASS, "IGN", IGN, "BELTP", BELTP, "BELTD", BELTD, "ALARM", ALARM)
    startcar = input("start car [y] [n]: ")
    print("DRIV", DRIV, "PASS", PASS, "IGN", IGN, "BELTP", BELTP, "BELTD", BELTD, "ALARM", ALARM)
    if DRIV == "1" and PASS == "1" and BELTD == "0" and BELTP == "0":
        ALARM.append(0)
        print ("alarm on")
        exit()
    elif DRIV == "1" and PASS == "1" and BELTD == "1" and BELTP == "1": 
        ALARM.append(1)
        print ("alarm off") 
        print ("car started")
        exit()  
    else:
        print ("error")
        exit()    
    



main()