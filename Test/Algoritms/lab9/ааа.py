
def task1(x,n,nx,math):
    nx=nx
    x=x
    n=n
    math= math
    if nx != n:
        math += ( -1 *(((-x)**nx)/nx))
        nx=nx+1
        task1(x,n,nx,math)
    else:
       print(math)


def task122(x,n):

    if n == 0 :
        return 0
    else:
        x = ( -1 *(((-x)**n)/n)) + task122(x,n-1)
        return x

def task1_1(x,n,):
    sum = 0
    for i in range(1,n +1 ):
        count = (-1 *(((-x)**i)/i))
        sum += count
    return sum



if __name__ == '__main__':
    task1(1,4,1,0)
    print(task122(1,4))
    print(task1_1(1,4))