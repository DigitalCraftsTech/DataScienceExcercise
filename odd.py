



def  oddNumbers(l, r):
    k=[]
    for i in range(l,r+1):
        if i%2==0:
            i+=1
        else:
            k.append(i)
    return(k)
         
    
print(oddNumbers(1,10))

    
    
