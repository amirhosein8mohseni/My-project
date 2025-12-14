def amir(x):
    if(x==0):
        return 1
    else:
        return amir(x-1)*2
print(amir(3))