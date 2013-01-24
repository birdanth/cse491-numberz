
# this is an implementation of E's sieve using
# Python's iterator functionality.  Here, 'sieve' is a class that
# obeys the iterator protocol.

class sieve(object):
    def __init__(self):
        self.primeslist = [2]

    def __iter__(self):
        return self

    def next(self): 
	start = self.primeslist[-1] + 1
	while 1:
	     for i in self.primeslist:
	          if start % i == 0:
			start += 1
	     self.primeslist.append(start)
	     return start
	          
	


