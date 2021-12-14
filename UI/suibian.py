def recursive(n):
    if n==1:
        return 1
    else:
        return n*recursive(n-1)
a = 5
print('%d! = %d' % (a,recursive(a)))
