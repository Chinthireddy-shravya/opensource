a,b,c,x=map(int,input().split())
if a+b>=x:
    print("YES")
elif b+c>=x:
    print("YES")
elif a+c>=x:
    print("YES")
else:
    print("NO")
