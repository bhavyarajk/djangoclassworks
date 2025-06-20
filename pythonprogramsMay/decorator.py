#Decorator

def decorator(fun):
    def wrapper(x,y):
        if x<y:
            x,y=y,x
        return fun(x,y)
    return wrapper

@decorator
def sub(x,y):
    s=x-y
    print(s)
@decorator
def div(x,y):
    s=x/y
    print(s)

sub(10,5)
sub(5,10)
div(10,5)
div(5,10)




