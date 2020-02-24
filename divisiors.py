def accum(s):
    # your code
    li = list(s)
    #output = []
    str1 = ""
    for i, value in enumerate(s):
        final = (value.upper())+(i * value) + "-"
        str1 = str1 + final

    return str1[:-1]


if __name__ == "__main__":
    string = "abcdef"
    output = accum(string)
    print(output)

