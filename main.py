p=[0,1,5,8,9,10,17,17,20,24,30]
def cut_steel_ex(p,n):
    r=[0]
    s=[0]
    for i in range(1,n+1):
        res=0
        left=0
        for j in range(1,i+1):
            if j<len(p):
                if p[j]+r[i-j]>res:
                    res=p[j]+r[i-j]
                    left=j
                else:
                    continue
        r.append(res)
        s.append(left)
    ans=[]
    while n>0:
        ans.append(s[n])
        n-=s[n]
    return r[ans[-1]],ans[::-1]

cut_steel_ex(p,20)