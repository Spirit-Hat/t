
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


def task122(x,n,a):

    if n == 0 :
        return 0
    else:
        x = (x**(n)*(a**(n-n))) + task122(x,n-1,a)
        return x

def task1_1(x,n,a):
    sum = 0
    for i in range(0, n  ):
        # for a in range(0,n):
            count = (x**(i)*(a**(n-i)))
            sum += count
    return sum



if __name__ == '__main__':
    # task1(1,4,1,0)
    print(task122(1,10,1))
    print(task1_1(1,4,1))