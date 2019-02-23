n=int(input())
c=0
for i in range(1,11):
    if i==n:
        c=1
if c==0:
    print("No")
else:
    print("Yes")
