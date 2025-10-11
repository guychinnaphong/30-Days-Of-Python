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
