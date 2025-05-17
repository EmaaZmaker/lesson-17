def cube(number):
    return number*number*number
def divide_by_3(number):
    if number %3==0:
        return cube(number)
    else:
        return False
print(divide_by_3(8))
print(divide_by_3(6))

    