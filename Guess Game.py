from random import randint

computer = randint(1,10)
tried = 1
while True:
    try:
        player = int(input('Guess a number between 1 and 10: '))
        if 0 < player < 11:
            if player == computer:
                if tried == 1:
                    print(f"You won with just {tried} chance! Do you have clairvoyance?")
                elif 1 < tried < 5:
                    print(f'Okay, not bad. You got in {tried} times.')
                else:
                    print(f"Finally! After {tried} times. Get better, okay?")
                break
            else:
                tried+=1
                print('Oh, oh. Try again.')
        else:
            print('I said 1 to 10. Try again!')
    except:
        print('Guess a number! N U M B E R')
