print('----------------------------Sort() and Sorted()------------------------------')
print('')

my_list = [1,5,3,7,2]
my_dict = {'car':4,'dog':2,'add':3,'bee':1}
my_tuple = ('d','c','e','a','b')
my_string = 'python'
print(my_list,'original')
print(my_list.sort()) #does not print
print(my_list,'new')#does print

print(my_list,'original')
print(sorted(my_list)) #creates a new list with no variable
print(my_list,'new')

print(my_tuple,'original')
print(sorted(my_tuple)) #creates a new list with no variable not a tuple
print(my_tuple,'new')

print(my_string,'original')
print(sorted(my_string)) #creates a new list with no variable not a string
print(my_string,'new')

print(my_dict,'original')
print(sorted(my_dict)) #creates a new list with just the strings
print(my_dict,'new')
print('')
print(my_dict,'original')
print(sorted(my_dict.items())) #creates a new list with string and numbers
print(my_dict,'new')
print('')
print(my_dict,'original')
print(sorted(my_dict.values())) #creates a new list just with the numbers
print(my_dict,'new')
print('')
print(my_dict,'original')
print(sorted(my_dict.values(), reverse = True)) #creates a new list and reverses the numbers
print(my_dict,'new')
print('')

print(my_list,'original')
print(list(reversed(my_list))) #creates a new list with no variable not a string
print(my_list,'new')
print('')

print(my_list,'original')
print(my_list[::-1]) #creates a new list with reversed numbers
print('')

my_list = [1,5,-3,7,-2]
my_llist=[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]

print(sorted(my_list, key = abs)) #sorted by absolute value

print(sorted(my_llist, key = lambda item :item[2])) #sorted by the item within the index inside the '[]'