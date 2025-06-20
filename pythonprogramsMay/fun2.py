#Define a function to find the simple interest

#Define using 3 parameters

# p-principal amount
# n-year
# r-rate
#
#
# SI-->p*n*r/100


def simple_interest(p,n,r):   #Here p,n,r -parameters
    "Simple Interest Calculation"
    SI=p*n*r/100

    print("Simple Interest",SI)

    return


# simple_interest(1000,2,6)
amount=int(input("Enter the amount"))
years=int(input("Enter the years"))
rate=int(input("Enter the rate"))
simple_interest(amount,years,rate) #amount,rate,years -arguments