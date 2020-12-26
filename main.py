import time
n=0
x=input('type the range')
start=time.time()
for i in range(2,int(x)):
    j=2
    m=i**0.5 #core:Set the upper limit of the enumeration to the radical i
    while j<=m:
        if i%j==0:
            break
        j+=1
    else:
        print(i)
        n=n+1
stop=time.time()        
print('the number is',n)
print('it has cost',stop-start,'s')        
