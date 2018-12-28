import numpy

if __name__=='__main__':
    n,m = map(int, raw_input().split(' '))
    numpy.set_printoptions(sign=' ')
    print(numpy.eye(n,m))