a,b=map(int,input().split())
def pf1(a,b):
    for i in range(1,a+1):
        def con(a,b):
            if (a*b//i)==a:
                print(i)
                return True
            else:
                print(i)
                return False
    return con(a,b)
if (pf1(a,b)):
    print("yes")
else:
    print("no")
