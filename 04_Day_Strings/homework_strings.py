# 'Thirty', 'Days', 'Of', 'Python'
word_1 = 'thirty'
word_2 = 'days'
word_3 = 'of'
word_4 = 'python'
space = ' '
all_words = word_1 + space + word_2 + space + word_3 + space + word_4
print(all_words)

word_a = 'coding'
word_b = 'for'
word_c = 'all'
space = ' '
word_ABC = word_a + space + word_b + space + word_c
print(word_ABC)

company = word_ABC
print('value of company is ', company)
print('length of the vairable \"company\" is ', len(company))
print('uppercased look of variable \"company\" is ', company.upper())
print('lowercased look of variable \"company\" is ', company.lower())
print('capitalized look of variable \"company\" is ', company.capitalize())
print('titled look of variable \"company\" is ', company.title())
print('swapped case look of variable \"company\" is ', company.swapcase())
company_one = (company[0:1])
print('first letter of variable company is ', company_one)
print(amount of string \'coding\' in variable \"company\" is ', company.count('coding'))
print(company.index('coding'))
print(company.find('coding'))
print(company.rindex('coding'))
print(company.rfind('coding'))
print('look of variable \"company\" when substring \'coding\' is replaced by \'python\' is ', company.replace('coding', 'python'))

python_all = company.replace('coding', 'python')
python_everyone = python_all.replace('all', 'everyone')
print('value of variable \"python_all\" is ', python_all)
print('value of variable \"python_aeveryone\" is ', python_everyone)
set = company.split()
print(set)

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
list_companies = companies.split()
print('values in list of the companies are ', list_companies)
first_letter = company[0:1]
print('first letter of variable \"company\" is ', first_letter)
length = len(company)
print('length of the variable \"company\" is ', length)
last_letter = company[ length - 1]
print('last letter of variable \"company\" is ', last_letter)
tenth_letter = company[10 - 1]
print('10th letter of variable \"company\" is ', tenth_letter)

py4every1 = python_all
code4all =  word_ABC
print('value of py4every1 is ', py4every1)
print('value of code4all is ', code4all)
print('first occurance of letter \'c\' is at point ', code4all.index('c'))
print('first occurance of letter \'f\' is at point ', code4all.index('f'))
print('first occurance of letter \'i\' is at point ', code4all.rindex('i'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
print('first occurance of \"because\" in sentence is at point ', sentence.find('because'))
print('last occurance of \"because\" in sentence is at point ', sentence.rfind('because'))

because_len = int(len('because'))
print('length of because_len is ', because_len)
sliced_sentence = sentence[0:31] + sentence[49:]
print('when sliced \"because\" out of the sentence, it will becomes' ,sliced_sentence)
gone_sentence = sentence[31:48 + because_len]
print('words that were sliced off are', gone_sentence)
print(sliced_sentence)




print('company starts with coding is ', company.startswith('Coding'))
print('company starts with coding is ', company.startswith('coding'))
ploblem = '   Coding For All      '
splited = ploblem.split()
print(splited)
space = ' '
new_sentence = space.join(splited)
print(new_sentence)


30DaysOfPython
thirty_days_of_python

print('valid 30DaysOfPython is ', '30DaysOfPython'.isidentifier())
print('valid thirty_days_of_python is ','thirty_days_of_python'.isidentifier())
python_lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
str_python_lib = " ".join(python_lib)
print('list of python libraries were merged into one string and value is currently ', str_python_lib)

Z = "I am enjoying this challenge."
X = "I just wonder what is next."
Y = Z + '\n' + X



#Name      Age     Country   City
#Asabeneh  250     Finland   Helsinki
question_1 = ['name', 'age', 'country', 'city']
question_2 = ['asabeneh', '250', 'finland', 'helsinki']

# 1. Calculate the maximum width needed for each column
column_widths = [max(len(q1), len(q2)) for q1, q2 in zip(question_1, question_2)]

# 2. Build each line by padding words to the column width
# .ljust(width) adds spaces to the right of a string to make it a certain width
question_1x = '  '.join([word.ljust(width) for word, width in zip(question_1, column_widths)])
question_2x = '  '.join([word.ljust(width) for word, width in zip(question_2, column_widths)])

# 3. Print the final, aligned result
print(question_1x)
print(question_2x)




#I GIVE UP SO THIS IS AI gemini 2.5 pro




