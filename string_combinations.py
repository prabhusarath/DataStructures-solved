
# coding: utf-8

# In[39]:

import itertools

s = 'And'

up = s.upper()
low = s.lower()

dicts = zip(s.upper(), s.lower())

list(
    ''.join(x) for x in itertools.product(*dicts)
     )

