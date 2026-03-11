total_running_cost = 0
student_percentage_discount = 10

def main():
    print("Welcome to the Python Coffee Shop!")
    place_order = input("would you like to place an order?: (yes/no)").lower()
    if place_order == "no":
        exitshop()
    elif place_order == "yes":
        customer_name = input("What is your name? ").lower()  
        student_check = input("Are you a student? (yes/no): ").lower()
        order(customer_name, student_check, total_running_cost)
    #while place_order == "yes": 

def exitshop():
    print("No worries, have a nice day")
    exit()

def order(customer_name, student_check, total_running_cost):
    
      
    print("Hello, " + customer_name + "! Let's order some coffee.")

    price_coffee = 3.50
    price_latte = 4.00
    price_mocha = 4.50

    print("Coffee: $" + str(price_coffee))
    print("Latte: $" + str(price_latte))
    print("Mocha: $" + str(price_mocha))

    
    while True:
        
        choice = input("What would you like to order? (coffee/latte/mocha): ").lower()

        if choice == "coffee":
            cost = price_coffee
        elif choice == "latte":
            cost = price_latte
        elif choice == "mocha":
            cost = price_mocha
        else:
            print("Sorry, we do not have that.")
            cost = 0

        quantity = int(input("How many cups would you like? "))

        #total_cost = cost * quantity
    
        if student_check == "yes":
            total_cost = cost * quantity
            student_discount = total_cost * (student_percentage_discount / 100)
            total_cost = total_cost - student_discount
            total_running_cost = total_running_cost + total_cost

        elif student_check == "no":    
            total_cost = cost * quantity
            total_running_cost = total_running_cost + total_cost

        

        print("Your total is: $" + str(total_cost))
        print("Your total running cost is: $" + str(total_running_cost))
        another_order = input("Would you like to make another order? (yes/no): ").lower()
        if another_order == "yes":
            order(customer_name, student_check, total_running_cost) 
        elif another_order == "no":
            exitshop()

#else:
    #print("No worries, have a nice day")
main()