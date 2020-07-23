cur1 = raw_input("What currency do you have?")
cur2 = raw_input("What currency do you want to it to?")
amt1 = int(raw_input("What is the amount you want to convert?"))

if cur1 == "P" or "p" or "pounds" or "Pounds" and cur2 == "E" or "e" or "euro" or "Euro":
    amt2 = amt1 * 1.25

elif cur1 == "P" or "p" or "pounds" or "Pounds" and cur2 == "y" or "Y" or "yen" or "Yen":
    amt2 = amt1 * 174.29
    
elif cur1 == "P" or "p" or "pounds" or "Pounds" and cur2 == "d" or "D" or "dollars" or "Dollars":
    amt2 = amt1 * 1.71
    

elif cur1 == "E" or "e" or "euro" or "Euro" and cur2 == "d" or "D" or "dollars" or "Dollars":
    amt2 = amt1 * 1.36

elif cur1 == "E" or "e" or "euro" or "Euro" and cur2 == "p" or "P" or "pounds" or "Pounds":
    amt2 = amt1 * 0.8

elif cur1 == "E" or "e" or "euro" or "Euro" and cur2 == "y" or "Y" or "Yen" or "Y":
    amt2 = amt1 * 138.68


elif cur1 == "D" or "d" or "dollar" or "Dollar" and cur2 == "y" or "Y" or "Yen" or "yen":
    amt2 = amt1 * 101.78
    
elif cur1 == "D" or "d" or "dollar" or "Dollar" and cur2 == "e" or "E" or "Euro" or "euro":
    amt2 = amt1 * 0.73

elif cur1 == "D" or "d" or "dollar" or "Dollar" and cur2 == "p" or "P" or "Pounds" or "pounds":
    amt2 = amt1 * 0.58


elif cur1 == "Y" or "y" or "yen" or "Yen" and cur2 == "p" or "P" or "Pounds" or "pounds":
    amt2 = amt1 * 0.0057

elif cur1 == "Y" or "y" or "yen" or "Yen" and cur2 == "d" or "D" or "Dollars" or "dollars":
    amt2 = amt1 * 0.0098

elif cur1 == "Y" or "y" or "yen" or "Yen" and cur2 == "e" or "E" or "Euro" or "euro":
    amt2 = amt1 * 0.0072

else:
    print ("Enter a valid currency...")

print("%.2f" % round(amt2,2))
print amt2
