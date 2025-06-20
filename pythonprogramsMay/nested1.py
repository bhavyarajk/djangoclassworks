 # A toy vendor supplies three types of toys:

# Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.

# The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.

# On orders of more than Rs. 100 for key-based toys,a discount of 5% is given,

# and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.

# Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.

# Write a program that reads the product code and the order amount and prints out the net amount that t(the customer is required to pay after the discount.


p_code=int(input("Enter the product code:1/2/3"))
amount=int(input("Enter the actual price"))

if p_code==1:
    if(amount>=1000):
        dis=amount*10/100
        print("Bill amount",amount-dis)
    else:
        print("Bill amount",amount)

elif p_code==2:
    if (amount >= 100):
        dis = amount * 5/ 100
        print("Bill amount", amount - dis)
    else:
        print("Bill amount", amount)

elif p_code==3:
    if (amount >= 500):
        dis = amount * 10 / 100
        print("Bill amount", amount - dis)
    else:
        print("Bill amount", amount)

else:
    print("Invalid Product Code")












