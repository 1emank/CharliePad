#CMD: PROMPT
#PowerShell: PSMODULEPATH
#Git-bash: MSYSTEM
#Git-cmd: GIT_CMD
#Terminal (macOs): Apple_Terminal
#Bash: 'SHELL' termina en 'bash'

from os import name, environ
from platform import system

def active_terminal():
    apple = bool()
    if name == 'nt':
        if 'PROMPT' in environ: return 'CMD'
        elif 'MSYSTEM' in environ: return 'Bash'
        elif 'PSMODULEPATH' in environ: return 'PowerShell'
        else: return 'CMD'
    elif name == 'posix':
        try: apple = environ['TERM_PROGRAM'] == 'Apple_Terminal'
        except: pass

        if apple: return 'Terminal'
        elif 'GIT_CMD' in environ: return 'CMD'
        else: return 'Bash'
    else: return 'Bash'

    return terminal

def default_Terminal():
    so = system()
    if so == "Windows":
        return "CMD"
    elif so == "Linux":
        return "Bash"
    elif so == "Darwin":
        return "Terminal"
    else:
        return "Bash"