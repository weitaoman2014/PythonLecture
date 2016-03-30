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
    print(fun)#print 打印不能放在定义函数的外面，因为程序执行时先执行定义函数外面的代码。
fun(2,5)


