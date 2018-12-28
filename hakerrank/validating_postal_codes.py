import re

def validate_postal_code(postal_code):
    print (bool(re.match(r'^[1-9][\d]{5}$', postal_code)
                and len(re.findall(r'(\d)(?=\d\1)', postal_code)) < 2))

uid_input = str(input())
response = validate_postal_code(uid_input)


import re
n,m = map(int,input().split())
matrix = []
s = ''
for line in range(n):
    matrix.append(input()+' ')
s = ''.join(matrix[i][j] for j in range(m) for i in range(n))
s1 = re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])',' ',s)
print(s1)