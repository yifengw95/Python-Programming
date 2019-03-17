import random
random_number = random.randint(1,10)
count = 0
while(True):
    guess = input('input your guess')
    try:
        guess = int(guess)
        count = count + 1
        if guess > random_number:
            print('your guess is larger than the real number')
        elif guess < random_number:
            print('your guess is smaller than the real number')
        else:
            print('your guess is accurate')
            print('you took {number} guesses to get the accurate number'.format(number = count))
            break
    except:
        print('your input is not valid, please input it again')