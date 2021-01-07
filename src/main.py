
name = input("What is your name?")
print("Welcome",name," in this game you are required to do a set of tasks to unlock the keycode to a safe in four different rooms, which contains all of the passwords to each persons bank account you have 3 lives/chances to figure out each answer and if you fail them you will lose one life, and the police will be one step closer to finding out where you are. Once all of these lives have been lost the police will find your location and arrest you good luck, Godspeed" ,name, )
NorthRoom=False
EastRoom=False
SouthRoom=False
WestRoom=False

lives = 3
RoomsLeft = 4
while RoomsLeft > 0:
  RoomOption = input("which room would you like to go to? Type the letters of the direction you want to go(North, East, South, West.")

  if RoomOption == "North":
    attempts = 2
    if NorthRoom == True:
      print("Room has already been completed!")
    while NorthRoom == False:
      
      print("Room question")
      Nquestion = input("What is 2 + 2?")
      if Nquestion == "4":
      
        print("correct")
        NorthRoom = True 
        RoomsLeft = (RoomsLeft - 1)
        print("The code for the north room is qu")
        break
      
      
      
        
      if attempts == 0:
          lives = (lives-1)
          print("you have lost a life you now have", lives,"lives left!, You will now be ejected to the main room")
          break
      elif Nquestion != "4":
           attempts= (attempts - 1)
           print(attempts)
           print("incorrect")
      
  
  if RoomOption == "East":
    attempts = 2
    if EastRoom == True:
      print("Room has already been completed!")
    while EastRoom == False:
      print("Room question")
      Equestion = input("What is 4 x 2?")
      if Equestion == "8":
      
        print("correct")
        EastRoom = True 
        RoomsLeft = (RoomsLeft - 1)
        print("The code for the north room is int")
        break
      
      
      if attempts == 0:
          lives = (lives-1)
          print("you have lost a life you now have", lives,"lives left!, You will now be ejected to the main room")
          break
      elif Equestion != "8":
           attempts= (attempts - 1)
           print(attempts)
           print("incorrect")


  if RoomOption == "West":
    attempts = 2
    if WestRoom == True:
      print("Room has already been completed!")
    while WestRoom == False:
      print("Room question")
      Wquestion = input("What is 4 + 2?")
      if Wquestion == "6":
      
        print("correct")
        WestRoom = True 
        RoomsLeft = (RoomsLeft - 1)
        print("The code for the north room is upl")
        break
      
      
      if attempts == 0:
          lives = (lives-1)
          print("you have lost a life you now have", lives,"lives left!, You will now be ejected to the main room")
          break
      elif Wquestion != "6":
           attempts= (attempts - 1)
           print(attempts)
           print("incorrect")

 
  if RoomOption == "South":
    attempts = 2
    if SouthRoom == True:
      print("Room has already been completed!")
    while SouthRoom == False:
      print("Room question")
      Squestion = input("What is 2 / 2?")
      if Squestion == "1":
      
        print("correct")
        SouthRoom = True 
        RoomsLeft = (RoomsLeft - 1)
        print("The code for the north room is ets")
        break
      
      
      if attempts == 0:
          lives = (lives-1)
          print("you have lost a life, you now have", lives,"lives left!, You will now be ejected to the main room")
          break
      elif Squestion != "1":
           attempts= (attempts - 1)
           print(attempts)
           print("incorrect")
  if lives ==0:
    print("You have lost try again")
    break


  
  
  

if RoomsLeft == 0: 
  codeTest=False
  while codeTest == False:
    finalCode= input("You have beaten all of the rooms please enter the code in the order N,E,W,S ")
    if finalCode == "quintuplets":
     print("well done you beat the game")
     codeTest =True
    if finalCode != "quintuplets":
      lives =(lives -1)
      print("You now have", lives, " left, try again!")
    if lives == 0:
      print ("you have lost the game try again")
      break

