import numpy as np

if __name__=='__main__':
    a, b, c = map(int, raw_input().split())
    arrA = np.array([raw_input().split() for _ in range(a)], int)
    arrB = np.array([raw_input().split() for _ in range(b)], int)
    print np.concatenate((arrA, arrB), axis=0)