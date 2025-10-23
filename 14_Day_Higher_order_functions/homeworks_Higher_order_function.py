map = ''' map function will take 2 value first one function and second one is iterable
(anything that you can do action multiple time like list) purpose if similar to for loop but this will
give you an answer directly without long code for an example you show 

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Let us apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']


you use "change_to_upper" function to change iterable in second slot to uppercase automatically. this way is easier
than using for loop or while loop but you'll need function for an input (also have list() because else it'll return 
ouput similar to zip file'''


filter = """ filter is function similar to map but it returns boolean which is useful when you want to filter something
out for a clean iterable output for an example

# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]

in an example we filtered out all the odd numbers but we cant just call it normally cuz you'll get something similar to
zip file so you do list() and that's a perfect ouput"""


reduce """ is the very same as other above but it returns only 1  value"""


"""difference between higher order functions, python closures and python decrorators
higher order function takes and return a function
python closures do the same but it remembers the variables
python decorators is mix of both but is being use to extend other function"""


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def call_upper(funct):
  return funct.upper()
make_list_upper = map(call_upper, countries)
print(list(make_list_upper))
  
def e_caller(funct):
  return funct if 'e' in funct or 'E' in funct else None
make_list_e = filter(e_caller, names)
print(list(make_list_e))

def minus_caller(x, y):
  return int(x) - int(y)
make_list_minus = reduce(minus_caller, numbers)
print(make_list_minus)


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for i country in countries:
  print(country)

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
i = 0
while i < len(names):
  print(names[i])
  i += 1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
  print(num)








countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

upper_countries = map(call_upper, countries)
print(list(upper_countries))

def square(x):
  return x**2

squared_numbers = map(square, numbers)
print(list(squared_numbers))

upper_names = map(call_upper, names)
print(list(upper_names))

land_filter = filter(lambda country: 'land' in country, countries)
print(list(land_filter))
