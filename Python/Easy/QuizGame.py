print("Welcome")

playing = input("Want to play? ")

if playing.lower() != "yes":
    quit()

score = 0

answer = input("What does CPU stand for? ")
if answer == "Central Processing Unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer == "Random Access Memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer == "Graphics Processing Unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Completed ")
print("You Got",score,"Questions Correct")