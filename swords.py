import rarity
import font


class none:

  item_rarity = rarity.grey
  name = font.text(item_rarity, 'None')
  poisoning = False

class wooden_sword:
  '''
        /| ________________
  O|===|* >_______________/
        \|                  
  '''
  def graphic():
    print('      /| ________________')
    print('O|===|* >_______________/')
    print('      \|')

  item_rarity = rarity.grey
  name = font.text(item_rarity, 'Wooden Sword')
  poisoning = False

  stats = {
    'Damage': 1,
    'Accuracy': 1.0
  }

class goblin_shiv:
  '''
             />
            /<
  O[/\//\\:(O)>===========================-
            \<
             \>
  '''
  def graphic():
    print(font.rarity_green('      />'))
    print(font.rarity_green('O[///(>================-'))
    print(font.rarity_green('      \>'))

  item_rarity = rarity.green
  name = font.text(item_rarity, 'Goblin Shiv')
  poisoning = True

  stats = {
    'Damage': 1,
    'Accuracy': 1.0,
    'Effect': font.text(rarity.grey, 'Poison I')
  }


class bruiser_battleaxe:
  '''
   . /\ .
 //`-||-'\\
(| -=||=- |)
 \\,-||-.//
   ' || '
     ||
     ||
     ||
     ||
     ||
     ()

  '''
  def graphic():
    print("   , /\ ,     ")
    print(" //'-||-'\\\   ")
    print('(| -=||=- |)  ')
    print(' \\\.-||-.//   ')
    print("   ` || `     ")
    print('     ||       ')
    print('     ||       ')
    print('     ||       ')
    print('     ||       ')
    print('     ||       ')
    print('     ()       ')

  item_rarity = rarity.green
  name = font.text(item_rarity, 'Bruiser Battleaxe')
  poisoning = False

  stats = {
    'Damage': 3,
    'Accuracy': 0.8
  }
