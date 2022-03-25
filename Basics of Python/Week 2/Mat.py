pi=3.14
def sum(x,y):
    return x+y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def minus(x,y):
    return x-y
def area_of_circle(r):
    return pi*r*r

def sum_args(x=1,y=2,*args):
    sum=x+y
    for element in args:
        sum=sum+element
    return sum