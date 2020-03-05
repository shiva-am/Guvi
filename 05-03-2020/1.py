n=int(input())
for i in range(n,0,-1):
  if int((i**0.5)**2)==i and round(n**(1./3))**3==i:
    print(i)
    break
