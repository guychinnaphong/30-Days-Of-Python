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

  
import string
from random import random, randint
def list_of_hexa_colors():
  hexa = list(string.digits + string.ascii_letters[0:6])
  amount = int(input('please enter amount of item in list of hex colours in number : '))
  hexa_list = ''.join([hexa[randint(0, len(hexa) - 1)] for _ in range(amount)])
  print(hexa_list)


import string
from random import random, randint
def list_of_rgb():
  rgb_list = []
  input_amount = int(input('please enter amount of rgb list you want to generate : '))
  for _ in range(input_amount):
    rgb_list.append(f'rgb{str([randint(0, 255) for _ in range(3)])}')
  print(rgb_list)

# หรือ

import string
from random import random, randint
def list_of_rgb():
  rgb_list = []
  input_amount = int(input('please enter amount of rgb list you want to generate : '))
  for _ in range(input_amount):
    r, g, b = (randint(0, 255) for _ in range(3))
    print([f'rgb({r}, {g}, {b})'])

#หรือ

import string
from random import random, randint
def list_of_rgb():
  input_amount = int(input('please enter amount of rgb list you want to generate : '))
  rgb_list = [f'rgb({randint(0, 255)}, {randint(0, 255)}, {randint(0, 255)})' for _ in range(input_amount)]
  print(rgb_list)



def generate_colors():
  input_amount = int(input('please enter amount of rgb_list or hexa_list you want to generate : '))
  input_hexa_amount = int(input('please enter amount of character you want in hexa color : '))
  hexa = list(string.digits + string.ascii_letters[0:6])
  whole_list = []
  for _ in range(input_amount):
    num = randint(1,2)
    if num == 1:
      hexa_color = ''.join(f'{hexa[randint(0, len(hexa) - 1)]}' for _ in range(input_hexa_amount))
      whole_list.append(f'hexa({hexa_color})')
    else:
      rgb_color = (f'rgb({randint(0, 255)}, {randint(0, 255)}, {randint(0, 255)})')
      whole_list.append((rgb_color))
  return whole_list


#input_rgb_amount = int(input('please enter amount of character you want in rgb color : '))          # USELESS
#rgb_color = (f'rgb({randint(0, 255)}, {randint(0, 255)}, {randint(0, 255)})' for _ in range(input_rgb_amount))






from random import random, randint
def shuffle_list(input_list):
  shuffled_list = []
  if not isinstance(input_list, list):
    print('please enter your input as a list and only a list')        # WRONG
  else:
    length = len(input_list)
    shuffled_list.append(input_list[randint(0, length - 1)] for _ in range(length))
    for i in shuffled_list:
      if shuffled_list.count(i) >= 2:
        (shuffled_list.remove(i) for _ in range(len(shuffled_list.count(i) - 1)))
    return shuffled_list


#from random import random, randint
#def shuffle_list(input_list):
 # if not isinstance(input_list, list):
   # print('please enter your input as a list and only a list')        # TRY TO SHUFFLE LIST USING SET
  #else:
   # set_input_list = set(input_list)
   # shuffled_list = [set_input_list]
  #return shuffled_list


#from random import random, randint
#def shuffle_list(input_list):
  #shuffled_list = []
  #if not isinstance(input_list, list):
    #print('please enter your input as a list and only a list')
  #else:
   # shuffled_list.append(input_list[randint(0, length - 1)] for _ in range(length * 2))        # wrong and too painful to fix
    #shuffled_list_clear = set(shuffled_list)
    #shuffled_list_new = list(shuffled_list_clear)
   # for i in shuffled_list_new:
     # if i in input_list == True:
       # return shuffled_list_new
     # else:
       # shuffled_list_new.insert(randint(0, len(shuffled_list) - 1), i)
    # return shuffled_list_new


import random

def shuffle_list(input_list):
    if not isinstance(input_list, list):
        print("please enter your input as a list and only a list")  #AI GENERATED WAY TOO LONG TO FIX
        return None
    shuffled = input_list[:]   # make a copy so original isn’t changed
    random.shuffle(shuffled)
    return shuffled

print(shuffle_list([1, 2, 3, 4, 5]))


# หรือ

import random

def shuffle_list(input_list):
    if not isinstance(input_list, list):
        print("please enter your input as a list and only a list")
        return None
    temp = input_list[:]   # copy
    shuffled = []
    while temp:
        idx = random.randint(0, len(temp) - 1)
        shuffled.append(temp.pop(idx))
    return shuffled

print(shuffle_list([1, 2, 3, 4, 5]))


# หรีอ

import random

def shuffle_list(input_list):
    if not isinstance(input_list, list):
        print("please enter your input as a list and only a list")
        return None
    return random.sample(input_list, len(input_list))

print(shuffle_list([1, 2, 3, 4, 5]))


