'''
Functions:
Inv - open inventory
Save - save game to a text file
n, s, w, or e - walk in that direction and show coord
'''


class prompts:

  def walkprompt():
    print('Your coordinates are (%s, %s).' % (str(plr.x), str(plr.y)))
  print('Where to? (n, s, w, or e)')

  entry = input()
  if entry == 'n':
    plr.y += 1
  elif entry == 's':
    plr.y -= 1
  elif entry == 'w':
    plr.x -= 1
  elif entry == 'e':
    plr.x += 1
  
  
  # map.checkpos(plr.x, plr.y)
  # if no opponents
  walkprompt()