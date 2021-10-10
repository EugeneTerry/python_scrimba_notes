print('------------------Lists---------------------')
print('')

friends = ['John', 'Mike', 'Tracy', 'Lilly', 'Erin']

#print(friends[1],friends[4]) #prints what is in index 1 and 4
#print(friends[:4])
#print(len(friends)) #tells how long the list is
#print(friends.index('John'))
#print(friends.count('John'))

cars=[911, 545, 655, 9887,3]

print(friends)
cars.sort() #puts them in alpha order
print(cars)
friends.sort(reverse=True) #puts them in reverse alpha order
print(friends)
friends.reverse() #just puts them in reverse order
print(friends)

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
# print(friends)
# new_friends=friends[:] # or new_friends = friends.copy() or new_friends = list(friends)
# print(friends)
# print(new_friends) #new list is created from the previous

print('')
print('------------------Lists Exercise---------------------')
print('')

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
new_w1=sales_w1.copy()

sales_oneday = input('Add one day sale ')
sales_input =int(sales_oneday)
sales_w2.append(sales_input)
sales_w1.extend(sales_w2)
sales=sales_w1
best=(max(sales))*1.50
worst=(min(sales))*1.50
print(f'Best Day ${round(best, 3)}')
print(f'Worst Day ${round(worst, 3)}')
print(f'Week 1 sales = ${(sum(new_w1))*1.5} Week 2 sales = ${(sum(sales_w2))*1.5} Total Sales = ${(sum(sales))*1.5}')
