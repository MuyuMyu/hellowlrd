lis=[1,2,3,4,5]
def fn(x):
    return x**2
res=map(fn, lis)
ret=res
res=[i for i in res if i>10]
print(res)