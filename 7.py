def min_max(x):
    min=x[0]
    max=x[0]
    for i in x:
        if i<min:
            min=i
        if i>max:
            max=i
    print(min,max)
n=int(input())
x=list(map(int,input().split(" ")))
min_max(x)
