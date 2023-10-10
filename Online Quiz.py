import time
print ("Welcome to my computer quiz!")

playing = input ("Do you want to play? ")
print (playing)

if playing.lower() != "yes":
    print("Oh well, goodbye.")
    time.sleep(3)
    quit()

print ("Okay! Let's play! :)")
score = 0
    

answer = input ("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print ('Correct!')
    score += 1
    input("Press Enter for next question.")
else:
    print ("Incorrect!")
    print("Correct answer is: central processing unit")
    input("Press Enter for next question.")
    
answer = input ("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print ('Correct!')
    score += 1
    input("Press Enter for next question.")
else:
    print ("Incorrect!")
    print("Correct answer is: graphics processing unit")
    input("Press Enter for next question.")

answer = input ("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print ('Correct!')
    score += 1
    input("Press Enter for next question.")
else:
    print ("Incorrect!")
    print("Correct answer is: random access memory")
    input("Press Enter for next question.")

answer = input ("What does GB stand for? ")
if answer.lower() == "gigabytes":
    print ('Correct!')
    score += 1
    input("Press Enter for next question.")
else:
    print ("Incorrect!")
    print ("Correct answer is: gigabytes")
    input("Press Enter to see your score.")

#Score calculation
if score == 0:
    print("Your total score is " + str(score) + " try again.")
    print("You got " + str(score/4 * 100) + "%!")
    print("This quiz will now close.")
    time.sleep(10)

elif score == 1:
    print("Your total score is " + str(score) + " you can do better!")
    print("You got " + str(score/4 * 100) + "%!")
    print("This quiz will now close.")
    time.sleep(10)

elif score == 2:
    print("Your total score is " + str(score) + " nearly there!")
    print("You got " + str(score/4 * 100) + "%!")
    print("This quiz will now close.")
    time.sleep(10)

elif score == 3:
    print("Your total score is " + str(score) + " nice job!")
    print("You got " + str(score/4 * 100) + "%!")
    print("This quiz will now close.")
    time.sleep(10)

else:
    print("Your total score is " + str(score) + " Congrats!")
    print("You got " + str(score/4 * 100) + "%!")
    print("This quiz will now close.")
    time.sleep(10)
    
