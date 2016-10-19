
low = 0
high = 100
est = (high + low)//2
ans = ''

print('Please think of a number between {} and {}!'.format(low, high))
while True:   
    print('Is your secret number {}?'.format(est))
    ans = input("Enter 'h' to indicate the guess is too high.\n"
                "Enter 'l' to indicate the guess is too low.\n"
                "Enter 'c' to indicate I guessed correctly. ")
    
    if ans == 'c':
        print('Game over. Your secret number was: {}'.format(est))
        break
    elif ans == 'l':
        low = est
    elif ans == 'h':
        high = est
    else:
        print('Sorry, I did not understand your input.')
    est = int(high + low)//2
