# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len('length of variable \'it_companies\' is ', it_companies))
it_companies.add('Twitter')
print('check : ', it_companies)
it_companies.update(['Nvidia', 'Notions', 'OpenAI', 'Anthropic'])
print(it_companies)
it_companies.remove('Facebook')
print(Facebook in it_companies)

# discard() method dont raise any error value, unlike remove() method

print('value of joined A set and B set are 'A.union(B))
print('value of intersected A set and B set are'A.intersection(B))
print('A is subset of B : ', A.issubset(B))
print('value of both A and B are disjointed : ', A.isdisjoint(B))
print(((A.union(B)).union(A)))
print('symmetric difference value of set A and set B are', (A.symmetric_difference(B)))
del A,B

age = [22, 19, 24, 25, 26, 24, 25, 24]
ages = set(age)
print('checking current status of variable age : ', ages)

string = """data type which were alphabet or alphanumeric. it has function on it's own which distinguish from set, tuple 
which all 3 may have mixed function, string can be formatted to due to it's purpose of saying something with meaning without 
being directly connected to codes for example. all these texts you're currently reading are a one single string...  but
this one is multiline string"""

list = """list are data type which use to dedicated to store same type of datas. list has it's own function also has similar
and sometime, same command use to do something with data like tuple and set for example function .remove(). data that is 
stored are in order and list can be modify, add, remove data into or from itself by using command"""

tuples = """tuples are type of data that you can not modify nor does anything to it. you can not change the data until you 
convert it into other type of data, data and be varie and usually will also be stored in order like list"""

sets = """sets are type of storing data which implicated from set theory in mathematic. it will be stored randomly without 
accordance to order but you will be able to do set theory operation with data in set, you can also use same .remove() command
from list on set data, the information can varie from string to number and other but you will be able to do set theory 
operation within that set"""

sentence = "I am a teacher and I love to inspire and teach people"
set_sentence = set(sentence.split())
print(set_sentence)
print('number of unique words that have been use in this sentence is : ', len(set_sentence))

