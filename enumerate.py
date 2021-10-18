print('----------------------------Enumerate------------------------------')
print('')

friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']
# i = 1
# for friend in friends:
#   print(f' {i} {friend}') #this gives ma a list with numbers next to each one counting up
#   i += 1

for num, friend in enumerate(friends,51):
  print(f' {num} {friend}') #this gives ma a list with numbers next to each one counting up also

print(list(enumerate(friends,1))) #makes a tuple like [(0, 'Brian'), (1, 'Judith'), (2, 'Reg'), (3, 'Loretta'), (4, 'Colin')]

for friend in enumerate(enumerate(friends,1),-99): #this gave ma a tuple with two sets of numbers counting up
  print(friend)
print(type(enumerate(friends)))
print(list(enumerate(friends)))

for num, letter in enumerate('United States', start = 1): #this gave me a tuple each letter with a number next to it as a string
  print(num, letter)