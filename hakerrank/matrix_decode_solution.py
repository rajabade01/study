import re

nm = raw_input().split()
n = int(nm[0])
m = int(nm[1])

matrix = []
s = ''
for line in xrange(n):
    matrix.append(raw_input()+' ')
s = ''.join(matrix[i][j] for j in range(m) for i in range(n))
s1 = re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])',' ',s)
print(s1)