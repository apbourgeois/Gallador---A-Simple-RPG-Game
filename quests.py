from abc import ABC, abstractmethod
import items
import font
import swords
import combat
import mobs
import replit

def wait():
  input('ꬲ ')

class quest(ABC):
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.completed = False
    self.assign_text = ''
  
  @abstractmethod
  def turn_in(self, plr):
    pass

  @staticmethod
  def assign(quest, plr):
    print(quest.assign_text)
    wait()
    print('You just received the quest: ' + quest.name)
    plr.quests.append(quest)
    wait()



class arrival_at_gallador(quest):
  name = "Arrival at Gallador"
  description = "You just arrived at the kingdom of Gallador. A guide will send you to your trainer for your first quest."

  def assign(plr):
    if arrival_at_gallador in plr.completed_quests:
      pass
    else:
      plr.quests.append(arrival_at_gallador)
      plr.sim_type('Guard: Greetings, traveller. What is your name?\n')
      plr.name = input('> ')
      plr.sim_type('\nWelcome to the kingdom of Gallador, ' + plr.name + '. ')
      plr.sim_type('If you would like to reside here, you must learn a class and help uphold this city. \n')
      plr.sim_type('We are in dire need of help, because the Crog have surrounded us with settlements of their own.\n')
      print('[Press enter to continue]\n')
      wait()

      plr.sim_type('We have trainers here who can teach you to become a warrior, mage, or archer. Which would you like to become?\n')
      cl = input('> ')
      while not cl == 'warrior':
        print('\nThe only class currently available is warrior. Please type warrior.')
        cl = input('> ')
      if str.lower(cl) == 'warrior':
        plr.sim_type('\nVery well. I will send you to Elric to begin your training. He is in the grey armor, at the northeast section of this castle.') # Player is in front of throne and has to find Elric
        wait()
        arrival_at_gallador.hand_in(plr)

  def hand_in(plr):
    plr.sim_type(font.green('You completed the quest: Arrival at Gallador\n'))
    plr.quests.remove(arrival_at_gallador)
    plr.completed_quests.append(arrival_at_gallador)
    plr.gain_rep(5)
    wait()



class learning_the_ropes(quest):

  name = 'Learning the ropes'
  description = 'Test your sword skills on a dummy.'

  def assign(plr):
    if learning_the_ropes in plr.completed_quests:
      pass
    else:
      plr.quests.append(learning_the_ropes)

      plr.sim_type('\nElric: Pleased to see a new member. I will give you this wooden sword to get started.')
      wait()

      print("You've just received %s!\n" % swords.wooden_sword.name)
      swords.wooden_sword.graphic()
      print("\n --- %s --- " % swords.wooden_sword.name)
      print("Damage: 1")
      wait()

      plr.sim_type('Your first task is to attack this dummy. Give it a try.')
      wait()
      combat.fight(mobs.dummy(), plr)

      plr.sim_type('Elric: Well done %s. Your form is good, so I am assuming you have held a sword before.\n' % plr.name)

      learning_the_ropes.hand_in(plr)

  def hand_in(plr):
    plr.sim_type(font.green('You completed the quest: Learning the Ropes\n'))
    plr.quests.remove(learning_the_ropes)
    plr.completed_quests.append(learning_the_ropes)
    plr.gain_rep(5)
    wait()
    print("When you gain reputation at Gallador, you are entitled to basic weapons. You can come see me at any time when you have gained enough reputation for your next weapon.")
    wait()



class proof_of_worth(quest):
  def __init__(self, name, description):
    self.name = "Proof of Worth"

  def assign(plr):
    if proof_of_worth in plr.completed_quests:
      pass
    else:
      print('I am confident that you are able to kill the goblins which roam around, who serve as scouts for the Crog. Take your wooden sword and slay five of the wretched things. Take their heads and put them into this bag, then bring them back to me.')
      wait()
      print('Stay near the castle. Be careful venturing any farther than 3 units from it until you are stronger, or your journey might come to a sudden end. When you have the four heads, come back to see me at the castle, whose coordinates are (0, 0).')
      wait()
      print('You just received the quest: Proof of Worth')
      plr.quests.append(proof_of_worth)
      plr.inventory[items.goblin_head] = 0
      wait()
      print('You received %s! You can open it by typing %s then %s at any time on your journey.' % (font.rarity_grey('Cotton Bag'), font.bold('menu'), font.bold('inv')))
      wait()

      plr.sim_type('You step outside, past the shops and homes of Gallador, and take a look around. Beautiful rolling hills cover the landscape, but the air has a strange tint which does not let you see the horizon. There are faint sights of walls and dark towers in the distance.')
      wait()
      replit.clear()

  def hand_in(plr):
    plr.inventory.pop(items.goblin_head, None)
    plr.quests.remove(proof_of_worth)
    plr.completed_quests.append(proof_of_worth)
    plr.sim_type("Thank you for carrying out that task.")
    plr.sim_type(font.green('You completed the quest: Proof of Worth\n'))
    plr.gain_rep(5)
    wait()