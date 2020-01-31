from functools import reduce
import time

def foo(name):
    print('good afternoon' + " " + name)

bar = foo
bar('foo')


class Greeter:
    def __init__(self, greeting):
        self.greeting = greeting

    def __call__(self, name):
        print(self.greeting + " " + name)

morning = Greeter('good morning')
#print(callable(morning))
#morning('chao')

x_run = {
    0: morning,
    1: foo,
    2: bar
}

scores = [3, 6, 8, 9, 11]

modified_scores = list(map(lambda x: x * 4, scores))
#print(modified_scores)
modified_scores = list(filter(lambda x: True if x % 2 == 0 else False, scores))
#print(modified_scores)
modified_scores = reduce(lambda x, y: (x + y), scores)
#print(modified_scores)


def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def display_time(func):
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time()
        print("total time: {:.4} s".format(t2 - t1))
        return result
    return wrapper

@display_time
def prime_nums(num_high=1000):
    counter = 0
    for i in range(2, num_high):
        if is_prime(i):
            counter += 1
    return counter

print(prime_nums(10000))
