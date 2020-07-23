sample_size = int(input("How many people do you want to find the probability for of sharing the same birthday?"))
lower_limit = int(365 - (sample_size-1))

def limited_fac(number):
    if (number) == 365:
        return (365)
    else:
        return(number *limited_fac(number+1))
        
prob = (1-(limited_fac(lower_limit)/(365**sample_size)))
print (prob*100,"%")
