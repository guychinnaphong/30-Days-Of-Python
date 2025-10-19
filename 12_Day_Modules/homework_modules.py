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
  amount = int(input('please enter amount of id you want to generate : '))
  user_id_all = []
  for _ in range(amount):
    user_id = ''.join([character_list[randint(0, len(character_list) - 1)] for _ in range(character)])
    user_id_all.append(user_id)
  for i in user_id_all:
    print(i)



def rgb_color_gen():
  rgb_list = []
  for _ in range(3):
    rgb_list.append(randint(0, 255))
  print 'rgb({}, {}, {})'.format(rgb_list[0], rgb_list[1], rgb_list[2])


#def user_id_gen_by_user():
    #length = int(input("Please enter amount of characters you want in your user id: "))
    #user_ids = []
    #for _ in range(6):  # generate 6 different IDs
        #user_id = ''.join(random.choice(character_list) for _ in range(length))              #AI GENERATED FOR REFERENCE
        #user_ids.append(user_id)
    #return user_ids

  
