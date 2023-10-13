import os, sys, subprocess, shlex, socket, re

### CLASES PROGRAMA

class ubiArchivo:
    def __init__(self, archivoArg):
        self.nom = os.path.basename(archivoArg)
        self.abs = os.path.abspath(archivoArg)
        if os.path.dirname(archivoArg) == "":
            self.dir = self.abs.replace(self.nom, "")
        else:
            self.dir = os.path.dirname(archivoArg)

class scroller: 
    def __init__(self, size):
        self.size = size
        self.top = size-(size-1)
        self.bottom = size
        self.mensaje = ""
    
    def true_if_scrollable(self, lastline):
        if lastline - self.size <= 0:
            self.mensaje = "El fichero no tiene suficientes líneas"
            self.checked = False 
        else: self.checked = True
        return self.checked

    def up(self, x, lastline):
        if self.true_if_scrollable(lastline):
            self.top -= x
            self.bottom -= x
            self.mensaje = f"Subiendo {x} líneas"
            if self.top <= 0:
                self.top = 1
                self.bottom = self.size
                self.mensaje = f"Subiendo algo menos de {x} líneas" #post: número exacto
        
    def down(self, x, lastline):
        if self.true_if_scrollable(lastline):
            self.top += x
            self.bottom += x
            self.mensaje = f"Bajando {x} líneas..."
            if self.bottom > lastline:
                self.top = (lastline - (self.size-1))
                self.bottom = lastline
                self.mensaje = f"Bajando algo menos de {x} líneas" #post: número exacto

### FUNCIONES PROGRAMA

def os_is_windows(): 
    if os.name == 'nt':
        windowsBool = True
    else:
        windowsBool = False
    return windowsBool

def clear(): 
    if windowsBool:
        os.system('cls')
    else:
        os.system('clear')

def help_command():
    print("\nAyuda charliePADconsole. Comandos:\n")
    print("Nuevo archivo: Crea un archivo en la dirección y con el nombre especificado. cpc -new *dirección/nombre*\n    Ejemplos: cpc -n archivo\n              cpc -new documentos/notas")
    print("Abrir archivo: Abre un archivo con el nombre especificado de la dirección especificada. cpc -open *dirección/nombre*\n    Ejemplos: cpc -open archivo\n              cpc -o documentos/notas")
    print('Renombrar archivo: Cambia el nombre de un archivo en la dirección especificada. cpc -rename *dirección/nombre* *nuevo nombre*\n    Ejemplos: cpc -rename archivo "receta de sopa" \n              cpc -r documentos/notas notas_2023')
    print("Eliminar archivo: Elimina un archivo con el nombre especificado de la direcciión especificada cpc -delete *dirección/nombre*\n    Ejemplos: cpc -d archivo\n              cpc -delete C:/Usuarios/test.txt")
    print("\nSi no especificas una dirección, se buscarán los archivos en la dirección en la que se encuentra la consola (puedes usar los comandos que ya conoces de cmd o bash).")
    print('Recuerda usar comillas ("") en dirección en caso de que haya espacios. Por ejemplo:\n    cpc -new "documentos/nuevo archivo"\nEsta orden creará un archivo con el nombre "nuevo archivo", dentro del directorio relativo "documentos"')
    print('Mientras el programa esté abierto, verás "cpc" al principio de la línea de comandos\n')
    input("Presiona Enter para continuar\n")

def welcome():
    print("Bienvenido a charliePADconsole, tu bloc de notas de consola")
    print("\nComandos:\ncpc -new *direccion/nombre*\ncpc -open *direccion/nombre*\ncpc -rename *direccion/nombre antiguo* *nombre nuevo*\ncpc -delete *direccion/nombre*\ncpc -exit")
    print("\nAlternativamente, usa -n, -o, -r, -d, -e")
    print('Escribe "cpc -help" para más ayuda\n')

def new_command(args):
    fichero = ubiArchivo(args[2])
    print(f"Creando nuevo archivo: {fichero.nom}")
          
    if os.path.exists(fichero.abs):
         print(f'El archivo {fichero.abs} ya existe')
    else:
        with open(fichero.abs, 'w') as archivo:
            archivo.write("")
            print(f'Se ha creado el archivo {fichero.nom}')

def rename_command(args): 
    fichero = ubiArchivo(args[2])
    ficheroNuevo= ubiArchivo(args[3])
    absNuevo= fichero.dir+ficheroNuevo.nom
    print(f"Renombrando archivo: de {fichero.nom} a {ficheroNuevo.nom}")
    try:
        if ficheroNuevo.abs != absNuevo:
            print(f"Fallo de sintaxis: El archivo {fichero.nom} no se le ha cambiado el nombre")
        else:
            os.rename(fichero.abs, absNuevo)
            print(f'El archivo {fichero.nom} ha sido renombrado a {ficheroNuevo.nom}.')
    except FileNotFoundError:
        print(f'No se pudo encontrar el archivo {ficheroNuevo.abs}.')
    except FileExistsError:
        print(f'Ya existe un archivo con el nombre {ficheroNuevo.nom}.')
    except Exception as e:
        print(f'Ocurrió un error al renombrar el archivo: {e}')

def delete_command(args): 
    fichero = ubiArchivo(args[2])
    print(f"Borrando archivo: {fichero.nom}")
    if os.path.exists(fichero.abs): #verifica que existe archivo
        os.remove(fichero.abs)
        print(f"El archivo {fichero.nom} ha sido borrado.")
    else:
        print(f"El archivo {fichero.nom} no existe.")

def exit_command(): 
    print("Cerrando programa")

def open_editor(args): ### EDITOR

    ### FUNCIONES EDITOR

    def carac_archivo(contenido): #Mejorable (claridad de uso)
        simbolos = ['¿','?','.','.',';',':','¡','!']
        numpalabras = 0
        numcaracteres = 0
        ultimaLinea = 0
        for linea in contenido:
            ultimaLinea += 1
            for caracter in linea:
                numcaracteres += 1
            for simbolo in simbolos:
                linea = linea.replace(simbolo,' ')

            palabras = linea.split()
            for palabra in palabras:
                numpalabras += 1
        numcaracteres += ultimaLinea-1 #añadiendo newlines que existen en el archivo final, pero no en la lista de contenido
        return ultimaLinea, numpalabras, numcaracteres

    def print_archivo(contenido, top_line, end_line):
        nlinea = 1
        for line in contenido:
            if nlinea >= (top_line) and nlinea <= (end_line):
                print(f'{nlinea} {line}', end='\n')
            nlinea += 1
        print()
    
    def eliminar_prefijos(accion, modo): #Mejorable (podría servir para englobar separarContenido_linea también)
        if modo == "new":
            prefixlist = '-new', '-n', ' '
        elif modo == "saveas":
            prefixlist = '-saveas', '-sa', ' '
        elif modo == "insert":
            prefixlist = "insert", "i", ' '
        elif modo == "edit":
            prefixlist = "edit", "e", ' '
        else: #modo full
            prefixlist = '-saveas', '-save', '-edit', '-help', 'down', 'up', 'bajar', 'subir', 'edit', 'insert', '-sa', '-s', '-e', '-h', 'd', 'u', 's', 'b', 'e', 'i',  ' '

        for prefix in prefixlist:
            accion = accion.removeprefix(prefix)
        return accion

    def separarContenido_linea(linea): #Mejorable: Buscar re match any character
        print(linea)
        temp = re.compile("([0-9]+)([ ]+?)([A-Za-zÀ-ȕ0-9 ._¡!\-\"`´¨'#%&º\ª,:·;<>=\¬\@\€\£\¥\${\}\~\(\)\*\+\/\\\¿\?\[\]\^\|]*)") #type: ignore
        res = list(temp.match(linea).groups())[2] # type: ignore
        print(res)
        return str(res)

    def leer_archivo(archivo):
        with open(archivo, 'r', encoding='utf-8') as fichero:
            contenido = fichero.read()
        contenidoList = contenido.splitlines()
        return contenidoList

    def help_editor():
        clear()
        print('Comandos:\nGuardar archivo: -save/-s \nGuardar como: -saveas/-sa *dirección*\nConfigurar pantalla: -config/-c *número de líneas*\nAyuda: -help/-h\nSalir: -exit/-e\n')
        print('Bajar X líneas: down/d/bajar/b *número*\nSubir X líneas: up/u/subir/s *número*\nEditar X Línea: edit/e *número* *contenido*\nInsertar línea: insert/i *número* *contenido*\nInsertar línea nueva al final: insert/i\nEliminar línea: remove/r *número*')
        input("\nPresiona Enter para continuar\n")

    def guardar_archivo(archivo, cont):
        archivo = os.path.abspath(archivo)
        contenido = '\n'.join(cont)
        with open(archivo, 'w', encoding='utf-8') as fichero:
            fichero.write(contenido)
      
    def insertar_linea(contenido, linea, contLinea): 
        contenido.insert((linea-1), contLinea)
        return contenido
    
    def eliminar_linea(contenido, args):
        del contenido[int(args[1])-1]
        return contenido

    ### INICIALIZAR EDITOR

    topHelpLine = 'Opciones: (-s)ave, (-sa)veas *dirección*, (-c)onfig X, (-h)elp, (-e)xit\n'
    bottomHelpLine = 'Comandos: (d)own X, (u)p X, (e)dit X *contenido*, (i)nsert X *contenido*, (r)emove X'
    
    tamanio = 15 #Post: Hacer configuración peresistente
    scr = scroller(tamanio)
    editado = False

    fichero = ubiArchivo(args[2])
    contenido = leer_archivo(fichero.abs)

    accion = "Abrir archivo"
    mensajeOrden = str(fichero.abs)
    args = "" #Debug

    ### BUCLE PROGRAMA
    
    while True:
        clear()
        carac = carac_archivo(contenido)
        ultimaLinea = carac[0]
        palabras = carac[1]
        caracteres = carac[2]
        if editado: editmark = "*"
        else: editmark = ""
        print(f'\nArchivo: {fichero.abs}{editmark}, Líneas: {ultimaLinea}, Palabras: {palabras}, Carácteres: {caracteres}') #Añadir Bytes
        print(topHelpLine)
        print_archivo(contenido, scr.top, scr.bottom)
        print(bottomHelpLine)
        print(f'Última orden: {accion} | {mensajeOrden}')
        if editado: print("Archivo modificado sin guardar*")

        try:
            accion = input()
            try:
                args = shlex.split(accion)
            except:
                args = accion.split()
            if args[0] == ("-save") or args[0] == ("-s"): mensajeOrden = guardar_archivo(fichero.abs, contenido); editado = False; mensajeOrden = "Guardando archivo..."
            elif args[0] == ("-saveas") or args[0] == ("-sa"):
                args[1] = eliminar_prefijos(accion, "saveas");
                try:
                    guardar_archivo(args[1], contenido); editado = False
                    mensajeOrden = f"Archivo guardado como {args[1]}" ; fichero = ubiArchivo(args[1])
                except:
                    mensajeOrden = "Dirección no válida\n(Si la sintaxis y la ubicación es correcta, deben faltar permisos de administrador)"
            elif args[0] == ("-exit") or args[0] == ("-e"): break
            elif args[0] == ("-help") or args[0] == ("-h"): help_editor()
            elif args[0] == ("-config") or args[0] == ("-c"): scr = scroller(int(args[1]))
            elif args[0] == ("down") or args[0] == ("d") or args[0] == ("bajar") or args[0] == ("b"): scr.down(int(args[1]), ultimaLinea); mensajeOrden = scr.mensaje
            elif args[0] == ("up") or args[0] == ("u") or args[0] == ("subir") or args[0] == ("s"): scr.up(int(args[1]), ultimaLinea); mensajeOrden = scr.mensaje
            elif args[0] == ("edit") or args[0] == ("e"):
                contenidolinea = eliminar_prefijos(accion, "edit")
                contenidolinea = separarContenido_linea(contenidolinea)
                contenido[int(args[1])-1] = contenidolinea
                editado = True ; mensajeOrden = f"Línea {args[1]} editada"
            elif args[0] == ("insert") or args[0] == ("i"):
                if accion == ("insert") or accion == ("i"):
                    contenido = insertar_linea(contenido, ultimaLinea+1, "")
                    editado = True; mensajeOrden = f"Nueva línea insertada en posición {ultimaLinea+1}"
                else:
                    contenidolinea = eliminar_prefijos(accion, "insert")
                    contenidolinea = separarContenido_linea(contenidolinea)
                    contenido = insertar_linea(contenido, int(args[1]), contenidolinea)
                    editado = True; mensajeOrden = f"Línea insertada en posición {args[1]}"
            elif args[0] == ("remove") or args[0] == ("r"):
                contenido = eliminar_linea(contenido, args)
            else:
                mensajeOrden = "Comando inexistente"
        except:
            mensajeOrden = "Comando no válido"

### INICIALIZAR PROGRAMA
windowsBool = os_is_windows()

if os.path.abspath("").lower == "c:\\windows\\system32":
    direccion = os.path.expanduser("~")
else: direccion = os.path.abspath("")
os.chdir(direccion)

args = sys.argv
del args[0]
command = ' '.join(args)

salida = False

welcome()

### BUCLE PROGRAMA

while True: #Bucle menú principal
    
    if command.startswith("cpc"):
        args = shlex.split(command)
        try: 
            if args[1] == ("-new") or args[1] == ("-n"): new_command(args)
            elif args[1] == ("-open") or args[1] == ("-o"): open_editor(args)
            elif args[1] == ("-rename") or args[1] == ("-r"): rename_command(args)
            elif args[1] == ("-delete") or args[1] == ("-d"): delete_command(args)
            elif args[1] == ("-help") or args[1] == ("-d"): help_command()
            elif args[1] == ("-exit") or args[1] == ("-e"): salida = True
            else: print("Comando inexistente")

        except:
            if command == "cpc": welcome()
            else: print("Comando no válido")

    elif command.startswith("cd"):
        args = shlex.split(command)
        try:
            os.chdir(args[1])
            direccion = os.getcwd()
        except: print("El sistema no puede encontrar la ruta especificada")
    elif command == ("cls") or command == ("clear"): clear()
    else:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if windowsBool: print(stdout.decode('cp437')) 
        else: print(stdout.decode('utf-8'))

    if windowsBool: lineacomandos = "cpc "+direccion+">"
    else: lineacomandos = f'{os.getlogin()}@{socket.gethostname()} cpc {direccion}\n$ '   

    if salida: exit_command(); break    
    else: command = input(lineacomandos)

"""
fuciones para añadir posteriormente:
    abrir último archivo
    configuración de idioma
    configuración de terminal
    configuración persistente
    al abrir archivos, abrir en la última posición
    lista archivos recientes
    nuevo+abrir en un comando
    confirmar salir, guardar y salir
    columna de números más elegante
    copiar fácilmente
"""