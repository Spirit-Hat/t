def Pevious(number):
    return number-1

def Next(number):
    return number+1


if __name__=='__main__':
    number = int(input())

    print("The next number for %d is %d." % (number, Next(number)))
    print("The previous number for %d is %d." % (number, Pevious(number)))