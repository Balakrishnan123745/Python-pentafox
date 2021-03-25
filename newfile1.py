a=list(map(int,input().split()))
b=int(input())
c1=0
c2=0
k=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        d=a[i]+a[j]
        print(d)
        if(d==b):
            k=1
            c1=a[i]
            c2=a[j]
            break
    
        d=0
    if (k==1):
        break
if (k==1):
    print(c1,",",c2)
else:
    print("No Pairs found")