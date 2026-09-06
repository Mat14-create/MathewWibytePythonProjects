import time
print('Hello World')

#get player info.

a = input('What is your name?')
b = input('What country are you from?')
c = input('What is your favourite food?')
d = input('What is your favourite animal to pet?')

#animating and printing "Gathering User Information"

print('\n')
print('Gathering User Information', end='')

for i in range(3):
    print('.', end='', flush=True)
    time.sleep(0.5)

#printing user information

print('\n')
print(f'Your name is {a}!')
print(f'Welcome From {b}!')
print(f'Your fav food is {c}!')
print(f'You like the animal {d}!')

print('\n') #this line of code is to leave a space/seperation
print(f'I have made something for you {a}!')#tells the user there is something for them

#special characters showcase

print('\nUnique Characters Demo:')
print('Quote: \"Coding is fun!\"')
print('Backslash: \\')
print('Tab:\tSUP')
print('Vertical Tab:\vDayum!')

#print charcters and spacing

print()
print()
print()
print('1234')

#Letter Art

print('PPPPP  # Y   Y  # TTTTT  # H   H  # OOOOO  # N   N')
print('P   P', ' Y Y ', '  T  ', 'H   H', 'O   O', 'NN  N', sep = '  # ')
print('PPPPP', '  Y  ', '  T  ', 'HHHHH', 'O   O', 'N N N', sep = '  # ')
print('P ', '  Y  ', '  T  ', 'H   H', 'O   O', 'N  NN', sep = '  #')
print('P ', '  Y  ', '  T  ', 'H   H', 'OOOOO', 'N   N', sep = '  # ', end= ' ')

#Complimenting User

print('Your name in cool style:\n')

# to print the letters as uppercase in a pattern

for letter in a.upper():
    print(letter * 5)
    time.sleep(0.2)

#Animating and displaying "launching to the moon"

print('\nLaunching To The Moon!')

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

print('🚀 GO!')

#countdown

print('\nProgress:')
for i in range(101):
    print(f'\r{i}% Complete', end='')
    time.sleep(0.02)

print('\n')

#Complementing The User

print(f'{a} from {b} who likes to eat {c} and pet the animal {d} is learning how to code like a king')