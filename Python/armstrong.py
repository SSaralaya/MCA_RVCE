size=int(input("Enter the end range to determine the armstrong Numbers:"))
l1=[]
res=1
sum=0
for i in range (1,size):
    length=len(str(i))
    num=i
    while(num > 0):
        # print("num:",num)
        rem=num%10
        # print("rem:",rem)
        res=1
        for j in range(0,length):
            res=res*rem
        sum=sum+res
        # print("sum:",sum)
        num=num//10
    if(i == sum):
        l1.append(i)
    sum=0
print("Armstrong Numbers are:",l1)     