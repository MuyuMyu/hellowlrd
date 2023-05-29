a=[1,2,3,4,5,6,7,8,9,10]
def fn(a):
    return a%2==1
list=filter(fn, a)
list=[i for i in list]
print(list)