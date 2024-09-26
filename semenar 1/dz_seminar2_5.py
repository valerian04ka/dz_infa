N = int(input())
b = int(input())
c = int(input())
n = 0
k = 0
m = 0
h = ''
while N >= 1:
    n += (N%10) * b**(k)
    N = N//10
    k += 1 
    
while n > 0 :
    m = n % c
    h = str(m) + h
    n = n // c
print(h)
    
