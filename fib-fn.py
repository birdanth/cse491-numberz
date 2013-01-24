last_1 = 1 #1
last_2 = 1 #2

def next():
    global last_1, last_2

    next_fib = last_1 + last_2
    last_1, last_2 = last_2, next_fib
    
    return next_fib

print next() #3
print next()
print next()
