"""
ANSI escape codes.

Color codes are inside of the style:

fe: Bold -> Colors

(Dont forget to "Reset" the format)


Cursor control can be accesed directly.

For abbreviated sintax don't use: "import ansi_codes"

Use: "from ansi_codes import _short as c" (or the name that you prefer)
"""
class _short:
  class r:
      bk   = '\033[0;30m' # Black
      r    = '\033[0;31m' # Red
      g    = '\033[0;32m' # Green
      y    = '\033[0;33m' # Yellow
      bl   = '\033[0;34m' # Blue
      p    = '\033[0;35m' # Purple
      c    = '\033[0;36m' # Cyan
      w    = '\033[0;37m' # White

  class b:
      bk   = '\033[1;30m' # Black
      r    = '\033[1;31m' # Red
      g    = '\033[1;32m' # Green
      y    = '\033[1;33m' # Yellow
      bl   = '\033[1;34m' # Blue
      p    = '\033[1;35m' # Purple
      c    = '\033[1;36m' # Cyan
      w    = '\033[1;37m' # White

  class u:
      bk   = '\033[4;30m' # Black
      r    = '\033[4;31m' # Red
      g    = '\033[4;32m' # Green
      y    = '\033[4;33m' # Yellow
      bl   = '\033[4;34m' # Blue
      p    = '\033[4;35m' # Purple
      c    = '\033[4;36m' # Cyan
      w    = '\033[4;37m' # White

  class bg:
      bk   = '\033[40m' # Black
      r    = '\033[41m' # Red
      g    = '\033[42m' # Green
      y    = '\033[43m' # Yellow
      bl   = '\033[44m' # Blue
      p    = '\033[45m' # Purple
      c    = '\033[46m' # Cyan
      w    = '\033[47m' # White

  class hi:
      bk   = '\033[0;90m' # Black
      r    = '\033[0;91m' # Red
      g    = '\033[0;92m' # Green
      y    = '\033[0;93m' # Yellow
      bl   = '\033[0;94m' # Blue
      p    = '\033[0;95m' # Purple
      c    = '\033[0;96m' # Cyan
      w    = '\033[0;97m' # White

  class bhi:
      bk   = '\033[1;90m' # Black
      r    = '\033[1;91m' # Red
      g    = '\033[1;92m' # Green
      y    = '\033[1;93m' # Yellow
      bl   = '\033[1;94m' # Blue
      p    = '\033[1;95m' # Purple
      c    = '\033[1;96m' # Cyan
      w    = '\033[1;97m' # White

  class hibg:
      bk   = '\033[0;100m' # Black
      r    = '\033[0;101m' # Red
      g    = '\033[0;102m' # Green
      y    = '\033[0;103m' # Yellow
      bl   = '\033[0;104m' # Blue
      p    = '\033[0;105m' # Purple
      c    = '\033[0;106m' # Cyan
      w    = '\033[0;107m' # White

  def pos(L, C):
      #Puts the cursor in Line L, and Column C
      return f'\033[{L};{C}f'

  def pos_b(L, C):
      #Puts the cursor in Line L, and Column C (if the regular pos doesn't work)
      return f'\033[{L};{C}H'

  def up(N):
      #Move the cursor up N lines:
      return f'\033[{N}A'

  def dn(N):
      #Move the cursor up N lines:
      return f'\033[{N}B'

  def fd(N):
      #Move the cursor forward N columns:  
      return f'\033[{N}C'

  def bd(N):
      #Move the cursor backward N columns:
      return f'\033[{N}D'

  res = '\033[0m' # Reset format

  cl = '\033[2J' # Clear the screen and move cursor to 0, 0

  el = '\033[K' # Erase from cursor to end of line

  s_pos = '\033[s' # Save cursor position:

  r_pos = '\033[u' # Restore cursor position:

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

def position(L, C):
    #Puts the cursor in Line L, and Column C
    return f'\033[{L};{C}f'

def position_alt(L, C):
    #Puts the cursor in Line L, and Column C
    return f'\033[{L};{C}H'

def up(N):
    #Move the cursor up N lines:
    return f'\033[{N}A'

def down(N):
    #Move the cursor up N lines:
    return f'\033[{N}B'

def forward(N):
    #Move the cursor forward N columns:  
    return f'\033[{N}C'

def backward(N):
    #Move the cursor backward N columns:
    return f'\033[{N}D'

Reset = '\033[0m' # Reset format

Clear = '\033[2J' # Clear the screen and move cursor to 0, 0

Erase_toLineEnd = '\033[K' # Erase from cursor to end of line

Save_position = '\033[s' # Save cursor position:

Restore_position = '\033[u' # Restore cursor position:
