import random
# print(random.randrange(start,stop))

top_of_range = input("Type of number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Enter greater number. ')
        quit()
else:
    print("Try a digit. ")

random_number = random.randrange(-1,11)

while True:
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess= int(user_guess)
    else:
        print("Try a digit. ")
        continue 

    if user_guess == random_number:
        print("You got it!")
        break
    else:
        print("Try again")
