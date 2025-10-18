numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_number = [num for num in numbers if num <= 0]
print(negative_number)


list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten = [num for row1 in list_of_lists for row2 in row1 for num in row2]
print(flatten)

list = [
