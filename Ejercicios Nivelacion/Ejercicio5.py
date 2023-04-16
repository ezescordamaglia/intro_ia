
dict1 = {1:10, 2:20, 3:30}
dict2 = {3:30, 4:40}
dict3 = {5:50}

# Forma 1
dict1.update(dict2)
dict1.update(dict3)
print(dict1)

# Forma 1
for key, value in dict1.items():
    print("Clave: " + str(key) + ", Valor:" + str(value))

# Forma 2 - Menos eficiente
for key in dict1.keys():
    print("Clave: " + str(key) + ", Valor:" + str(dict1[key]))

