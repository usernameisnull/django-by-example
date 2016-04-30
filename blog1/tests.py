from django.test import TestCase


# Create your tests here.
class tracer:
    def __init__(self, func):  # On @ decoration: save original func

        self.calls = 0
        self.func = func

    def __call__(self, *args):  # On later calls: run original func

        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)


@tracer
def spam(a, b, c):  # spam = tracer(spam)
    print(a + b + c)  # Wraps spam in a decorator object





def tracer1(func):
    counter=[0]
    def wrapper(*args, **kwargs):
        counter[0] += 1
        print counter[0]
        func(*args, **kwargs)
    return wrapper

@tracer1
def spam1():
    pass

spam1()
spam1()
spam1()
