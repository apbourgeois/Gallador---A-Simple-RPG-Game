import font

def none(opponent, plr):
  print(opponent.name + " doesn't know what to do.")

def plr_attack(opponent, plr):
  if opponent.df >= plr.atk():
    dmg = 1
  else:
    dmg = plr.atk() - opponent.df
    print('\nYou attack %s and do %s damage!' % (opponent.name, font.bold_green(str(dmg))))
    opponent.hp -= dmg

def opp_attack(opponent, plr):
  if plr.df >= opponent.atk():
    dmg = 1
  else:
    dmg = opponent.atk() - plr.df
  print('Your opponent attacks you. %s hp\n' % (font.bold_red('-' + str(dmg))))
  plr.hp -= opponent.atk()

def plr_poisoning_strike(opponent, plr):
  print('\nYou attack %s and do %s damage! Your opponent is now poisoned!' % (opponent.name, font.bold_green(str(plr.weapon.stats['Damage']))))
  opponent.hp -= plr.weapon.stats['Damage']
  opponent.poisoned = True

def opp_poisoning_strike(opponent, plr):
  print('Your opponent attacks you. %s hp. You are now poisoned!\n' % (font.bold_red('-' + str(opponent.weapon.stats['Damage']))))
  plr.hp -= opponent.weapon.stats['Damage']
  plr.poisoned = True

# Names of each move
name = {
    plr_attack: 'Attack',
    opp_attack: 'Attack',
    plr_poisoning_strike: 'Poisoning Strike',
    opp_poisoning_strike: 'Poisoning Strike'
  }