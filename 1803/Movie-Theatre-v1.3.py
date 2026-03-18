# Starter
  # list of (title, qty, price_each)

# TODO: use a while loop that continues until the user enters 'done'
# 1) ask for movie title (case sensitive is fine)
# 2) if title not in movies, print the available keys and continue
# 3) ask for quantity (int)
# 4) append (title, qty, movies[title]) to purchases
# 5) optional: track running subtotal

# TODO: iterate over purchases and compute line totals
# for title, qty, price_each in purchases:
#     line_total = ...
#     print(...)
# print("Total:", ...)



movies = {
    "Dune": 12.5,
    "Barbie": 11.0,
    "Oppenheimer": 13.0,
    "Spirited Away": 10.0
}

def reciept(viewmovies, ticketcost, ticketamount):
    print ("reciept")
    print ("selection ", viewmovies)
    print ("total tickets" , ticketamount)
    print ("cost per ticket $", movies[viewmovies])
    print ("total cost $" , ticketcost)
    
    exit()
  

purchases = []


print(movies)
viewmovies = input("what movie would you like to watch: ").title()
if viewmovies  == "Dune" or "Barbie" or "Oppenheimer" or "Spirited Away":
    while True:
        print ("you have selected", viewmovies)
        print (viewmovies, "costs", movies[viewmovies])
        ticketamount = int(input("how many tickets would you like? "))
        ticketcosts = movies[viewmovies] * ticketamount
        print ("you opt to purchase" , ticketamount, "tickets totaling $", ticketcosts)
        confirm = input("input [done] to confirm: ").lower()
        if confirm == "done":
            print ("enjoy")
            reciept(viewmovies, ticketcosts, ticketamount)
            break
else:
    print("We dont have that, try again")



