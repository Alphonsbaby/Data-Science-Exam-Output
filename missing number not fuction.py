l=[]
print("enter value 10 digit mobile number : \n")
for i in range(0,9):
    x=input()
    l.append(x)
n=l
num=set([0,1,2,3,4,5,6,7,8,9])
n=set([int(i) for i in n])
n=n.symmetric_difference(num)
n=sorted(n)
print("missing number",n)