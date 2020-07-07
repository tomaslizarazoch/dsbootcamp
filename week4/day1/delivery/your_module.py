# This file represents your module.
# Write the code...





def squares(n=10):
    print('Generating squares from 1 to {0}'.format(n ** 2))
    for i in range(1, n + 1):
        yield i ** 2

def attempt_float(x):
    try:
        return float(x)
    except:
        return x