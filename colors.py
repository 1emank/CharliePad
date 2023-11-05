class txt:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Regular:
    Black   = '\033[0;30m'
    Red     = '\033[0;31m'
    Green   = '\033[0;32m'
    Yellow  = '\033[0;33m'
    Blue    = '\033[0;34m'
    Purple  = '\033[0;35m'
    Cyan    = '\033[0;36m'
    White   = '\033[0;37m'

class Bold:
    Black   = '\033[1;30m'
    Red     = '\033[1;31m'
    Green   = '\033[1;32m'
    Yellow  = '\033[1;33m'
    Blue    = '\033[1;34m'
    Purple  = '\033[1;35m'
    Cyan    = '\033[1;36m'
    White   = '\033[1;37m'

class Underline:
    Black   = '\033[4;30m'
    Red     = '\033[4;31m'
    Green   = '\033[4;32m'
    Yellow  = '\033[4;33m'
    Blue    = '\033[4;34m'
    Purple  = '\033[4;35m'
    Cyan    = '\033[4;36m'
    White   = '\033[4;37m'

class Background:
    Black   = '\033[40m'
    Red     = '\033[41m'
    Green   = '\033[42m'
    Yellow  = '\033[43m'
    Blue    = '\033[44m'
    Purple  = '\033[45m'
    Cyan    = '\033[46m'
    White   = '\033[47m'

class High_Intensty:
    Black   = '\033[0;90m'
    Red     = '\033[0;91m'
    Green   = '\033[0;92m'
    Yellow  = '\033[0;93m'
    Blue    = '\033[0;94m'
    Purple  = '\033[0;95m'
    Cyan    = '\033[0;96m'
    White   = '\033[0;97m'

class Bold_High_Intensty:
    Black   = '\033[1;90m'
    Red     = '\033[1;91m'
    Green   = '\033[1;92m'
    Yellow  = '\033[1;93m'
    Blue    = '\033[1;94m'
    Purple  = '\033[1;95m'
    Cyan    = '\033[1;96m'
    White   = '\033[1;97m'

class High_Intensty_backgrounds:
    Black   = '\033[0;100m'
    Red     = '\033[0;101m'
    Green   = '\033[0;102m'
    Yellow  = '\033[0;103m'
    Blue    = '\033[0;104m'
    Purple  = '\033[0;105m'
    Cyan    = '\033[0;106m'
    White   = '\033[0;107m'

Reset = '\033[0m'

Clear = '\033[2J'

print(f'Colortest:\n{txt.FAIL}FAIL\n{txt.ENDC}ENDC\n{txt.HEADER}HEADER\n{txt.OKBLUE}OKBLUE\n{txt.OKCYAN}OKCYAN\n{txt.OKGREEN}OKGREEN\n{txt.UNDERLINE}UNDERLINE\n{txt.WARNING}WARNING')