def Factorial(x):
    if x==1 or x==0:
        return 1
    else:
        return x*Factorial(x-1)
    '''this is recursive function'''
print(Factorial.__doc__)
print(Factorial(0))
print(Factorial(4))


    