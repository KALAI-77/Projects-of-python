
import random                                   # python in-built module import for print random number

print("Welcome To The Guessing Number Game!")             # this print greetings for game

random_num = random.randint (1,100)                    # randint fuction give random number in 1 to 100 

attempts = 0                                    # (attempts it's used for how many time player to takes attempts)

while True :  

    guess=int(input("Guess The Number : "))            # guess variable get the number from player

    attempts +=1                               # this arguments attempts count one plus one 
  

    if guess == random_num:
        print(f"Congratulations You Won in {attempts} attempts. ")    # this is if guess number equal to random number this statement will print & break the loop
        break

    elif guess > random_num:
        print("It's Too High!")                # this statement guess number greater than random number, it will print

    else:
     print("It's Too Low!")                    # this statement guess number less than random number, it will print
