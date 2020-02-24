def my_decorator(func):
    def inner():
        print("decorator")
        func()
        print("after decorator")
        #return func

    return inner()


def original():
    print ("in original function")


if __name__ == "__main__":
    mydec = my_decorator(original)
    print(mydec)