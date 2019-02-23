def avg(n,ls):
    sum=0
    for i in ls:
        sum+=i
    av=int(sum/n)
    print(av)
n=int(input())
x=list(map(int,input().split(" ")))
avg(n,x)
