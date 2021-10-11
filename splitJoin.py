print('------------------Split---------------------')
print('')

# msg ='Welcome to Python 101: Split and Join'
# csv = 'Eric,John,Michael,Terry,Graham'
# friends_list = ['Eric','John','Michael','Terry','Graham']

# print(msg.split()) #changes a string into a list
# print(csv.split(','))#changes a string into ta list by ','
# print(' '.join(friends_list)) #changes a list into a string with a 'space' between
# print(msg.replace(' ', '-')) #this replaces the "spaces" to '-'

# csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
# friends_list = ['Exercise: fill me with names']
# # print(friends_list)
# csv=csv.replace(';',',')
# csv=csv.replace(':',',')
# print(csv)
# friends_list=csv.split(',')
# print(friends_list)
# # changes 'Eric,John,Michael,Terry,Graham:TerryG;Brian' to ['Eric', 'John', 'Michael', 'Terry', 'Graham', 'TerryG', 'Brian']
# print('')
# print('------------------Tuples---------------------')
# print('lists that cannot be changed')

# friends = ['John','Michael','Terry','Eric','Graham']
# friends_tuple = ('John','Michael','Terry','Eric','Graham')
# #you cant split or append or anything to these with a'()' instead of '[]'

# print('')
# print('------------------Sets---------------------')
# print('')

# friends = ['John','Michael','Terry','Eric','Graham']
# friends_tuple = ('John','Michael','Terry','Eric','Graham')
# friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}

# # are faster somehow and they do not print duplicates in the set the second 'Eric' will not print
# my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}
# print(friends_set.intersection(my_friends_set)) #who is in both sets?
# print(friends_set.difference(my_friends_set)) #who is NOT in both?
# print(friends_set.union(my_friends_set))#put both together with no repeats

# empty_list=[]
# empty_tuple=()
# empty_set=set()

print('')
print('------------------Sets Exercise---------------------')
print('')
friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

#1
print('Eric' in friends and 'John' in friends)

#2
print(friends.union(my_friends))

#3
print(friends.intersection(my_friends))

#4
print(friends-my_friends)

#5
print((my_friends.difference(friends)).union(friends.difference(my_friends)))

#6
print(set(cars))