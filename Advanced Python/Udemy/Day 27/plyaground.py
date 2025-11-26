def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
add(1,3,5,6,7,8,99)


def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
bar(1, 2)

# Your choice of '1 2 'yes please!' 0' is correct
# When you call the function bar(1, 2),
# the parameters spam and eggs are assigned the values 1 and 2,
# while the optional parameters toast and ham take their default
# values of
# 'yes please!' and 0, respectively.
# This results in the output being exactly as you selected.


def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
bar(toast='nah', spam=4, eggs=2)
#  2 'nah' 0

# when you use the *args syntax in a function,
# it collects all positional arguments into a single object,
# which is actually a tuple.

def all_aboard(a, *args, **kw):
    print(a, args, kw)
all_aboard(4, 7, 3, 0, x=10, y=64)

# 4 (7, 3, 0) {'x': 10, 'y': 64}
# is correct because the function all_aboard takes the first argument as
# a standalone value (4),
# then collects the subsequent positional arguments (7, 3, and 0) into a tuple,
# while the keyword arguments x and y are organized into a dictionary.