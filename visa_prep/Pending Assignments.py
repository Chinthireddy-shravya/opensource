x,y,z=map(int,input().split())
t1=x*y
t2=z*24*60
if t1<=t2:
    print("YES")
else:
    print("NO")
