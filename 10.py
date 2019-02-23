def is_power(n):
    if n<=0:
        return False
    else:
        return n&2==0
n=int(input())
x=is_power(n)
if x:
    print("yes")
else:
    print("no")
