import font

class numeric_hpbar:
  name = 'Numeric'
  def display(entity):
    if entity.hp > (2 * entity.maxhp / 3):
      return 'Health: ' + str(entity.hp) + ' / ' + str(entity.maxhp)
    elif entity.hp > (entity.maxhp / 3):
      return 'Health: ' + font.yellow(entity.hp) + ' / ' + str(entity.maxhp)
    else:
      return 'Health: ' + font.red(entity.hp) + ' / ' + str(entity.maxhp)

class modern_hpbar:
  name = 'Modern'
  def display(entity):
    return_str = "  "
    if entity.hp > (2 * entity.maxhp / 3):
      color = font.bold_green
    elif entity.hp > (entity.maxhp / 3):
      color = font.bold_yellow
    else:
      color = font.bold_red

    for num in range(entity.hp):
        return_str += color('▱ ')
    for num in range(entity.maxhp - entity.hp):
      return_str += font.grey('▱ ')
    return return_str + ""

class classic_hpbar:
  name = "Classic"
  def display(entity):
    return_str = "  "
    if entity.hp > (2 * entity.maxhp / 3):
      color = font.green
    elif entity.hp > (entity.maxhp / 3):
      color = font.yellow
    else:
      color = font.red

    for num in range(entity.hp):
        return_str += color('█')
    for num in range(entity.maxhp - entity.hp):
      return_str += font.grey('▒')
    return return_str + ""