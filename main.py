import quests
import swords
from player import player
import replit
import combat
import font
import time
import outside_map

plr = player()

def wait():
  input('ꬲ ')

def learn(ability):
    plr.sim_type('You have just learned %s!' % ability)
    plr.moves.append(ability)

def reveal_surrounding_tiles(plr):
  for y in range(plr.y - 1, plr.y + 2):
    for x in range(plr.x - 1, plr.x + 2):
      coord = str(x) + ',' + str(y)
      try:
        plr.current_map.get_tile[coord]['explored'] = True
      except KeyError:
        pass
  

def walk_prompt():
  replit.clear()
  plr.current_map.walking_display(plr)
  print('\nYour coordinates are (%s). You can open the menu by typing %s.' % (plr.pos(), font.bold('menu')))
  print('Where would you like to go? (w, a, s, or d then enter)')

  entry = input('> ')

  if entry == 'w':
    plr.y += 1
  elif entry == 'a':
    plr.x -= 1
  elif entry == 's':
    plr.y -= 1
  elif entry == 'd':
    plr.x += 1
  elif entry == 'menu':
    menu()
  replit.clear()
  reveal_surrounding_tiles(plr)
  plr.current_map.walking_display(plr)
  try:
    plr.current_map.get_tile[plr.pos()]['object'].step(plr)
  except AttributeError:
    pass
  if plr.ran:
    plr.sim_type('You were able to run away!')
    plr.ran = False
    input()

  walk_prompt()

### MENU ###
def menu_exit(placeholder):
  plr.exit_menu = True

menu_options = {
  'inventory': plr.show_inv,
  'inv': plr.show_inv,
  'stats': plr.show_stats,
  'stat': plr.show_stats
}

def menu():
  plr.exit_menu = False
  while not plr.exit_menu:
    replit.clear()
    print('-- MENU --')
    print('[Inventory]\n[Stats]\n[Exit]\n')
    entry = input('> ').lower()
    if entry == '' or entry == 'exit':
      plr.exit_menu = True
    else:
      try: 
        replit.clear()
        menu_options[entry](plr)
      except KeyError:
        input('Invalid command.')
    replit.clear()
    

# def load(plr):
#   data = open('gallador_save_state.txt')
#   for line in data:
#     line = line.rstrip()
#     if line.startswith('Name:'):
#       plr.name = line[line.index(':') + 1 : len(line)]

# PROGRAM START

plr.castle.init_map()
plr.outside.init_map()
for y in range(-1, 2):
    for x in range(-1, 2):
      coord = str(x) + ',' + str(y)
      try:
        plr.outside.get_tile[coord]['explored'] = True
      except KeyError:
        pass

quests.arrival_at_gallador.assign(plr)
quests.learning_the_ropes.assign(plr)
quests.proof_of_worth.assign(plr)

walk_prompt()