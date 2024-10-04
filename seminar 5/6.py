def f(n):
    n = int(input())
    f[1] = 1
    f[2] = 2
    for i in range (n-1):
        f[i+1] = f[i] + f[i-1]
    print (f(n))
    

    