print('')
print('------------------Functions---------------------')
print('')
# def greeting(name, age):
#     print(f'Hello {name}, you are {age} years old')
# greeting('John', 30)

print('')
print('------------------Functions Exercise---------------------')
print('')
# 1. Add new print statement - on a new line
#    which says 'We hear you like the color xxx! xxx is a string with color 
# 2. extend the function with another  input parameter 'color', that defaults to 'red'
# 3. Capture the color via an input box as variable:color 
# 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday 
#  adding 1 to the age
# 5. Capitalize first letter of the 'name', and rest are small caps 
# 6. Favorite color should be in lowercase 

def greeting(name, age=28, color='red'):
    #Greets user with 'name' from 'input box' and 'age', if available, default age is used
    print('Hello '  +  name.title() + ', you will be ' + str(age+1) +' next birthday!')
    print(f'Hello {name.title()}, you will be {age+1} next birthday!')
    print(f'We hear you like the color {color.lower()}!')
color = input('Enter your color: ')
name = input('Enter your name: ')
age = input('Enter your age: ')
greeting(name, int(age), color)