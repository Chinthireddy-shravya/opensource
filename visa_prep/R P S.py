n1,n2=input().split()
n1=n1.upper()
n2=n2.upper()
if (n1=='R' and n2=='P') or (n1=='P' and n2=='S') or (n1=='S' and n2=='R'):
        print("Charan")
    
elif (n2=='R' and n1=='P') or (n2=='P' and n1=='S') or (n2=='S' and n1=='R'):
    print("Vignesh")
else:
    print("NULL")
