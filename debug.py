"""Obligatoriamente, usar globals() y locals() como parámetros"""

def _load(glob, loc):
    gl = dict(glob)
    lo = dict(loc)

    for item in gl:
        try: del lo[item]
        except: pass
    
    return gl, lo

def _show_variables(globales, locales):
    gl, lo = _load(globales, locales)

    maxgl = max(len(item) for item in gl)
    maxlo = max(len(item) for item in lo)
    
    print("\nGLOBALS\n")
    for item in gl:
        esp = maxgl-len(item)
        print(f'{" "*esp}{item} = {gl[item]}')

    print("\n(only) LOCALS\n")
    for item in lo:
        esp = maxlo-len(item)
        print(f'{" "*esp}{item} = {lo[item]}')

"""def _show_variables_scope(globales, locales)

def _show_info(var, globales, locales):
    f'{var=}'.split('=')[0]"""

"""
import inspect

def obtener_globals_y_locals():
    # Obtén el marco de llamada actual (frame)
    marco_de_llamada = inspect.currentframe()
    
    # Obtén el espacio de nombres global del archivo que importa el módulo
    espacio_global = marco_de_llamada.f_back.f_globals
    
    # Obtén el espacio de nombres local del archivo que importa el módulo
    espacio_local = marco_de_llamada.f_back.f_locals
    
    # Devuelve los diccionarios completos de globals() y locals()
    return espacio_global, espacio_local

# Llama a la función del módulo para obtener los diccionarios de globals() y locals()
diccionario_globals, diccionario_locals = obtener_globals_y_locals()

# Imprime los diccionarios completos de globals() y locals()
print("Globals():", diccionario_globals)
print("Locals():", diccionario_locals)
"""