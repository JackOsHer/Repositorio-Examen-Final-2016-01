primos = [2]
nmax = 1000
for x in range(3, nmax):
    for i in range(2, x):
        if x%i != 0:
           
            continue
        else:
            
            break 
    else:
        
        print (len(primos))
        primos.append(x)




