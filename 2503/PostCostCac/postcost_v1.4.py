
first_ounce_cost = 0.05
ongoing_ounce_cost = 0.10

def cost_one_ounce(weight_input):
    print ("in progress")
    total_cost = weight_input * first_ounce_cost
    print ("total cost: $", total_cost)


def cost_multiple_ounce(weight_input):
    print ("in progress")
    weight_input = weight_input - 1
    total_cost = weight_input * ongoing_ounce_cost + first_ounce_cost
    print ("total cost: $", total_cost)
    
def cac():
        try:
            weight_input = float(input("enter weight by ounce: "))
            if weight_input == 1:
                cost_one_ounce(weight_input)
            elif weight_input > 1:
                cost_multiple_ounce(weight_input) 
            else:
                print ('incorrect input')
        except:
            print ('incorrect input')
            

def main():
    while True:
        runprogram = str(input("run program? [yes] or [no]: ")).lower()
        if runprogram == "yes":
            cac()
        elif runprogram == "no": 
            print ('exting')
            exit()
        else:
            print ("incorrect input, try again")    

main()
