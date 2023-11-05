globales = dict(globals())

max = max(len(item) for item in globales)
for item in globales:
    esp = max-len(item)
    print(f'{" "*esp}{item} = {globales[item]}')

command = "cd koiekfps"

print(command[3:len(command)])