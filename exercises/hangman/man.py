from const import BODY_PARTS
from const import GALLOWS
from time import sleep

class Man:
  def __init__(self):
    self.__body = list()

  def add_body_part(self):
    element = BODY_PARTS[len(self.__body)]
    self.__body.append(element)
    sleep(0.2)
    print("\n"*50)
    print(GALLOWS[len(self.__body)])
  
  def is_game_over(self):
    return len(self.__body) == 6



