def fun(n, greatestNumber, steps):
    steps = steps + 1
    if n > greatestNumber:
        greatestNumber = n
    if (n == 1):
        end(greatestNumber, steps)
    #checking if the number is even
    if (n % 2) == 0:
        n2 = n/2
        fun(n2, greatestNumber, steps)
    #checking if the number is odd
    n3 = n/2
    if (isinstance(n3, float)  ):
        n1 = (3 * n) + 1
        fun(n1, greatestNumber, steps)