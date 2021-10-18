print('')
print('------------------Loops---------------------')
print('')

# print("1.*Loops are great*")
# print("2.**Loops are great**")
# print("3.***Loops are great***")
# print("4.****Loops are great****")
# print("5.*****Loops are great*****")

# Three Loop Questions:
#1. What do I want to repeat?
#  -> 
#2. What do I want to change each time?
#  -> 
#3. How long should we repeat?
#  -> 

i = 0
while i < 5:
  i += 1
  print(f'{i}. '+ '*' * i +'Loops are awesome'+ '*' * i)

#1. *Loops are awesome*
# 2. **Loops are awesome**
# 3. ***Loops are awesome***
# 4. ****Loops are awesome****
# 5. *****Loops are awesome*****

print('')
print('------------------Loops Exercise---------------------')
print('')

# correct_number = 33
# guess = 0
# guess_limit = 3
# guess_number = 0
# guess = int(input(f'Enter your guess between 1 and 50 '))
# guess_number +=1
# while guess_number < guess_limit:
    
#     if guess != correct_number:
#       guess_number +=1
#       if guess > correct_number:
#         guess = int(input(f'{guess} is too high, guess again '))
#       else:
#         guess = int(input(f'{guess} is too low, guess again '))
#     if guess == correct_number:
#       print (f'You Win!')
#       break
# if guess != correct_number:
#   print(f'Sorry you lose. It was {correct_number}')

print('')
print('------------------For Loops and Nesting---------------------')
print('')

# for letters in 'United States':
#   print(letters) #goes through every letter and prints each one out until there are no more

# print('For Loop Done')

# for numbers in range(10):
#   print(numbers) #goes through every number and prints each one out until there are no more

# print('For Loop Done')

# for numbers in range(4,10):
#   print(numbers) #goes through every number between 4 and 10 but not 10 and prints each one out until there are no more

# print('For Loop Done')


# friends = ['Mike', 'Helen', 'Jane', 'Markisha']
# for friend in friends:
#   print(friend) #goes through every name and prints each one out until there are no more

# print('For Loop Done')

# friends = ['Mike', 'Helen', 'Jane', 'Markisha']
# for friend in friends:
#   if friend == 'Helen':
#     print(f'Found {friend} !')
#     break
#   print(friend) #goes through every name and prints each one until it finds Helen and then prints the statement and stops

# print('')
# print('------------------For Loops and Nesting---------------------')
# print('')

# friends = ['Mike', 'Helen', 'Jane', 'Markisha']
# for friend in friends:
#   for number in [1,2,3,4]:
#     print(friend, number)

# print('for loop done')

print('------------------For Loops Exercise---------------------')
print('')

# have two lists of names, input two mor names and make invites with both lists
names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']

names.extend(names1)

# names.append(input('add first new name: '))
# names.append(input('add second new name: '))

for index in range(2):
  names.append(input('Enter new name: '))

for name in names:
  print(f'{name.title()}! you are invited to the party on Saturday')
