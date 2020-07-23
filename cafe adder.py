take_out = input("Is the order a take out?:(Y/N)")
pensioner = input("Are you a pensioner?:(Y/N)")

item = input("What is the name of item?:")
price = input("What is the price?:")
quantity = input("How many of the item?:")

item2 = input("What is the name of item?:")
price2 = input("What is the price?:")
quantity2 = input("How many of the item?:")

item3 = input("What is the name of item?:")
price3 = input("What is the price?:")
quantity3 = input("How many of the item?:")

item4 = input("What is the name of item?:")
price4 = input("What is the price?:")
quantity4 = input("How many of the item?:")

item5 = input("What is the name of item?:")
price5 = input("What is the price?:")
quantity5 = input("How many of the item?:")

cost = (quantity*price)+(quantity2*price2)+(quantity3*price3)+(quantity4*price4)(quantity5*price5)

if take_out == ("Y"):
    cost = cost*1.2
if pensions == ("Y"):
    cost = cost*0.9

print (cost)


