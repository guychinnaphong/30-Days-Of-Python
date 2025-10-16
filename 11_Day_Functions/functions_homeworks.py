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



def add_item(input_list, input_item):
  if isinstance(input_list, list):
    input_list.append(input_item)
    return input_list
  print('error, type of input is not list')
  return None


def remove_item(input_list, remove_item):
  if isinstance(input_list, list) and remove_item in input_list:
    input_list.remove(remove_item)
    return input_list
  elif remove_item not in input_list and isinstance(input_list, list) == True:
    print('input_removed item is not in the list')
    return None
  elif isinstance(input_list, list) != True and remove_item in input_list:
    print('error input type is not list')
    return None
  else:
    print('nigga what are you stimming')
    return None



def sum_of_numbers(input_range = 0):
  if type(input_range) != int:
    return 'nigga enter your fucking integer and not anything else'
  elif type(input_range) == int:
    int_list = []
    for i in range(input_range + 1):
      int_list.append(i)
    return f'sum of all number in range of {input_range} is {sum(int_list)}.'



def sum_of_odds(input_range = 0):
  if type(input_range) != int:
    return 'nigga enter your fucking integer and not anything else'
  elif type(input_range) == int:
    odd_list = []
    for i in range(input_range + 1):
      if i % 2 == 1:
        odd_list.append(i)
      else:
        odd_list.append(0)
    return f'sum of all odds number in range of {input_range} is {sum(odd_list)}.'




def sum_of_even(input_range = 0):
  if type(input_range) != int:
    return 'nigga enter your fucking integer and not anything else'
  elif type(input_range) == int:
    even_list = []
    for i in range(input_range + 1):
      if i % 2 == 0:
        even_list.append(i)
      else:
        continue         #odd_list.append(0)
    return f'sum of all odds number in range of {input_range} is {sum(even_list)}.'



def evens_and_odds(positive_int):
  if positive_int < 0:
    return 'we dont accept negative integer, only positive.'
  even_list = []
  odd_list = []
  for i in range(positive_int + 1):
    if i % 2 == 0:
      even_list.append(i)
    elif i % 2 == 1:
      odd_list.append(i)
  return f'numbers of odds are {len(odd_list)}.\nnumber of evens are {len(even_list)}.'

#หรือ 


def evens_and_odds(n):
    if n < 0:
        return 'we dont accept negative integer, only positive.'
    evens = (n // 2) + 1
    odds = n // 2 + (n % 2)
    return f'numbers of odds are {odds}. number of evens are {evens}.'



def factorial(input_int):
  factorial = 1
  if type(input_int) != int:
    return 'your input is not an integer'
  elif type(input_int) == int and input_int < 0:
    return 'function is not define (negative integer)'
  elif type(input_int) == int and input_int > 0:
    for i in range(1, input_int + 1):
      factorial *= i
  return factorial


  #หรือ


  def factorial_iterative(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 1
    
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact



  

  def is_empty(something):
    if isinstance(something, (int, float, str, bool)):
        raise ValueError("your input is undefined")              #AI because my brain cant handle for some reason

    try:
        return "EMPTY" if len(something) == 0 else "NOT EMPTY"
    except TypeError:
        raise TypeError("Unsupported type")




def mean(input_list):
  if not isinstance(input_list, list):
    raise ValueError("your input is not a list")
  elif isinstance(input_list, list):
    for i in input_list:
      return 'your input list is not all pure number' if not isinstance(input_list, (int, float)) else sum(input_list) / len(input_list)
    mean_output = (sum
