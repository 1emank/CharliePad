"""import os

archivo = "-sa F:\\CODE\\PYTHON\\archivo.txt"

archivo = archivo.removeprefix("-saveas")
archivo = archivo.removeprefix("-sa")
archivo = archivo.removeprefix(" ")
print(archivo)

with open(archivo, 'r', encoding='utf-8') as fichero:
            contenido = fichero.read()

contenidoList = contenido.splitlines()
print(contenidoList)

input("Presiona Enter para salir")"""

import re

def eliminar_prefijos(accion, modo): #editable
        if modo == "new":
            prefixlist = '-new', '-n', ' '
        elif modo == "saveas":
            prefixlist = '-saveas', '-sa', ' '
        elif modo == "insert":
            prefixlist = "insert", "i", ' '
        else: #modo full
            prefixlist = '-saveas', '-save', '-edit', '-help', 'down', 'up', 'bajar', 'subir', 'edit', 'insert', '-sa', '-s', '-e', '-h', 'd', 'u', 's', 'b', 'e', 'i',  ' '

        for prefix in prefixlist:
            accion = accion.removeprefix(prefix)
        return accion

test_str = "insert 10 15 palabras 60 carácter.es!¿+`+¨Ç*^+_:;_ºª!\"·$%&\n/()=¿?€"

test_str = eliminar_prefijos(test_str, "insert")
 
print("The original string A is : " + str(test_str))

temp = re.compile("([0-9]+)([ ]+)([A-Za-zÀ-ȕ0-9 ._¡!-\"`¨'#%&ºª,:¿·;<>=\\n@\\€\£\¥\${\}\~\(\)\*\+\/\\\¿\?\[\]\^\|]+)") # type: ignore
res = list(temp.match(test_str).groups()) # type: ignore

# printing result
print(f"The list after the split of string and number : {res}")

test_str = "pepe"

if True:
     pepe = "pepito"

print(pepe) # type: ignore

e 8 ºª!"·$%&/()=?¿º1234567890'¡\|@#~€¬`+ç´-.,;:_¨^*Ç[]}{<>A-Za-zÀ-ȕ0-9 ._¡!\-\"`¨'#%&º,:¿·;<>=\\n@\\€\£\¥\${\}\~\(\)\*\+\/\\\¿\?\[\]\^\|  # type: ignore
