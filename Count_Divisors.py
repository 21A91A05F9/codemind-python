l,r,k=map(int,input().split())
d=0
for i in range(l,r+1):
    if(i%k==0):
        d+=1
print(d)