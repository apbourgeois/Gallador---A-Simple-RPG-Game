import random
import swords
import font
import items
import moves
from outside_map import outside_map
from castle_map import castle_map
import replit
import ui
import time
import quests

class player:

  def __init__(self):
    self.name = 'Player'
    self.lvl = 1
    self.xp = 0
    self.reputation = 0
    self.maxhp = 6
    self.hp = self.maxhp
    self.df = 0
    self.agi = random.randint(4,5)
    self.weapon = swords.wooden_sword
    self.entity_accur = random.random()/10 + 0.7 # Accuracy is 70-80%
    self.result_accur = self.weapon.stats['Accuracy'] * self.entity_accur
    self.emoji = font.bold_yellow(':|')
    self.quests = []
    # self.completed_quests = []
    # TESTING
    # self.completed_quests = [quests.arrival_at_gallador]
    self.completed_quests = [quests.arrival_at_gallador, quests.learning_the_ropes]
    # self.completed_quests = [quests.arrival_at_gallador, quests.learning_the_ropes, quests.proof_of_worth]
    self.combat_actions = {
    }
    self.settings = { # Text speed: 2 (instant), 1 (fast), 0 (slow)
      'Text Speed': 2,
      'Health Bar Style': ui.modern_hpbar
    }

    # Misc
    self.exit_menu = False
    self.outside = outside_map()
    self.castle = castle_map()
    self.current_map = self.outside

    # Ability to switch moves' places?

    # Belongings
    self.money = 0
    self.weapons = [self.weapon]
    self.inventory = {
    }
    self.consumables = {
      items.health_potion: 5
    }

    # Combat
    self.blocking = False
    self.poisoned = False
    self.can_attack = True
    self.ran = False
    self.selected_action = False
    self.chance_to_hit = 1
    

    # Movement
    self.x = 0
    self.y = 0
    self.prev_x = 0
    self.prev_y = 0


    ############### LEVELING ################

  levelup_xp = {
    1: 30,
    2: 70,
    3: 110,
    4: 180,
    5: 300,
    6: 450,
    7: 650
  }

  # TESTING
  # levelup_xp = {
  #   1: 20,
  #   2: 20,
  #   3: 20,
  #   4: 20,
  #   5: 20,
  #   6: 20,
  #   7: 20,
  #   8: 20,
  #   9: 20,
  #   10: 20,
  #   11: 20,
  #   12: 20
  # }

  def levelup(self):
    new_lvl = self.lvl + 1
    new_hp = self.maxhp + 2
    old_atk = self.weapon.stats['Damage'] + self.lvl
    new_atk = self.weapon.stats['Damage'] + new_lvl
    new_df = self.df + random.randint(1,2)
    new_agi = self.agi + random.randint(1,2)

    print()
    print(" --- %s'S STATS --- " % str.capitalize(self.name))
    print('LVL: %d➔ %s' % (self.lvl, font.bold_green(new_lvl)))
    print('HP:  %d➔ %s' % (self.maxhp, font.bold_green(new_hp)))
    print('ATK: %d➔ %s' % (old_atk, font.bold_green(new_atk)))
    print('DEF: %d➔ %s' % (self.df, font.bold_green(new_df)))
    print('AGI: %d➔ %s' % (self.agi, font.bold_green(new_agi)))
    ''' Learning moves
    print('MOVES: ')
    for moveID in self.moves:
      print(str(moveID) + ' - [' + moves.name[self.moves[moveID]] + ']')
    '''
    self.lvl = new_lvl
    self.maxhp = new_hp
    self.hp = new_hp
    self.df = new_df
    self.agi = new_agi
    input()

  def gainxp(self, xpgain):
    self.xp += xpgain
    while self.xp > self.levelup_xp[self.lvl]:
      print(font.bold('You levelled up!'))
      self.xp -= self.levelup_xp[self.lvl]
      self.levelup()
      replit.clear()

  #################### MENUS #####################

  def show_inv(self, placeholder):
    print(' --- INVENTORY --- ')
    print('Money: %s coins' % str(self.money))
    for item in self.inventory:
        print('%s: %s' % (item.name, str(self.inventory[item])))
    for consumable in self.consumables:
        print('%s: %s' % (consumable.name, str(self.consumables[consumable])))
    for weapon in self.weapons:
      print(weapon.name)
    input()

  def show_stats(self, placeholder):
    print(" --- %s'S STATS --- " % str.upper(self.name))
    print('LVL: ' + str(self.lvl))
    print('HP: ' + str(self.hp))
    print('ATK: ' + str(self.atk()))
    print('DEF: ' + str(self.df))
    print('AGI: ' + str(self.agi))
    print('MOVES: ')
    for moveID in self.moves:
      print(str(moveID) + ' - [' + moves.name[self.moves[moveID]] + ']')
    print('WEAPON: ' + self.weapon.name + '\n')
    self.weapon.graphic()
    input()

  def atk(self):
    return self.weapon.stats['Damage'] + self.lvl

  def show_consumables(self):
    for consumable in self.consumables:
        print('%s - [%s]: %d' % (consumable.input_word, consumable.name, self.consumables[consumable]))

  def pos(self):
    return (str(self.x) + ',' + str(self.y))

  def receive_sword(self, sword):
    input()
    replit.clear()
    print(" --- %s --- \n" % sword.name)
    sword.graphic()
    print()
    for stat in sword.stats:
      if stat == 'Accuracy':
        print("%s: %s%%" % (stat, font.accuracy(sword.stats[stat])))
      else:
        print("%s: %s" % (stat, sword.stats[stat]))
    ans = input('\nWould you like to equip %s? (y/n)\n' % sword.name)
    while not(ans == 'y' or ans == 'n'):
      ans = input('Try typing y then enter to say yes, or n then enter to say no.\n')
    if ans == 'y':
      print('\nYou equipped %s!' % sword.name)
      self.weapon = sword
    else:
      print('\n%s has been added to your inventory.' % sword.name)
    if self.weapon == swords.goblin_shiv:
        self.learn_move(moves.plr_poisoning_strike)
    print()
    self.weapons.append(sword)

  ################## MOVES ######################
  moves = {
    '1': moves.plr_attack
  }

  def learn_move(self, move):
    print('\nYou learned %s!' % font.bold(moves.name[move]))
    self.moves[str(len(self.moves.keys()) + 1)] = move

  def initialize_combat_actions(self):
    self.can_attack = True
    self.ran = False
    self.selected_action = False

    self.combat_actions = {
      'run': self.run
    }

    for moveID in self.moves:
      self.combat_actions[moveID] = self.moves[moveID]
    for consumable in self.consumables:
      self.combat_actions[consumable.input_word] = consumable.use

  def run(self, placeholder):
    self.ran = True
    self.selected_action = True
  # This is what associates an input in combat (moveID) with a move. Moves are added as they are learned.

  def gain_rep(self, rep):
    print(font.reputation('You just gained ' + str(rep) + ' reputation!'))
    self.reputation += rep

    
  def sim_type(self, text):
    count = 0
    if self.settings["Text Speed"] == 2:
      for letter in text:
        print(letter, end = '', flush = True)
        if count == 2:
          time.sleep(0)
          count = 0
        count += 1
    elif self.settings["Text Speed"] == 1:
      for letter in text:
        print(letter, end = '', flush = True)
        if count == 2:
          time.sleep(0.03)
          count = 0
        count += 1
    else:
      for letter in text:
        print(letter, end = '', flush = True)
        time.sleep(0.04)