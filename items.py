import rarity
import font

class goblin_head:
  rarity = rarity.green
  name = font.text(rarity, 'Goblin Head')
  #usable_in_combat = False

class health_potion:
  input_word = 'hp'
  name = 'Health Potion'
  #usable_in_combat = True

  def use(user):
    if user.consumables[health_potion] > 0:
      if user.hp == user.maxhp:
        print('You are already at full health!')
      else:
        gain = round((3/4) * user.maxhp)
        if user.hp + gain > user.maxhp:
          gain = user.maxhp - user.hp
        print('You used a health potion. %s hp!' % font.bold_green('+' + str(gain)))
        user.hp += gain
        user.selected_action = True
        user.consumables[health_potion] -= 1
        user.can_attack = False
    else:
      print("You don't have any health potions...")