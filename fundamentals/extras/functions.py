def add(a,b):	# function name: 'add', parameters: a and b
    x = a + b	# process
    return x	# return value: x

new_val = add(3, 5)
print(new_val)

def say_hi(name): #this is a parameter
    print('Hi,', name)

say_hi('Chris') #this is an argument
say_hi('Harper')
say_hi('Nars')

def say_hi(name):
    return "Hi", name
greeting = say_hi('Chris')

print(greeting)

def add(a, b):
    x = a + b
    return x
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2

