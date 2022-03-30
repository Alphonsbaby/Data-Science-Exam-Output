
def missing(n):
    num=set([0,1,2,3,4,5,6,7,8,9])
    n=set([int(i) for i in n])
    n=n.symmetric_difference(num)
    n=sorted(n)
    return n

print("missing value:",missing([2,3,4,5,6,3,4,5,6,7]))