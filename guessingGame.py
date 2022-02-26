import random
number = random.randint(1, 9)
chances = 0

while chances < 5: 
#while loop start
    guess = int(input("Enter your guess: "))

    if(number == guess):
        print("You guessed the number! Good Job!")
        break
        #if end

    elif(number < guess):
        print("Your number is too big, try a smaller number.")
        #elif end

    elif(number > guess):
        ("Your number is too small, try a larger number.")
        #elif2 end
     
    chances = chances + 1
#while loop end

if not chances < 5:
    print("YOU LOST!!! The number was ", number)


