import random

done = False

name = input('Hello, What is your name? ')
while not done:
  try:
   num1 = int(input('Please tell me a Number: '))
   done = True
  except:
   print('That was an invalid input.')

   done = False

  try:
   num2 = int(input('Please tell me another Number: '))
   done = True
  except:
   print('That was an invalid input.')
   done = False

# Pick a random operator index
op = random.randint(0, 2)

if op == 0:
    lhs = num1 + num2
    correct_op = '+'
elif op == 1:
    lhs = num1 - num2
    correct_op = '-'
else:
    lhs = num1 * num2
    correct_op = '*'

# Display the puzzle to the user
print('\nCan you tell the missing operator? (+, - or *):')
answer = input(f"{num1} __ {num2} = {lhs}\nYour answer: ")

# Check the answer
if answer == correct_op:
    print('Good Job!')
else:
    print('You will Improve. Keep trying :D')


print()
print()

#introduction to a number 3.

num3 = random.randint(1, 100)

op1 = random.randint(0, 1)
op2 = random.randint(0, 1)

#num3 addition subtraction and multiplication if statements

if op1 == 0:
    rhs = num1 + num2
else:
    rhs = num1 - num2

if op2 == 0:
    lhs = rhs + num3
else:
    lhs = rhs - num3

print('Can you tell the missing operator? (++, +-, -+ or --):')
answer = input(f"{num1} __ {num2} __ {num3} = {lhs}\nYour answer: ")

# Convert op1 and op2 choices into the string expected from the user
str_op1 = "+" if op1 == 0 else "-"
str_op2 = "+" if op2 == 0 else "-"
correct_op2 = str_op1 + str_op2

# Check the answer
if answer == correct_op2:
    print("Good Job!")
else:
    print("You will Improve. Keep trying :D")
