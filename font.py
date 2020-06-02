import rarity

def text(font, text):
  return font + str(text) + default

default = '\033[0m'

'''
How to use custom font:
font.font_here(text here) returns a string with that font.
Example:
  print(font.bold_red('-2'))
'''
# Rarities
def rarity_grey(text):
  return rarity.grey + str(text) + default

def rarity_green(text):
  return rarity.green + str(text) + default

def rarity_blue(text):
  return rarity.blue + str(text) + default

def rarity_purple(text):
  return rarity.purple + str(text) + default

def rarity_orange(text):
  return rarity.orange + str(text) + default

def rarity_red(text):
  return rarity.red + str(text) + default

def rarity_yellow(text):
  return rarity.yellow + str(text) + default

def rarity_cyan(text):
  return rarity.cyan + str(text) + default

# Fonts
def bold(text):
  return '\033[1m' + str(text) + default

def grey(text):
  return '\033[90m' + str(text) + default

def bold_grey(text):
  return '\033[1;90m' + str(text) + default

def light_grey(text):
  return '\033[2m' + str(text) + default


def bold_light_grey(text):
  return '\033[1;2m' + str(text) + default

def black(text):
  return '\033[30m' + str(text) + default

def bold_black(text):
  return '\033[1;30m' + str(text) + default

def green(text):
  return '\033[32m' + str(text) + default

def bold_green(text):
  return '\033[1;32m' + str(text) + default

def yellow(text):
  return '\033[93m' + str(text) + default

def bold_yellow(text):
  return '\033[1;93m' + str(text) + default

def red(text):
  return '\033[91m' + str(text) + default

def bold_red(text):
  return '\033[1;91m' + str(text) + default

def cyan(text):
  return '\033[96m' + str(text) + default

def bold_cyan(text):
  return '\033[1;96m' + str(text) + default

# Misc

def person(text):
  return '\033[44;93m' + str(text) + default

    # For reputation gains
def reputation(text):
  return '\033[1;94m' + str(text) + default

    # Returns a text color depending on lvl diff
def lvl_diff(plr, opponent, text): 
  if opponent.lvl > plr.lvl + 1:
    return red(text)
  elif opponent.lvl < plr.lvl - 1:
    return green(text)
  else:
    return yellow(text)

def accuracy(value):
  if value > 0.7:
    return green(int(100*value))
  elif value > 0.3:
    return yellow(int(100*value))
  else:
    return red(int(100*value))

def custom(text):
  return '\033[40;2m' + str(text) + default