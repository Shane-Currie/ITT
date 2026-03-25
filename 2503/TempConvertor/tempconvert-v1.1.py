

def fahrenheit_to_celsius():
    fahrenheit = float(input("enter fahrenheit: "))
    temp_convert = (fahrenheit-32) * 5/9
    print (temp_convert)

          
def main():
    while True:
        runprogram = str(input("run program? [yes] or [no]: ")).lower()
        if runprogram == "yes":
            fahrenheit_to_celsius()
        elif runprogram == "no": 
            print ('exting')
            exit()
        else:
            print ("incorrect input, try again")    

main()
