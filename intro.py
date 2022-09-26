#Creating a variable
msg = "Hello World"

#Prints the variable's contents
print(msg)

#Prints the length of the variable
print(len(msg))

#Prints the specific character of the variable
print(msg[0])
print(msg[1])
print(msg[2])
print(msg[3])
print(msg[4])

#Prints the chracters in the given range
print(msg[0:5])
print(msg[:5])

#Prints the string in all uppercase or lowercase
print(msg.lower())
print(msg.upper())

#Prints that how many times the word appeared in the given code
print(msg.count('Hello'))
print(msg.count('hello'))
print(msg.count('l'))

# Prints the line no. in which the given code appeared
print(msg.find('World'))

#Creating another variable which replaces the world with universe
new_msg=msg.replace('World', 'Universe')

print(new_msg)

#contatenation of two variables in types
#1
print(new_msg, 'and', msg)

#2
message = new_msg + ' and ' + msg
print(message)

#3
message = '{} and {}.'.format(new_msg, msg)
print(message)

#4
message = f'{new_msg} and {msg}.'
print(message)

#Prints the methods we can use with that data type
print(dir(msg))

#Prints all the methods possible and simple explanation of the data type
print(help(str))