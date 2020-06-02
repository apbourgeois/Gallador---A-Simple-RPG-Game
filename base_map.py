import random
from mobs import goblin, crog_bruiser
import font
import combat
import quests
from PIL import Image
import math

class base_map():
  
  # min_y to max_y: 
  def __init__(self, name, img_name, has_fog, width, height):
    self.name = name
    self.tile_color = Image.open(img_name).load()
    self.tiles_revealed = not has_fog
    self.min_x = -math.trunc(width / 2)
    self.max_x = math.trunc(width / 2) + 1
    self.min_y = math.trunc(height / 2)
    self.max_y = -math.trunc(height / 2) - 1
  
  def print_legend(self):
    pass

  def print_map(self, plr):
    self.print_legend()
    print('      -- MAP: %s --' % str.upper(self.name))
    for y in range(self.min_y, self.max_y, -1):
      for x in range(self.min_x, self.max_x):
        coord = (str(x) + ',' + str(y))
        tile_pos = self.get_tile[coord]
        if coord == plr.pos():
          print('﴾﴿', end = '')
        elif tile_pos['explored']:
          print(tile_pos['object'].graphic, end='')
        else:
          print('  ', end='')
      print()
    input()

  def walking_display(self, plr):
    print()
    for y in range(self.min_y, self.max_y, -1):
      for x in range(self.min_x, self.max_x):
        coord = (str(x) + ',' + str(y))
        tile_pos = self.get_tile[coord]
        if coord == plr.pos():
          print(plr.emoji, end = '')
        elif tile_pos['explored']:
          print(tile_pos['object'].graphic, end='')
        else:
          print('  ', end='')
      print()

  ####################### get_tile ###########################
  get_tile = {}

  color_to_id = {}

  def init_map(self):
    for y in range(self.min_y, self.max_y, -1):
      for x in range(self.min_x, self.max_x):
        x_offset = math.trunc(self.width / 2)
        y_offset = math.trunc(self.height / 2)
        coord = str(x) + ',' + str(y)
        # color = self.tile_color[x + offset, y + offset]
        color = self.tile_color[x + x_offset, -y + y_offset]

        tile = self.color_to_id[color]
        self.get_tile[coord] = {'object':tile, 'explored':self.tiles_revealed}
        # print('Initialized position ' + coord + ' with color ' + str(color) + ' and tile ' + tile.graphic)

