print('')
print('------------------Conditionals---------------------')
print('')

# is_raining = True
# is_cold = False
# print('Good Morning')
# if is_raining and is_cold:# the 'and' can be an 'or' also
#   print('Bring a raincoat and a jacket')
# else:
#   print('Raincoat is optional')

# is_raining = False
# is_cold = True
# print("Good Morning")
# if is_raining and is_cold:
#     print("Bring Umbrella and jacket")

# elif is_raining and not(is_cold):
#     print("Bring Umbrella")

# elif not(is_raining) and is_cold:
#     print("Bring just a jacket")

# else:
#     print("Just a shirt is fine")


# amount = 200
# if amount <= 50:
#   print('Approved')
# else:
#   print('Denied')

print('')
print('------------------Else If Exercise---------------------')
print('')

# this is a calculator that also is a temperature converter °C to °F
# mode = input('Enter the operation: ')
# num1 = float(input('Enter your first number: '))
# if mode == 'Temp':
#   print(f'{num1} °C is equal to {num1 * (9/5) + 32} °F')
# else:
#   num2 = float(input('Enter your second number: '))
#   if mode == '*' :
#     print(num1 * num2)
#   elif mode == '+':
#     print(num1 + num2)
#   elif mode == '-':
#     print(num1 - num2)
#   elif mode == '/':
#     print(num1 / num2)
#   else:
#     print("Input Error")

print('')
print('------------------Else If Exercise---------------------')
print('')

def num_days(month):

    if month == 'jan' or month == 'mar' or month == 'may' or month == 'jul' or month == 'aug' or month == 'oct' or month == 'dec':
        print('number of days in',month,'is',31)
    elif month == 'apr' or month == 'jun' or month == 'sep' or month == 'nov':
      print('number of days in',month,'is',30)
    elif month == 'feb':
        print('number of days in',month,'is',28)

num_days('jun')

# or
def num_days(month):
    days = 30
    if month in  {'jan','mar','may','jul','aug','oct','dec'}:
        days = 31
    elif month == 'feb':
        days =28
    print('number of days in',month,'is',days)
#     

num_days('jan')
# optimize/shorten the code in the function
# try to reduce the number of conditionals 