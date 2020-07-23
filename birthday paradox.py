#probability someone else in the sample has the same birthday
n = int(input("How many people do you want to find the probability for of sharing the same birthday?"))

def prob_calc(number):
    i=0
    final = 1
    for i in range(0,number):
        prob = (365-i)/365
        print (prob)
        i=i+1    
        final = prob * final 
    return (1- final)

print ((prob_calc(n)*100),"%")
