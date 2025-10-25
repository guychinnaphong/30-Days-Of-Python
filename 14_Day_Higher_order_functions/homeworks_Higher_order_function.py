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
from functools import reduce

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
for country in countries:
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

land_filter = filter(lambda country: 'land' not in country, countries)
print(list(land_filter))


six_filter = filter(lambda country: len(country) != 6, countries)
print(list(six_filter))

six_more_filter = filter(lambda country: len(country) < 6, countries)
print(list(six_more_filter))

E_filter = filter(lambda country: not country.startswith('E'), countries)
print(list(E_filter))

mapped = list(map(lambda mapped_country: mapped_country.upper(), countries))
print(mapped)
filtered = list(filter(lambda filtered_country: 'A' in filtered_country, mapped))
print(filtered)
reduced = reduce(lambda a, b: a + ' ' + b, filtered)
print(reduced)




def get_string_lists(input_list):
    if isinstance(input_list, list):
        output_list = list(map(lambda input_element: str(input_element), input_list))
        return output_list
    return None


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_num_list = reduce(lambda a, b: a + b, numbers)
print(sum_of_num_list)


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
sentence = reduce(lambda a, b: f'{a}, {b}', countries[:-1])
sentence = f'{sentence} and {countries[-1]} are north European countries'
print(sentence)


countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

def categorize_countries():
    return list(filter(lambda country: country.endswith(('land', 'stan', 'ia', 'Islands')), countries))
    
#def categorize_countries():
   # return list(filter(lambda country: any(('land', 'stan', 'ia', 'Islands')) in country, countries))

def categorize_countries():
    substrings = ('land', 'stan', 'ia', 'Islands')
    return list(filter(lambda country: any(sub in country for sub in substrings), countries))

#import string
#def dict_letter():
   # letters_list = list(string.ascii_letters[:len(string.ascii_letters) // 2])
   # letter_dict = dict.fromkeys(letters_list, 0)
    #for letter in letters_list:
       # for country in countries:
           # if country.startswith(letter):
               # print(letter, country)
              # letter_dict[str(letter)] += 1
          #  else:
              #  letter_dict[letter] + 0
   # return letter_dict

import string

def dict_letter():
    letters_list = list(string.ascii_letters[:len(string.ascii_letters) // 2])
    letter_dict = dict.fromkeys(letters_list, 0)

    for country in countries:
        first_letter = country[0]   # get the first character
        if first_letter in letter_dict:
            letter_dict[first_letter] += 1

    return letter_dict
