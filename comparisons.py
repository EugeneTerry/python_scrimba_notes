print('')
print('------------------Comparisons---------------------')
print('')

a=7
b=3
print('a == b is', a == b)
print('a != b is', a != b)
print('a > b is', a > b)
print('a < b is', a < b)
print('a >= b is', a >= b)
print('a <= b is', a <= b)
print('o in John is ','o' in 'John') #membership
print('o in John is ','o' not in 'John') #non membership
print('John is John ','John' is 'John') #identity
print('John is not John is ','John' is not 'John') # negative identity

a = [3, 7, 42]
b = [3, 7, 42]
print(a is b)
print(id(a), id(b)) #shows the memory slot each one is in

print('')
print('------------------Booleans---------------------')
print('')

print(bool('john')) #true
print(bool('')) #false
print(int(False)) #0