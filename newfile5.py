import random
b=["a1","a2","a3","a4","a5"]
b1=[]
for i in range(5):
    s=random.sample(b,5)
    if s not in b1:
      b1.append(s)
for i in range(5):
    for j in range(5):
        print(b1[i][j],end=" ")
    print() 