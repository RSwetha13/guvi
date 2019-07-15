k=int(input())
lst=list(map(int,input().split()))[:k]
lst.sort()
print(*lst,end=" ")
