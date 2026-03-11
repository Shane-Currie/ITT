#Get Tax income
def main():
    income = float(input("Enter your taxable income: "))
    if income > 20000:
        income_more_than_20000()
    elif income <= 20000:
        income_less_than_20000()
    else:
        print("Invalid input. Please enter a valid income amount.")        
    
#function - income is more the 20000
def income_more_than_20000():
    print("still being coded, income over 20000")


#function - income is less the 20000
def income_less_than_20000():
    print("still being coded, income under 20000")

#display tax


main()

