num1 = 42
#this is a int
num2 = 2.3
#this is a float
boolean = True
#boolean only true or false statements no quotes needed
string = 'Hello World'
#srtring
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#list with names
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#tuples mixed values
fruit = ('blueberry', 'strawberry', 'banana')
#dictionary
print(type(fruit))
#will print to the console
print(pizza_toppings[1])
#will print to the console sausage as thats the value its declaring
pizza_toppings.append('Mushrooms')
#add mushrooms to the list of toppings
print(person['name'])
#will print john to the console
person['name'] = 'George'
#chnage the dictonary value to george
person['eye_color'] = 'blue'
#change the dictionary value to blue
print(fruit[2])
#print banana to the console

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
#conditional statement if number is grater than 45 itll print "its greater" if it is not itll print "its lower"

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
#conditional statement will print the values depending on the number of values in string

for x in range(5):
    print(x)
#loop 0-5
for x in range(2,5):
    print(x)
#loop 2-5
for x in range(2,10,3):
    print(x)
#loop 2-10 that incraeses by 3 everytime it prints

x = 0
while(x < 5):
    print(x)
    x += 1
#Will print the number and and increase by one until it reaches 4

pizza_toppings.pop()
#will remove the last value
pizza_toppings.pop(1)
#will remove the second value

print(person)
#print dictionary value
person.pop('eye_color')
#will remove eye color value
print(person)
#will print dictionary value with poped value

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
#loop through the list if the topping of pep is true itll print if its not itll go to the next statement 
# if topping is olives itll stop the loop

def print_hello_ten_times():
    for num in range(10):
        print('Hello')
#declares what to do then the loop will start from 0-10 and as long as the value is true it will print to console 

print_hello_ten_times()
#calls the previous function

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')
#declares what to do then if value is within the range itll print hello

print_hello_x_times(4)
#calls the previous function as x=4

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')
#function will loop unti the defined value and will print hello

print_hello_x_or_ten_times()
#calls the previous function
print_hello_x_or_ten_times(4)
#calls the previoius funtion but as x=4

"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)