print('------------------Lists---------------------')
print('')

friends = ['John', 'Mike', 'Tracy', 'Lilly', 'Erin']

#print(friends[1],friends[4]) #prints what is in index 1 and 4
#print(friends[:4])
#print(len(friends)) #tells how long the list is
#print(friends.index('John'))
#print(friends.count('John'))

cars=[911, 545, 655, 9887,3]

# print(friends)
# cars.sort() #puts them in alpha order
# print(cars)
# friends.sort(reverse=True) #puts them in reverse alpha order
# print(friends)
# friends.reverse() #just puts them in reverse order
# print(friends)

# print(min(cars))
# print(max(cars))
# print(sum(cars))

# friends.append('Zach') #adds to the end
# print(friends)
# friends.insert(2,'Xion') #adds to index 2
# print(friends)
# friends[5]='Erin2'# replaces index 5
# print(friends)
# friends.extend(cars) #adds a nother list to the end of a list
# print(friends)
# friends.remove('Tracy')
# print(friends)
# print(friends.pop(-1)) #takes the last on the list out
# print(friends)
# # friends.clear() #takes everything out of the list
# print(friends)
# del friends[2]
print(friends)
new_friends=friends[:] # or new_friends = friends.copy() or new_friends = list(friends)
print(friends)
print(new_friends) #new list is created from the previous
