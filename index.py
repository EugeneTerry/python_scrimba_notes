failed_subjects="6"
name='John'

print('Dear Mrs Badger')
print('Your son '+name+' is failing ' + failed_subjects + ' subjects.')
print(name+' will need to redo ' + failed_subjects + ' courses.')

name='Eric'
print(name+' is doing well in geography.')
print('')
print('------------------Datatypes---------------------')


failed_subjects=2
name='John'
print('')
print("In the code we are using the number 2 as an interger and not a string 'str(failed_subjects)'")
print('Dear Mrs Badger')
print('Your son '+name+' is failing ' + str(failed_subjects) + ' subjects.')
print(name+' will need to redo ' + str(failed_subjects) + ' courses.')

name='Eric'
print(name+' is doing well in geography.')
print('')
print(type('hello'))
print(type(1))
print(type(1.64))
print(type(True))

print('')
print('------------------Datatypes and Variables---------------------')
print('')

item_name="Coke"
price=1.75
in_stock=5

print(item_name, '$',float(price) , in_stock)