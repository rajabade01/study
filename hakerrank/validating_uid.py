import re
import sys

uid_input = sys.stdin.readlines()
end = (int(uid_input[0]))+1
uid_input = uid_input[0 : end]
del uid_input[0]

for uid in uid_input:
    u = ''.join(sorted(uid.rstrip()))
    try:
        assert re.search(r'[A-Z]{2}', u)
        assert re.search(r'\d\d\d', u)
        assert not re.search(r'[^a-zA-Z0-9]', u)
        assert not re.search(r'(.)\1', u)
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')