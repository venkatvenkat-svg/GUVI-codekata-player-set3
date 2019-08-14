x1,y1,x2,y2,x3,y3=map(int,input().split())
if(x1==x2 or x1==x3 or x2==x3 or y1==y2 or y1==y3 or y2==y3 ):
    print("yes")
else:
    print("no")
