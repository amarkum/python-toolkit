number = 100  # An integer assignment
miles = 1000.0  # A floating point
name = "John"  # A string

a = b = c = 40  # multiple assignment
d, e, f = 1, 2, "john"  # split assignment

# 1. if-elif-else
if number == 3:
    print(3)
elif number == 4:
    print(4)
else:
    print("unknown")

# 2. python string
str = 'Hello World!'
print(str)  # Prints complete string
print(str[0])  # Prints first character of the string
print(str[2:5])  # Prints characters starting from 3rd to 5th
print(str[2:])  # Prints string starting from 3rd character
print(str * 2)  # Prints string two times
print(str + "TEST")  # Prints concatenated string

# 3. python list
list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(list)  # Prints complete list
print(list[0])  # Prints first element of the list
print(list[1:3])  # Prints elements starting from 2nd till 3rd
print(list[2:])  # Prints elements starting from 3rd element
print(tinylist * 2)  # Prints list two times
print(list + tinylist)  # Prints concatenated lists

# 4. python tuple
# Tuples can be thought of as read-only lists. tuple - (), list - []
tuple = ('abcd', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print(tuple)  # Prints complete list
print(tuple[0])  # Prints first element of the list
print(tuple[1:3])  # Prints elements starting from 2nd till 3rd
print(tuple[2:])  # Prints elements starting from 3rd element
print(tinytuple * 2)  # Prints list two times
print(tuple + tinytuple)  # Prints concatenated lists

# 5. python dictionary
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(dict['one'])  # Prints value for 'one' key
print(dict[2])  # Prints value for 2 key
print(tinydict)  # Prints complete dictionary
print(tinydict.keys())  # Prints all the keys
print(tinydict.values())  # Prints all the values

# 6. python deleting reference
del name
