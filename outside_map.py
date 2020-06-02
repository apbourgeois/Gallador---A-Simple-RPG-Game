import random
from mobs import goblin, crog_bruiser
import font
import combat
import quests
from base_map import base_map

class outside_map(base_map):
  def __init__(self):
    self.name = 'Outside'
    self.img_name = "outside_map.png"
    self.has_fog = True
    self.width = 15
    self.height = 15
    super().__init__(self.name, self.img_name, self.has_fog, self.width, self.height)
    
  def print_legend():
    print('﴾﴿     You')
    print('▒▒     Goblin Zone')
    print('░░     Bruiser Zone')
    print('[]     Crog Watchtower')
    print('۩      Crog Batallion')
    print('▪────▪ Dungeon Entrance')
    print('██     Dungeon Wall')
    print('⌂⌂     Castle\n')

  ########################## tile classes ###########################


  class tile_castle:
    graphic = font.bold('⌂⌂')
    description = 'Castle'

    def step(plr):
      #plr.current_map = castle_map
      print('You step into the castle.')
      plr.current_map = plr.castle
      plr.x = 0
      plr.y = -9
      
  class tile_goblin75:
    graphic = font.green('▒▒')
    description = '75% goblin'

    def step(plr):
      if random.random() < 0.75:
        opponent = goblin()
        print('\nA %s is attacking!' % font.lvl_diff(plr, opponent, opponent.name))
        input('> ')
        combat.fight(opponent, plr)

  class tile_goblin100:
    graphic = font.green('▒▒')
    description = '100% goblin'

    def step(plr):
      opponent = goblin()
      print('\nA %s is attacking!' % font.lvl_diff(plr, opponent, opponent.name))
      input('> ')
      combat.fight(opponent, plr)

  class tile_bruiser100:
    graphic = font.cyan('░░')
    description = '100% crog bruiser'

    def step(plr):
      opponent = crog_bruiser()
      print('\nYou bumped into a %s!' % font.lvl_diff(plr, opponent, opponent.name))
      input()
      combat.fight(opponent, plr)

  class tile_bruiser75:
    graphic = font.cyan('░░')
    description = '75% crog bruiser'

    def step(plr):
      if random.random() < 0.75:
        opponent = crog_bruiser()
        print('\nYou bumped into a %s!' % font.lvl_diff(plr, opponent, opponent.name))
        input()
        combat.fight(opponent, plr)

  class tile_NE_tower:
    graphic = font.bold_grey('[]')
    description = 'NE Crog Tower'

    def step(plr):
      #plr.current_map = castle_map
      print('You step into the NE Crog Tower.')

  class tile_SE_tower:
    graphic = font.bold_grey('[]')
    description = 'SE Crog Tower'

    def step(plr):
      #plr.current_map = castle_map
      print('You step into the SE Crog Tower.')

  class tile_SW_tower:
    graphic = font.bold_grey('[]')
    description = 'SW Crog Tower'

    def step(plr):
      #plr.current_map = castle_map
      print('You step into the SW Crog Tower.')

  class tile_NW_tower:
    graphic = font.bold_grey('[]')
    description = 'NW Crog Tower'

    def step(plr):
      #plr.current_map = castle_map
      print('You step into the NW Crog Tower.')

  class tile_batallion:
    graphic = font.yellow('۩ ')
    description = 'Crog batallion'

    def step(plr):
      #plr.current_map = castle_map
      print('There is a Crog Batallion standing in front of the dungeon door. Are you ready to fight them?')

  class tile_wall:
    graphic = font.black('██')
    description = 'Dungeon wall'

  class tile_dungeon_door:
    graphic = '▪ '
    description = 'Dungeon door'

    def step(plr):
      print('You step into the dungeon.')


  ######################### get_tile ###########################

  get_tile = {}

  color_to_id = {
    (200, 200, 200): tile_castle,
    (0, 255, 0): tile_goblin75,
    (50, 200, 50): tile_goblin100,
    (0, 100, 100): tile_bruiser100,
    (0, 150, 150): tile_bruiser75,
    (50, 50, 50): tile_NE_tower,
    (51, 51, 51): tile_SE_tower,
    (52, 52, 52): tile_SW_tower,
    (53, 53, 53): tile_NW_tower,
    (250, 200, 0): tile_batallion,
    (0, 0, 0): tile_wall,
    (100, 100, 100): tile_dungeon_door
  }





''' COMPLETE map
print('████████████▪────▪████████████')
print('██[]░░░░░░░░۩ ۩ ۩ ░░░░░░░░[]██')
print('██░░░░░░░░░░░░░░░░░░░░░░░░░░██')
print('██░░░░░░░░░░░░░░░░░░░░░░░░░░██')
print('██░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░██')
print('██░░░░░░▒▒▒▒▒▒﴾﴿▒▒▒▒▒▒░░░░░░██')
print(' ▪۩ ░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░ ۩▪ ')
print(' │۩ ░░░░▒▒▒▒▒▒⌂⌂▒▒▒▒▒▒░░░░ ۩│ ')
print(' ▪۩ ░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░ ۩▪ ')
print('██░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░██')
print('██░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░██')
print('██░░░░░░░░░░░░░░░░░░░░░░░░░░██')
print('██░░░░░░░░░░░░░░░░░░░░░░░░░░██')
print('██[]░░░░░░░░۩ ۩ ۩ ░░░░░░░░[]██')
print('████████████▪────▪████████████')
'''


