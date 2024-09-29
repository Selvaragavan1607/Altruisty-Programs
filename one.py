def isreverse(l):
    for i,j in enumerate(l):
        if i==len(l)-1: return True
        if l[i]<l[i+1]:  return False

n=int(input("Enter the numeber of days: "))
l=list(map(int,input(f"Enter the prices of {n} stocks seperated by space: ").split()))
l=l[:n]

if len(l)==1: #If it's a single day stock
    print("Profit: 0")

elif isreverse(l): #if the stock prices is decreaing or same all day
    print("Profit: 0")
    
else:
    mi=min(l)
    ma=max(l)
    if l.index(mi)<l.index(ma):
        print("Profit: ",ma-mi)
    else:
        ml=[]
        for i in l:
            for j in l:
                if i!=j: ml.append(i-j)
        print("Profit: ",max(ml))
            
        
    
