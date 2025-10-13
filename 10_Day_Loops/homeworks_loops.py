for i in range(11):
  print(i)
c = 0
while c < 10:
  c = c + 1
  print(c)
  # หรือ
while c in range(11):
  print(c)
  c = c + 1

c = 10
while c > 0:
  print(c)
  c = c - 1
  if c == 0:
    print(c)


hashtag = '#'
space = ' '
while len(hashtag and space) < 8:          ## WRONG
  print(hashtag + space)
  if len(hashtag and space) == 8:
    print('i hit 8')
  break



hashtag = '#'
space = ' '

for row in range(8):
    print((hashtag + space) * 8)      # CORRECT

หรือ

hashtag = '#'
space = ' '
rows = 0

while rows < 8:
    print(((hashtag + space) * 8) - ' ')          # CORRECT
    
    rows += 1

หรือ 

hashtag = '#'
rows = 0

while rows < 8:
    print(' '.join([hashtag] * 8))
    rows += 1


hashtag = '#'
while len(hashtag) < 8:
  print(hashtag)
  hashtag += '#'
    

a = 0
line = 0
while line < 11:
  print('{} x {} = {}'.format(a, a, a*a))
  a = a + 1
  line = line + 1


list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in list:
  print(i)

for i in range(100):
  if i % 2 != 0:
    pass
  else:
    print(i)

for i in range(100):
  if i % 2 == 0:
    pass
  else:
    print(i)






total = 0

for num in range(1, 101):  # goes from 1 to 100
    total += num

print('sum of all numbers is : ', total)


num = 0
list_even = []
list_odd = []
for num in range(0, 101):
  if num % 2 == 0:
    list_even.append(num)
  elif num % 2 == 1:
    list_odd.append(num)
print('sum of all odd numbers are: ', sum(list_odd))
print('sum of all even numbers are: ', sum(list_even))

