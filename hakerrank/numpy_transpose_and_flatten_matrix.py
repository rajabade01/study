import numpy

if __name__=='__main__':
    n, m = map(int, raw_input().split())
    array = numpy.array([raw_input().strip().split() for _ in range(n)], int)
    print (array.transpose())
    print (array.flatten())
