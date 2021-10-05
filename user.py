print('')
print('------------------User Input---------------------')
print('')

name = input('What is your name?')  # opens an input box for name
age = input('How old are you?')  # opens an input box for age
print('Hello '+name + '! You are '+age+' years old')

print('')
print('------------------Calculate User Input---------------------')
print('')

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
answer = float(num1)+float(num2)  # this will add both inputs
print(f'If you add {num1} to {num2} you will get {answer}')

print('')
print('------------------Input Exercise---------------------')
print('')

distance = input('Enter your distance: ')
convert = float(distance)/1.609
print(f'Hello {name.title()}! Your distance in {float(distance)} kilometers is equal to {convert} miles')
