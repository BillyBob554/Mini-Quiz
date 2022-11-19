score = 0
print("Welcome To Mini Quiz V1.0!")

playing = input("Do You Want To Play? ")

if playing != "yes": 
  print("Ok, Come Back When You're Ready.")
  quit()

print("Ok! Let's Play!")

#Question 1
answer = input("What Is 10 X 10? ")
if answer == "100":
  print('Correct!')
  score = score + 1
  
else:
  print("Incorrect!")

#Question 2
answer = input("What's the name of the river that runs through Egypt? ")
if answer == "The Nile River":
  print('Correct!')
  score = score + 1
  
else:
  print("Incorrect!")

#Question 3
answer = input("How Many Days Are In A Week? ")
if answer == "7":
  print('Correct!')
  score = score + 1
  
else:
  print("Incorrect!")

#Question 4
answer = input("What Is The Fastest Land Animal? ")
if answer == "Cheetah":
  print('Correct!')
  score = score + 1
  
else:
  print("Incorrect!")

#Question 5
answer = input("What Does PC Stand For(Computer Wise)? ")
if answer == "Personal Computer":
  print('Correct!')
  score = score + 1
  
else:
  print("Incorrect!")

#Question 6
answer = input("What Is A Normal #2 Pencil Made Of? ")
if answer == "Wood":
  print('Correct!')
  score = score + 1
  
else:
  print("Incorrect!")

#Question 7
answer = input("Is Normal Poop Brown? ")
if answer == "Yes":
  print('Correct!')
  score = score + 1
  
else:
  print("Incorrect!")

#Question 8
answer = input("Does Pineapple Belong On Pizza? ")
if answer == "No":
  print('Correct!')
  score = score + 1
  
else:
  print("Incorrect!")

#Question 9
answer = input("Is Soccer The Best Sport? ")
if answer == "Yes":
  print('Good')
  score = score + 1
  
else:
  #Question 10
  answer = input("Are You Sure? ")
  if answer == "No":
    print("That's What I Thought.")
    score = score + 1
  else:
    print("I'm Just Going To Assume That You're Joking.")

#Score Counter
print(score,"/ 10")

if score >= 5:
  print("Congratulations! You Passed This Quiz!")

else:
  print("I'm Sorry. You Did Not Pass This Quiz.")
  print("Try Again Next Time.")