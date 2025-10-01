list = []
list = ['dad', 'mom', 'older brother', 'younger sister']
print(len(list))
print(list[0],",", list[1],",", list[2], ",", list[3])
mixed_data_types = ['chinnaphong roikaew', 16, 172, 'not married', 'bangkok, thailand']
it_companies = ['facebook', 'google', 'microsoft', 'apple', 'IBM', 'oracle', 'amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0], it_companies[2], it_companies[3], it_companies[5])

del it_companies[5]
print(it_companies)

it_companies.append('palantir')
print(it_companies)

it_companies.insert(3, 'nvidia')
print(it_companies)

it_companies[1].capitalize()
'#; '.join(it_companies)
print(it_companies)

'nvidia' in it_companies
print(it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

new_companies = it_companies[3:7]
print(new_companies)

neo_companies = it_companies[0:3]
print(neo_companies)

liberal_company = it_companies[3:5]
print(liberal_company)

it_companies.pop(0)
len(it_companies)
it_companies.pop(3), it_companies.pop(4)
print(it_companies)
len(it_companies)
it_companies.pop(4)
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)


# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_end
print(full_stack)
full_stack.insert(5, 'python')
full_stack.insert(6, 'SQL')
print(full_stack)
