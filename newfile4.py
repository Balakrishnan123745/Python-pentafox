a=list(input())
b=list(input())

c=a[0].lower()
d=b[0].lower()
if(c==d):
    a.remove(a[0])
    b.remove(b[0])

l=a
m=b


n=[]
for i in l:
    for j in m:
        if(i==j):
            n.append(j)

for i in n:
    if i in l:
        l.remove(i)
    if i in m:
        m.remove(i)
o=l+m
s=""
for i in o:
    s+=i
print(s)
