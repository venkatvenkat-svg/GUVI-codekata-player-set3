n,k=map(int,input().split())
if n<k:
    min=n
else:
    min=k
for fact in range(1,min+1):
    if(n%fact==0 and k%fact==0):
        gcd=fact
print(gcd)
