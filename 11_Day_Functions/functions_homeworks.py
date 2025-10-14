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
      int(i)
      num_list.append(i)
      reserve_num.append(i)                                                        #UNFINISHED BECAUSE I CANT DO THIS ANYMORE
    else:
      non_num += 1
      num_list.append(i)
      reserve_non_num.append(i)
  
  print('sum of all input numbers are', sum(reserve_num))
  print(f'there are {len(num_list)} values in num_list and which {non_num} of them are not pure number')
  return num_list, non_num

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

print(add_all_nums(0, 1, 15, 67, 69, 41, 2552, 'brochato', 'pancake', 'banana', 'blackhawk rescue mission 5', 916))

