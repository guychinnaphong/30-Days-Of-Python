def add_two_numbers(num1, num2):
  num_sum = num1 + num2
  return num_sum
print(add_two_numbers(int(input('enter num1: ')), int(input('enter num2: '))))

def area_circle_calculator(radius):
  area = 3.14 * radius * radius
  message = f'area of the circle of with {radius} radius is {area}'
  return message
print(area_circle_calculator(int(input('please enter your number: '))))


def add_all_nums(*num):
  num_list = []
  reserve_num = []
  reserve_non_num = []
  non_num = 0
  for i in map(str, num):
    if i.isnumeric() == True:
      num_list.append(int(i))
      reserve_num.append(int(i))                                                        #UNFINISHED BECAUSE I CANT DO THIS ANYMORE
    else:
      non_num += 1
      num_list.append(i)
      reserve_non_num.append(i)
  print('\n ')
  print('sum of all input numbers are', sum(reserve_num))
  print(f'there are {len(num_list)} values in num_list and which {non_num} of them are not pure number')
  return 'statement above is output if error please check again'

print(add_all_nums(0, 1, 15, 67, 69, 41, 2552, 'brochato', 'pancake', 'banana','blackhawk rescue mission 5', 916))







def add_all_nums(*num):
    num_list = []
    reserve_num = []
    reserve_non_num = []
    non_num = 0

    for i in num:  # don't convert everything to str yet
        if isinstance(i, (int, float)):   # check if it's numeric
            num_list.append(i)
            reserve_num.append(i)
        else:
            non_num += 1
            num_list.append(i)
            reserve_non_num.append(i)

    print('sum of all input numbers are', sum(reserve_num))
    print(f'there are {len(num_list)} values in num_list and which {non_num} of them are not pure number')
    return num_list, non_num




def temp_convert(celsius = 0):
  if celsius != 0:
    fahrenheit = (celsius * 9/5) + 32
  elif celsius == 0:
    fahrenheit = ((9/5) + 32)
  return (f'{celsius} *C is equivelent to {fahrenheit} *F')
print(temp_convert(int(input('please enter number of temperature in celsius for conversion to fahrenheit: '))))






year_season = {
    'autumn' : ['september', 'october', 'november'],
    'winter' : ['december', 'january', 'february'],
    'spring' : ['march', 'april', 'may'],
    'summer' : ['june', 'july', 'august']
  }

def check_season(input_month):
  for season in year_season:
    for month in range(3):
      if year_season[season][month] == input_month:
        return season
  print('no bro')
  return None
  
print(check_season(input('please enter your selected month in a year : ').lower()))



def calculate_slope(x1, y1, x2, y2):
  if not all(isinstance(i, (int, float)) for i in (x1, y1, x2, y2)):
    return 'wrong'
  else:
    slope = (y2 - y1)/(x2 - x1)
  if slope == 0:
    return 'error, the answer is equal to 0'
  else:
    return f'slope of input values are {slope}'

calculate_slope(6, 5, 9, 1)


#หรือ

def calculate_slope(x1, y1, x2, y2):
  for i in (x1, y1, x2, y2):
    if not isinstance(i, (int, float)):
      return 'wrong'
  else:
    slope = (y2 - y1)/(x2 - x1)
  if slope == 0:
    return 'error, the answer is equal to 0'
  else:
    return f'slope of input values are {slope}'

calculate_slope(6, 5, 9, 1)




def solve_quadratic_eqn(a, b, c)
  x = (-b  ((b**2) - 4 * a * c)) / 2 * a        #skip because too complicated for beginner
  
  equation = (a * (x**2)) + (b * x) + c


test_list = ['hello', 'world', 'henlo', 'baka']
def print_list(input_list):
  if isinstance(input_list, list):
    for i in input_list:
      print(i)
  else:
    return 'be quiet bro...'


def reverse_list(list):
  reversed = []
  for i in range(len(list) - 1, - 1, -1):
    reversed.append(list[i])
  return reversed


test1 = ['baka', 'wawa', 'nega', 'knee guard']
def capitalize_list_item(input_list):
  capitalized_list = []
  if isinstance(input_list, list):
    for i in input_list:
      capitalized_list.append(i.capitalize())
  else:
    print('unable to capitalize')
  return capitalized_list

capitalize_list_item(test1)


