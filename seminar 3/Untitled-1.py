def fib(n):
    #if n in [0,1]:
     #   return n
    #return fib(n-1)+fib(n-2)

    #a , b = 0 , 1
    #for i in range(n):
        #a,b = a+b, a
    #return a
    c={0:0,1:1}
    if n in c:
          return c[n]
    c[n]= fib(n-1)+fib(n-2)
    return c[n]
print(fib(50))