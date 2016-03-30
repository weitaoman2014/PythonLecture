#http://www.pythontip.com/coding/code_oj_case/11
L=[2,8,3,50,85,88,45,25,63,56,89]
#L=[2,8,3,50]
sum=1
twoCount=0
fiveCount=0
zeroCount=0
for item in L:
    twoCountTmp = 0
    fiveCountTmp = 0
    while item%2 == 0:
        twoCountTmp+=1
        item = item/2
    twoCount += twoCountTmp

    while item%5 == 0:
        fiveCountTmp+=1
        item = item/5
    fiveCount += fiveCountTmp

zeroCount = fiveCount if fiveCount<twoCount else twoCount
print zeroCount



