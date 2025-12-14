def a(x):
    if x==0 or x==1:
        return 1
    else:
        return a(x-1)*x
print(a(3)) 