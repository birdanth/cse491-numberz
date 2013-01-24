import sieve

list =  []

def test1():
    for n, i in zip(range(1), sieve.sieve()):
	list.append(i)
        assert i == 3

def test2():
    for n, i in zip(range(1), sieve.sieve()):
	list.append(i)
    assert list[1] == 5

def test3():
    for n, i in zip(range(1), sieve.sieve()):
        list.append(i)
    assert list[2] == 7


 


test1()
test2()
test3()


