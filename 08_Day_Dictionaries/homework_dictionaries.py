dog = {}
print(f'type of variable \'dog\' is : {type(dog)}')
dog['name'] = 'kylo'
dog['colour'] = 'cream'
dog['breed'] = 'shiba inu'
dog['legs'] = 4
dog['age'] = 9
print(dog)
dog_copy = ((dog.copy()).clear())
print(dog_copy)


student = dict()
type = ['first name', 'last name', 'gender', 'age', 'martial status', 'skill', 'country', 'city', 'address']
detail = ['chinnaphong', 'roikaew', 'man', '16', 'single', 'none', 'thailand', 'bangkok', 'bangmod']
another = zip(type, detail)
for a, b in another:
  student[a] = b
  print(student)

หรือ

student = dict()
type = ['first name', 'last name', 'gender', 'age', 'martial status', 'skill', 'country', 'city', 'address']
detail = ['chinnaphong', 'roikaew', 'man', '16', 'single', 'none', 'thailand', 'bangkok', 'bangmod']
for i, a in enumerate(type):
  student[a] = detail[i]

student_len = len(student)
print(student_len)

