#https://www.patest.cn/contests/pat-b-practise/1001
n=int(input())
if n>1000:
    exit

count=0
while True:
    if n==1:
        break

    #print(n) #log
    if n%2==0:
        n=n/2
    else:
        n=(3*n+1)/2
    count+=1

print(count)



