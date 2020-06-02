import quests

class npc:
  def __init__(self, name, quests):
    self.name = name
    self.quests = quests

class guard(npc):
  self = npc('Guard', [quests.warrior.warrior_first_quest])