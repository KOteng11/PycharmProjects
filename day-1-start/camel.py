name = input("camelCase: ")
names = ""
for char in name:
    if char.isupper():
        names += "_"
    names += char.lower()

print(names)






