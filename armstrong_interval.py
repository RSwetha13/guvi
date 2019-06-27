g,k=map(int,input().split())
for i in range(g+1,k):
  sum=0
  num=i
  while(num>0):
    z=num%10
    num=num//10
    y=z**3
    sum=sum+y
  if(i==sum):
    print(sum,end=' ')
