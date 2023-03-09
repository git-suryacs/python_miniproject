print("Welcome to my computer quiz!")

playing = input("Do you want to start playing the game??:[Yes/No] ")
if playing.lower() != "yes":
    print("Incorrent input, quitting the game")
    quit()

print("Okaay ! lets play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct !")
    score +=1
else:
    print("Incorrect answer")

answer = input("What does GPU Stand for? ")
if answer.lower() == "graphic processing unit":
    print("Correct !")
    score +=1
else:
    print("Incorrect answer")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct !")
    score +=1
else:
    print("Incorrect answer")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct !")
    score +=1
else:
    print("Incorrect answer")

print("End of the Game, Your score out of hundred is - > ",(score/4)*100)
