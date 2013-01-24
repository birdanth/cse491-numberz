# this is an implementation of the 'sieve' functionality using
# a generator.


_primeslist = [2]

def _is_prime(primes, n):
    for i in primes:
        if n % i == 0:
            return False
    return True

def next():
    start = _primeslist[-1] + 1
    while 1:
        if _is_prime(_primeslist, start):
            _primeslist.append(start)
            return start
        start += 1

def sieve():
    while 1:
	yield next()

# additional questions to address:
# - could you swap the last two lines of the while statement?  what are the
#    plusses and minuses of doing so?
# - is there a way to condense the 'while' loop into two statements? try
#    getting rid of the next_fib variable.



