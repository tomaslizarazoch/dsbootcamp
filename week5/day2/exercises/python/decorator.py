from functools import wraps
import pandas as pd
import matplotlib

def prepost(*arg, **kwargs):
    def real_decorator(function):
        @wraps(function)
        def wrapper(*a, **k):
            if "link" in kwargs.keys():

                df1 = pd.read_csv(kwargs['link'] , sep=",")
                print(df1)
            retval = function(*a, **k)
            df1.hist()
            return retval
        return wrapper
    return real_decorator

@prepost(link = 'http://winterolympicsmedals.com/medals.csv')
def _f_protected():
    v =  v = lambda x : True if x > 5  else False 
    l1 = [x  for x in range(16)]
    
    return list(filter(v, l1))

_f_protected()