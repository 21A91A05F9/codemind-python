n=int(input())
e=0
o=0
n1=0
while(n):
    r=n%10
    n=n//10
    n1+=1
    if(r%2==0):
        e+=1
    else:
        o+=1
if(n1==e):
     print('Even')
elif(n1==o):
    print('Odd')
else:
    print('Mixed')