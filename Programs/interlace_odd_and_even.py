a=int(input())
b=int(input())
odds=[]
evens=[]
inter=[]
for i in range(a,b+1):
    if i%2!=0:
        odds.append(i)
for i in range(b,a-1,-1):
    if i%2==0:
        evens.append(i)
i,j=0,0
if a%2==0 and b%2==0:
    while i<len(odds) and j<len(evens):
        inter.append(evens[j])
        inter.append(odds[i])
        i+=1
        j+=1
    while j<len(evens):
        inter.append(evens[j])
        j+=1
elif a%2!=0 and b%2!=0:
    while i<len(odds) and j<len(evens):
        inter.append(odds[i])
        inter.append(evens[j])
        i+=1
        j+=1
    while i<len(odds):
        inter.append(evens[j])
        i+=1
else:
    while i<len(odds) and j<len(evens):
        inter.append(odds[i])
        inter.append(evens[i])
        i+=1
        j+=1
print(*inter)
