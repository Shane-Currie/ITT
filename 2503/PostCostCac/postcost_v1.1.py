
first_ounce_cost = 0.05
ongoing_ounce_cost = 0.10

def cost_one_ounce(weight_input):
    print ("in progress")
    total_cost = weight_input * first_ounce_cost
    print ("total cost: $", total_cost)
    main()


def cost_multiple_ounce(weight_input):
    print ("in progress")
    total_cost = weight_input * ongoing_ounce_cost + first_ounce_cost
    print ("total cost: $", total_cost)
    main()

    
def main():
    weight_input = float(input("enter weight by ounce: "))
    if weight_input == 1:
        cost_one_ounce(weight_input)
    elif weight_input > 1:
        cost_multiple_ounce(weight_input)    


main()


