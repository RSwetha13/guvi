x=int(input())
y=list(map(int,input().split(" ")))
z=sorted(y)
print(z[len(y)//2])
