a = [1,2,3,2,3,2,4,4,5,4]
c = []
t=[]
for i in range(0,10):
    for j in range(i+1,10):
        if a[i]==a[j]:
            c.append(i)

for i in a:
    for j in c:
        a.remove(j)
    a.remove(i)

for i in a:
    print(i)
