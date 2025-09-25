# Day 2: 30 days of python programming
first_name = "chinnaphong"
last_name = "roikaew"
full_name = first_name + " " + last_name
country = "thailand"
city = "bangkok"
age = 16
year = "highschool 11"
is_married = 'true'
is_true = 'true'
is_light_on = 'true'
is_married, is_true, is_light_on = 'false'

for i in (first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on):
  type(i)

len(first_name)
difference_in_length = len(first_name) - len(last_name)
num_one = 5
num_two = 4
num_sum = num_one + num_two
print(num_sum)
num_diff = num_two - num_one
print(num_diff)
num_whole = num_two * num_one
print(num_whole)
num_reduced = num_two / num_one
print(num_reduced)
remainder to num_two % num_one
print(remainder)
exponential = num_one ** num_two
print(exponential)
floor_product = num_one // num_two
print(floor_product)
area_of_circle = 3.14*30**2
print(area_of_circle)
circum_of_circle = 2*3.14*30
print(circum_of_circle)
radius = float(input("what is radius of circle for calculating area?"))
area = float(3.14 * (radius) **2.00)
print(f"area of a circle is {area}")


first_name = str(input("enter your first name"))
last_name = str(input("enter your last name"))
country = str(input("enter your country"))
age = str(input("enter your age"))
information_template = ["first name:", "last name:", "country:","age"]
user_information = [first_name, last_name, country, age]
print("first_name", first_name,  '\n',"last_name", last_name, '\n',"country", country,  '\n',"age", age)

help('keyword')
