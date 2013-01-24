import fib

def test0():
    f = fib.fib()
    n = 0
    for i in f:
       n+=1
       print i
       if n > 3 : break


def test1():
    f = fib.fib()
    global i = iter(f)
    i.next()
    assert i.next() == 2

def test2():
    f = fib.fib()
    global i = iter(f)
    i.next()
    assert i.next() == 3

def test3():
    f = fib.fib()
    global i = iter(f)
    i.next()
    assert i.next() == 5


test1()
test2()
test3()
