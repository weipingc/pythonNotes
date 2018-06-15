>>> na
[0, 1, 2, 3, 4, 5]
>>> na1 = [i+1 for i in na]
>>> na1
[1, 2, 3, 4, 5, 6]
>>> m1 = {'a':1, 'b':2}
>>> m2 = {k:v for k,v in d1.items()}
>>> m2
{'a': 1, 'b': 2}
>>> m3 = {k:v+10 for k,v in m1.items()}
>>> m3
{'a': 11, 'b': 12}
