import replit
import font
import ui
import random
import items
import moves
from mobs import dummy

'''
Poison goes completely through armor. Lasts whole fight.
Poison I: 1 dmg per turn
'''

def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def do_poison(opponent, plr):
  if opponent.poisoned:
    opponent.hp -= 1
    print('%s loses %s health to poison!' % (opponent.name, font.bold_green('1')))
  if plr.poisoned:
    plr.hp -= 1
    print('You lose health to poison. %s hp' % font.bold_red('-1'))

def reset_bools(opponent, plr):
  plr.blocking = False
  plr.can_attack = True
  plr.selected_action = False
  opponent.blocking = False
  opponent.can_attack = True

def get_input(plr):
  while not plr.selected_action:
    moveID = input('\n∆ ')
    try:
      if is_number(moveID): # If it's a move, it is stored for later
        plr.selected_move = plr.combat_actions[moveID]
        plr.selected_action = True
      else: # If it's anything but a move, it is done now
        plr.combat_actions[moveID](plr) # Each combat move has its own validation
    except:
      print('Invalid command.')

def opponent_random_move(opponent, plr):
    rand = random.randint(1, len(opponent.moves.keys()))
    opponent.moves[rand](opponent, plr)

def do_attacks(opponent, plr):
  if opponent.agi > plr.agi:
      if opponent.can_attack:
        opponent_random_move(opponent, plr)
      if plr.hp > 0 and plr.can_attack:
        plr.selected_move(opponent, plr)
  else:
    if plr.can_attack:
      plr.selected_move(opponent, plr)
    if opponent.hp > 0 and opponent.can_attack:
      opponent_random_move(opponent, plr)

def battle_over(opponent, plr):
  if plr.hp <= 0:
    # Show final combat window
    plr.hp = 0 # Prevents showing -1
    combatscreen(opponent, plr)
    print()

    plr.hp = plr.maxhp
    plr.x = 0
    plr.y = 0
    print('You have been defeated! Perhaps you should have run...\n\nA local hurried you to the castle to be healed.')
    input()
    print("Local: Be careful out there %s. We can't afford to lose a fighter!" % plr.name)
    input()
  elif opponent.hp <= 0:
    opponent.hp = 0
    combatscreen(opponent, plr)
    print()
    print(plr.name + ' has defeated ' + opponent.name + '!')
    input()
    replit.clear()

    try:
      opponent.loot(plr)
    except AttributeError:
      pass
  plr.poisoned = False
  replit.clear()

def combatscreen(opponent, plr):
  replit.clear()
  font.bold(' -------------------- FIGHT --------------------\n')
  # Opponent
  print(font.lvl_diff(plr, opponent, ' -- ' + opponent.name + ' --'))
  print(plr.settings['Health Bar Style'].display(opponent))
  print('Level: ' + str(opponent.lvl))
  print('Weapon: ' + opponent.weapon.name)
  # print('Moves: ')
  # for moveID in opponent.moves:
  #   print('[' + opponent.moves[moveID] + ']')
  print()
  # Player
  print(font.green(' -- ' + plr.name + ' --'))
  print(plr.settings['Health Bar Style'].display(plr))
  print('Level: ' + str(plr.lvl))
  print('Weapon: ' + plr.weapon.name + '\n\n')
  #print('Your moves: ')
  for moveID in plr.moves:
    print(str(moveID) + ' - [' + moves.name[plr.moves[moveID]] + ']')
  print()
  plr.show_consumables()


##################### FIGHT ####################
def fight(opponent, plr):
  plr.initialize_combat_actions()
  while opponent.hp > 0 and plr.hp > 0:
    combatscreen(opponent, plr)
    get_input(plr)
    if plr.ran:
      break

    do_attacks(opponent, plr)
    do_poison(opponent, plr)
    reset_bools(opponent, plr)

    input()
  replit.clear()

  battle_over(opponent, plr)