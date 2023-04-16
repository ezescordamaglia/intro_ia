
dict1 = {1:10, 2:20, 3:30}
dict2 = {3:30, 4:40}
dict3 = {5:50}

# Forma 1
dict1.update(dict2)
dict1.update(dict3)
print(dict1)

# Forma 2
new_dict = {**dict1, **dict2, **dict3}
print(new_dict)

# Forma 3 (Solo con Python 3.9)
# print(dict1 | dict2 | dict3)