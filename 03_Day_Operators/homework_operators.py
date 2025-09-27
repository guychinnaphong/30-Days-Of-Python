radius = input('enter radius ')
radius = float(radius)
area_of_circle = 3.14*(radius ** 2)
print(area_of_circle)


age = 16
height = 172.5
complex = 25 - 100j

b = float(input('enter base: '))
h = float(input('enter height: '))
area = 0.5 * b * h
print("area of a circle is", area)

side_a = float(input('enter side a of triangle: '))
side_b = float(input('enter side b of triangle: '))
side_c = float(input('enter side c of triangle: '))
perimeter = side_a + side_b + side_c
print('the perimeter of the triangle is', perimeter)

length = float(input('enter length of triangle: '))
width = float(input('enter width of your triangle: '))
area = length * width
perimeter = 2*(length + width)
print('area of the rectangle is', area)
print('perimeter of the reactangle', perimeter)

radius = float(input('enter the radius of the circle: '))
area = 3.14 * (radius * radius)
circumference = 2 * (3.14 * radius)
print('area of the circle is', area)
print('circumference of the circle is', circumference)

a = len('python')
b = len('dragon')
a != b

for i in a, b:
  'on' in i

sentence = 'I hope this course is not full of jargon'
'jargon' in sentence

for i in a, b:
  truth = 'on' not in i
truth = 'true'
print(truth)

python = len('python')
A = float(python)
print(A)
B = str(python)
print(B)

even = float(input('enter your number: '))
check_even = even % 2 == 0
fact = bool(check_even)
print(fact)

floor = 7//3 == int(2.7)
print("\"product by doing floor divison of 7 and 3 is equal to converted integer of value 2.7: \"", ( bool(floor)))

number = '10'
check = (int(number)) == 10
print("\'10\' is equal to 10 = ", (bool(check)))
check = (int(number)) != 10
print("\'10\' is not equal to 10 = ", (bool(check)))

x = 2
y = 2
answer = x/y
print(answer)

x_1, x_2, y_1, y_2 = 2, 6, 2, 10
slope = (y_2 - y_1)/(x_2 - x_1)
Euclidean_distance = ((x_2 - x_1)**2 +(y_2 - y_1)**2)**0.5
print("slope is =", slope)
print("Euclidean distance is =", Euclidean_distance)

x_math = 1
x_cood = 2 * x_math - 0 
y_cood = 0 * 2 - 2
slope = 2
x = 2
y = 2
intercept = x/y
print(slope)
print(x_cood)
print(y_cood)
print(intercept)

x =  0
y = x**2 + 6*x + 9
print ('value of y when x is 0 is', y)
while 'true':
  x = x - 1
  y = x**2 + 6*x + 9
  if y == 0:
    print("x value when y = 0 is", x)
    print("y value when x is", x,"is", y)
    break

number = 9.8
check = 10
num_processed = int(number)
answer = print('converted integer of 9.8 is 10 =', bool(check == number))

hour = float(input('enter your hours: '))
rate = float(input('enter your rate per hour: '))
weekly_earned = hour * rate
print("your weekly earned will be: ",weekly_earned, " baht per week")

minutes = 60
hour = 60
hour_day = 24
month_day = 31
months_year = 12
year_user = float(input("enter the years you've lived to calculate it to seconds: "))
seconds_user = year_user * months_year * month_day * hour_day * hour * minutes
print("amount of seconds you had lived in your entire life is :", seconds_user)

1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125

def display_table():
    """
    Displays a table with numbers, their squares, and cubes.
    The table structure is: n, 1, n, n^2, n^3
    for n from 1 to 5.
    """
    for n in range(1, 6):
        # Calculate the values for each column
        col1 = n
        col2 = 1
        col3 = n
        col4 = n ** 2
        col5 = n ** 3

        # Print the row with appropriate spacing
        print(f"{col1} {col2} {col3} {col4} {col5}")

# Call the function to display the table
display_table()
