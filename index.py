print('')
print('------------------Datatypes---------------------')

failed_subjects = "6"
name = 'John'

print('Dear Mrs Badger')
print('Your son '+name+' is failing ' + failed_subjects + ' subjects.')
print(name+' will need to redo ' + failed_subjects + ' courses.')

name = 'Eric'
print(name+' is doing well in geography.')
print('')
print('------------------Datatypes---------------------')


failed_subjects = 2
name = 'John'
print('')
print("In the code we are using the number 2 as an interger and not a string 'str(failed_subjects)'")
print('Dear Mrs Badger')
print('Your son '+name+' is failing ' + str(failed_subjects) + ' subjects.')
print(name+' will need to redo ' + str(failed_subjects) + ' courses.')

name = 'Eric'
print(name+' is doing well in geography.')
print('')
print(type('hello'))
print(type(1))
print(type(1.64))
print(type(True))

print('')
print('------------------Datatypes and Variables---------------------')
print('')

item_name = "Coke"
price = 1.75
in_stock = 5

print(item_name, '$', float(price), in_stock)

print('')
print('------------------Basic Arithmetic---------------------')
print('')

a = 10
b = 3
print('Addition : ', a + b)
print('Subtraction : ', a - b)
print('Multiplication : ', a * b)
print('Division (float) : ', a / b)
print('Division (floor) : ', a // b)
print('Modulus : ', a % b)
print('Exponent : ', a ** b)

print('')
print('------------------Strings---------------------')
print('')

msg = 'hello and welcome to my house of pain'
print(msg)  # printing the message
print(msg, msg)  # printing the message mor then once
print(msg.upper())  # capitalize all
print(msg.capitalize())  # capitalize first
print(msg.title())  # capitalize first of every word
print(len(msg))  # how many letters
print(msg.count('o'))  # how many "o's"
print(msg[7])  # which letter is in location 7?
print(msg[-1])  # which letter is the last?
print(msg[7:])  # what is a after 7?
print(msg[7:14])  # what is only between 7 and 14?
print(msg[:7])  # what is before and including 7?

print('')
print('------------------Strings Exercise---------------------')
print('')

msgI = 'Welcome to Python 101: Strings'
print((msgI[18]+' '+msgI[0:7]+' '+msgI[25:30]+' ' + msgI[8:10] +
      ' ' + msgI[13]+msgI[12]+msgI[2]+msgI[1]+msgI[25]).title())
print('')
print('In reverse')
print('')
print((msgI[18]+' '+msgI[0:7]+' '+msgI[25:30]+' ' + msgI[8:10] +
      ' ' + msgI[13]+msgI[12]+msgI[2]+msgI[1]+msgI[25]).title()[::-1])

print('')
print('------------------Multi-Lined Strings---------------------')
print('')

msg = """Dear Eugene,,
We need more nachos
in order for us to make it
through the big game tonight """
print(msg)

print('')
print('------------------Find and Replace Strings---------------------')
print('')

msg = 'Welcome to Python 101: Strings'
print(msg.find('h'))  # tells me that the 'h' is in the location #
print(msg.find('Python'))  # tells me where the location starts
print(msg.replace('Python', 'C++'))  # replaces Python with C++
print('Python' in msg)  # tells me if it is in the msg, true or false
print('Python' not in msg)  # tells me if it is NOT in the msg, true or false

print('')
print('------------------Place Strings In Line of Text---------------------')
print('')
name = 'TERRY'
color = 'RED'
msg = '[' + name + '] loves the color [' + color.lower() + ']!'
msg1 = f'{name.title()} loves the color {color.lower()}!'  # this is a function

print(msg)
print(msg1)
