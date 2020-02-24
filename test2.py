l1 = [1,2,3,3,4,1,2,3,1,2,3]
max_count = 0
l2 = []
if (len(l1) >= 3):
    for i in range(len(l1)):
        if(len(l2) == 0):
            l2.append(l1[i])

        elif(l1[i] == l1[i-1] + 1):
            l2.append(l1[i])
            if(len(l2) == 3):
                max_count += 1
                l2 = []
                continue
        else:
            continue
    print(max_count)
else:
    print("wrong input list")
