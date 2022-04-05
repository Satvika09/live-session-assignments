n=int(input("enter a number:"))
for i in range(0,n):
    print(" "*i+" * "*(n-i))
for j in range(2,n+1):
    print(" "*(n-j)+" * "*j)
