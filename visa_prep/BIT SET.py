n=int(input())
i=int(input())
x=bin(n)[2:]

if i<=len(x) and x[-i]=="1":
    print("true")
else:
    print("false")
