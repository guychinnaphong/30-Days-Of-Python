inputs = int(input('enter your age: '))
print('you are old enough to drive') if inputs >18 else print('you need', (18  - inputs), 'more years to learn to drive.')

my_age = 16
your_age = int(input('please enter your age: '))
diff_age = abs(16 - your_age)
if your_age > my_age and diff_age != 1:
  print(f'you are {diff_age} years older than me')
if your_age > my_age and diff_age == 1:
  print(f'you are {diff_age} year older than me')
if your_age < my_age and diff_age != 1:
  print(f'you are {diff_age} younger than me')
if your_age < my_age and diff_age == 1:
  print(f'you are {diff_age} year younger than me')
if your_age == my_age:
  print(f'wassup twin you\'re the same age as me')

num1 = int(input('please enter your first number (num1): '))
num2 = int(input('please enter your second number (num2): '))
if num1 > num2:
  print('num1 is more than num2')
if num1 < num2:
  print('num1 is less than num2')
if num1 == num2:
  print('num1 and num2 is equal')

student_scores = int(input('please enter your scores: '))
if student_scores in range(0, 49):
  print('your grade: F')
if student_scores in range(50, 59):
  print('your grade: D')
if student_scores in range(60,69):
  print('your grade: C')
if student_scores in range(70,79):
  print('your grade: B')
if student_scores > 80:
  print('your grade: A')
if student_scores < 0:
  print('nigga stop stimming')

autumn = ['september', 'october', 'november']
winter = ['december', 'january', 'february']
spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']

print('january\n february \n march \n april \n may \n june \n july \n august \n september \n october \n november \n december')
input_month = (input('please enter your month out of all choices : ')).lower()
if input_month in autumn:
  print('season of %s is autumn' %(input_month))
elif input_month in winter:
  print('season of %s is winter' %(input_month))
elif input_month in spring:
  print('season of %s is spring' %(input_month))
elif input_month in summer:
  print('season of %s is spring' %(input_month))
else:
  print('nigga kill yourself')

fruits = ['banana', 'orange', 'mango', 'lemon']
input_fruit = input('please enter your desired fruit : ').lower()
if input_fruit in fruits:
  print('this fruit already exist in the list')
else:
  fruits.append(input_fruit)
  print('%s has been added to the list' %(input_fruit.upper()))
  print(fruits)

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
len_skills = len(person['skills'])
if 'skills' in person:
  if len(person['skills']) % 2 == 1:
    print(person['skills'][0:(len_skills) // 2] and person['skills'][len_skills // 2])
  elif len(person['skills']) % 2 == 0:
    print(person['skills'][((len_skills) // 2) - 1: -((len_skills // 2) - 1)])   

if 'skills' in person:
  if 'python'.capitalize() in person['skills']:
    print('Is there Python in skills section?:' ,'python'.capitalize() in person['skills'])
  else:
    print('there\'s no Python in skills section in dictionary')

if {'Javascript', 'React'}.issubset(person) and not {'Node', 'MongoDB', 'Python'}.intersection(person):
  print('He is a front end developer')
elif {'Node', 'Python', 'MongoDB'}.issubset(person) and not {'Javascript', 'React'}.intersection(person):
  print('He is a backend developer')
elif {'React', 'Node', 'MongoDB'}.issubset(person) and not {'Javascript', 'Python'}.intersection(person):
  Print('He is a fullstack developer')
elif None in person:
  print('He had none of the skills')
else:
  print('He had multiple skills varie in language')

if person['is_marred'] == True and person['country'] == 'Finland':
  print('%s %s lives in %s. He is %s' %(person['first_name'], person['last_name'], person['country'], 'is married.'))
