def hannoi(n,a,b,c):
    k=0
    if n>0:
        hannoi(n-1,a,c,b)
        print("moving from %s to %s " % (a,c))
        k=k+1
        hannoi(n-1,b,a,c)
    print(k)

hannoi(4,'A','B','C')