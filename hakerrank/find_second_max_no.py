if __name__ == '__main__':
    n = int(input())
    arr = map(int, raw_input().split())
    arr.sort(reverse=True)
    first = arr[0]
    for element in arr:
        if element < first :
            print element
            break
    print arr