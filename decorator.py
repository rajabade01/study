def decorator(*args, **kwargs):
    print("Inside decorator")

    def inner(func):
        print("Inside inner function")
        print(len(args), len(kwargs))
        func(args)
        print("I like " + kwargs['like'])
        print("I like " + kwargs['test'])
        return func

    return inner


@decorator(["list"],like="geeksforgeeks", test="test")
def func(*args):
    print("Inside actual function")
    print(args)


func(["list"])