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


import string
from random import random, randint
character_list = list(string.ascii_letters + string.digits)
def user_id_gen_by_user():
  character = int(input('please enter amount of character you want in your user id : '))
  amount = int(input('please enter amount of id you want to generate'))
  for i in range(amount):
    user_id = [character_list[i] for i in range(character)]
  return user_id

  
  user_id = ''.join([character_list[randint(0, len(character_list) - 1)] for i in range(character)])
  six_user_id = [user_id for _ in range(6)]
  return six_user_id
