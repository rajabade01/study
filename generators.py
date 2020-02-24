def f():
     while True:
         val = yield
         yield (val*10)


g = f()
next(g)
print(g.send(10))
next(g)
print(g.send(11))
next(g)
print(g.send(12))
next(g)
print(g.send(13))
next(g)
print(g.send(14))