t=int(input())
while(t):
    l=int(input())
    dec=0
    i=0
    while(l):
        r=l%10
        dec+=r*(8**i)
        i+=1
        l=l//10
    b=[]
    i=0
    while(dec):
        r=dec%2
        b.append(r)
        dec=dec//2
    k=''
    for i in range(len(b)-1,-1,-1):
        k=k+str(b[i])
    print(k)
    t-=1