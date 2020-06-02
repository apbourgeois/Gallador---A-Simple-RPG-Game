import font
from base_map import base_map
import quests
import items

class castle_map(base_map):
  def __init__(self):
    self.name = 'Castle'
    self.img_name = "castle_map.png"
    self.has_fog = False
    self.width = 21
    self.height = 21
    super().__init__(self.name, self.img_name, self.has_fog, self.width, self.height)

  def print_legend():
    print('﴾﴿ You')
    print('██ Wall\n')
    print('╬╬ Floor\n')

  ########################## tile classes ###########################

  class tile_wall:
    graphic = font.light_grey('██')
    description = 'Wall'

  class tile_floor:
    graphic = font.bold_light_grey('╬╬')
    description = 'Floor'

  class tile_elric:
    graphic = '\033[44;93m' + '◄►' + '\033[0m'
    description = 'Elric, Master Warrior'

    def step(plr):
      if quests.proof_of_worth in plr.quests:
        try:
          if plr.inventory[items.goblin_head] > 4:
            quests.proof_of_worth.hand_in(plr)
        except KeyError:
          pass
            

  class tile_npc:
    graphic = font.person('◄►')
    description = 'Person'
  
  class tile_fountain:
    graphic = font.rarity_blue('██')

  class tile_door:
    graphic = font.grey('██')

    def step(plr):
      print('You step outside.')
      plr.current_map = plr.outside
      plr.x = 0
      plr.y = 0

  class tile_empty:
    graphic = ('  ')

  ################################ get_tile ###########################

  get_tile = {}

  color_to_id = {
    (0, 0, 0): tile_wall,
    (255, 255, 255): tile_floor,
    (255, 225, 100): tile_npc,
    (75, 75, 75): tile_elric,
    (0, 0, 255): tile_fountain,
    (100, 100, 100): tile_door,
    (0, 255, 0): tile_empty
  }

