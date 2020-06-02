import random
import swords
import rarity
import font
import items
import quests
import moves
import abc

class mob:
  def __init__(self, name, lvl, weapon, maxhp, df, agi, accur):
    self.maxhp = maxhp
    self.hp = maxhp
    self.name = name
    self.weapon = weapon
    self.lvl = lvl
    self.df = df
    self.agi = agi
    self.accur = accur
    self.blocking = False
    self.poisoned = False
    self.can_attack = True
    self.chance_to_hit = 1.0

  @abc.abstractmethod
  def atk(self):
    pass
  
  def basic_loot(self, plr, xpgain, coins):
    print(font.bold_yellow('+ ' + str(xpgain) + ' XP'))
    plr.gainxp(xpgain)
    print(' -- Loot -- ')
    print(str(coins) + ' coins')
    plr.money += coins

class dummy(mob):
  def __init__(self):
    super().__init__('Dummy', 0, swords.none, random.randint(5, 6), 0, 0, 0)

  moves = {
    1: moves.none
  }

  def atk(self):
    return 0

class goblin(mob):
  def __init__(self):
    super().__init__('Goblin', 1, swords.goblin_shiv, 4, 0, random.randint(5, 6), 1.0)

  # In battle, a random int is rolled and the associated move is produced.
  moves = {
      1: moves.opp_attack,
      2: moves.opp_poisoning_strike
  }

  def atk(self):
    return 1

  def loot(self, plr):
    self.basic_loot(plr, 20, coins = random.randint(2,3))
    if quests.proof_of_worth in plr.quests:
      print(items.goblin_head.name)
      plr.inventory[items.goblin_head] += 1
    # 40% chance to drop goblin shiv
    if random.random() < 0.4 and (swords.goblin_shiv not in plr.weapons):
      print(swords.goblin_shiv.name)
      plr.receive_sword(swords.goblin_shiv)
    input()

class crog_bruiser(mob):
  def __init__(self):
    self.lvl = random.randint(3,4)
    super().__init__('Crog Bruiser', self.lvl, swords.bruiser_battleaxe, random.randint(7, 8) + self.lvl, self.lvl, 5, 1.0)

  moves = {
      1: moves.opp_attack
  }

  def loot(self, plr):
    self.basic_loot(plr, 30 + 5 * self.lvl, 8 + self.lvl)
    # 40% chance to drop blunt mace
    if random.random() < 0.4 and (swords.bruiser_battleaxe not in plr.weapons):
      print(swords.bruiser_battleaxe.name)
      plr.receive_sword(swords.bruiser_battleaxe)
    input()

  def atk(self):
    return self.weapon.stats['Damage'] + self.lvl