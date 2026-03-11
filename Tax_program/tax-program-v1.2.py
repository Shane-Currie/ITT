#Get Tax income
def main():
    income = float(input("Enter your taxable income: "))
    if income > 20000 and income < 50000:
        income_more_than_20000(income)
    elif income <= 20000:
        income_less_than_20000(income)
    elif income >= 50000:
        income_more_than_50000(income)         
    else:
        print("incorrect input.")        
    
#function - income is more the 20000 and less than 50000
def income_more_than_20000(income):
    tax_rate = 0.02
    tax_amount = income * ( tax_rate / 100) 
    after_tax_income = income - tax_amount
    print ("you owe $",tax_amount, "in taxes.") 
    print ("your income after taxes is $",after_tax_income)

#function - income is less the 20000
def income_less_than_20000(income):
    print("still being coded, income under 20000")

#function - income is more than 50000
def income_more_than_50000(income): 
    print("still being coded, income over 50000")


main()

