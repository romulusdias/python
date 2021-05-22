def fib(n): # write Fibonacci series upto n
    a, b = 1, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        print()
fib(78)