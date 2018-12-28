
string, parts = raw_input(), int(raw_input())

for part in zip(*[iter(string)] * parts):
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))
