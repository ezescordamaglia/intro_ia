
from collections import Counter

dict1 = {'a':1, 'b':5, 'c':10}
dict2 = {'a':2, 'c':1, 'd':3}

# Forma 1
print(Counter(dict1) + Counter(dict2))

# Forma 2 Profe
result = {}

dict_keys = set(list(dict1) + list(dict2))
for key in dict_keys:
    result[key] = dict1.get(key, 0) + dict2.get(key, 0)

print(result)