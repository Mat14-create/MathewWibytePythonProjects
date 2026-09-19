import random
n = random.randint(1, 100)

print('I have selected a number between 1 and 100, Please try to guess it.')

attempts = 0
done = False

while not done:
    guess = int(input('Guess the number:\n'))
    attempts = attempts + 1

    if guess > n:
        print('My number is smaller than your guess')

    if guess < n:
        print('My number is bigger than your guess')
    if guess == n: 
        print('Bingo!!! You guessed it right!!!')
        print('Attempts taken', attempts)
        done = True

print()
print()

print('Now it\'s your turn to select a number between 1 and 100, and I will try to guess it.')
print('Click Enter when ready...')

input()

done = False
attempts = 0
guess = 1
guess_step = 10
prev_answer = ['', '']
xy = 'xy'
low = [0, 0]
high = [100, 100]

while not done:

    for kk in range(2):
      guess [kk] = round((low[kk] + high[kk])/2)

      answer =input('Is your number in the ' + xy[kk] + ' coordinate? (y = yes, n = no)\n')
            

    print('I will guess the', xy, 'coordinate of your number')
    guess = (low[kk] + high[kk]) // 2


    answer = input('Is it \n' + str(guess) + '?' + '(y = yes, s = smaller than that, l = larger than that)\n')
    attempts = attempts + 1

    print('attempts =', attempts, 'prev answer = ', prev_answer,'answer =', answer)

    if attempts > 1:
        if prev_answer != answer:
            # Cut the step in half if you change direction (e.g. going from smaller to larger)
            guess_step = max(1, guess_step // 2) 
        prev_answer[kk] = answer[kk]

    if answer[kk].lower() == 's':
            guess = guess - guess_step
            if guess < 1: guess = 1
    if answer[kk].lower() == 'l':
            guess = guess + guess_step
            if guess > 100: guess = 100
    high [kk] = guess [kk]

    if answer == 'y':
            print('Bingo!!! I guessed it right!!!')
            print('Attempts taken', attempts)
            done = True
        
    n = random.randint(1, 100)
    print(n)

    temp = random.randint(1, 100)

    if temp > 90:
         n = random.randint (1, 90)
    else:
         n = random.randint (91, 100)

print(n)

#Project not completed yet because line 43 is still wrong but will fix it tomorrow.
