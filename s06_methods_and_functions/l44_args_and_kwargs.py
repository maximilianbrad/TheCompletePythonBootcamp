def myfunc(a, b):
    '''
    Returns 5% of the sum of a and b
    '''
    return sum((a, b)) * 0.05


print(myfunc(40, 60))


def my_arg_func(*args):
    for item in args:
        print(item)
    return sum(args) * 0.05


print(my_arg_func(100, 200, 300, 500))


def my_kwarg_func(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')


my_kwarg_func(fruit='apple', vegetable='lettuce')


def my_arg_kwarg_func(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))


my_arg_kwarg_func(10, 20, 30, fruit='orange', food='eggs', animal='dog')
