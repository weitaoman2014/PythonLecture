def fun(a,b):
    if a>b:
        max=a
    else:
        max=b
    while True:
        if (max%a==0)and(max%b==0):
            fun=max
            break
        else:
            max+=1
    print(fun)#print 打。
fun(2,5)


