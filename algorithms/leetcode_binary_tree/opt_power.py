import sys

'''
2, 10
4, 5
(16, 2) * 1024
(256, 1) => 256
'''

def opt_power(x, n):
    if n == 1:
        return x
    elif n % 2 == 1:
        return opt_power(x**2, n //2) * x
    else:
        return opt_power(x**2, n //2)

pw = sys.argv[1]
print(opt_power(2,int(pw)))
