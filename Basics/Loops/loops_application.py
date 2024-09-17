import random 

number = random.randint(1,100)
chance = 5
counter = 0
while chance > 0 :
    chance -= 1
    counter += 1
    guess = int(input("Guess : "))

    if(number==guess):
        print(f"Congratulations !! You found the right number at your {counter}th guess . Your total score is {(100)-(20*(counter-1))}")
        break
    elif(number > guess):
        print("Number is bigger than your guess...")
    else:
        print("Number is smaller than your guess...")   
    if chance == 0:
        print(f"Game is over... The Number was {number}")     