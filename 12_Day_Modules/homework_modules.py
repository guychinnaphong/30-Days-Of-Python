import string
from random import random, randint
character_list = []
for i in string.ascii_letters:
  character_list.append(i)
for i in string.digits:
  character_list.append(i)
character_list = set(character_list)
character_list = list(character_list)
def random_user_id():
  numbers = ''.join([character_list[randint(0, 62)] for i in range(6)])
  return numbers


