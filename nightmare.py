import time
game_running = True
inventory = []
print("Banging on door.")
time.sleep(2)
print("...")
time.sleep(3)
print("Let me help you... I love you.")
while game_running:
     choice = input("\nDo you want to open the door? (Yes/No): ")
     if choice == "Yes":
        print("A rotting smell came into your room. You found a letter on the ground")
        inventory.append("Letter")
        print("Its written with blood, 'MEET ME DOWNSTAIRS'.")
        print("You hear someone walking behind you.")
        other_choice = input("\nYou should open the window behind you. Will you open the window? (Yes/No): ")
        if other_choice == "Yes":
            print("You see a shade of a women in the light of streetlight, She has a blooded knife. You are Fucked!.")
            game_running = False
        elif other_choice == "No":
            print("You hear someone walking above your roof.")
            print("You starts running towards exit door. But after 30 minutes you realize you are trapped in a loop and she won't let you go, Find a way out.")  
            fuck_choice = input("\nDo you wanna go downstairs? (Yes/No?): ")
            if fuck_choice == "Yes":
             print("Downstairs you saw a room and on the wall written come inside and you have no choice, YOU ARE HERS")
             game_running = False
            elif fuck_choice == "No":
             print("Door to downstairs is locked now hope you find a way to the roof, IDIOT")
             game_running = False   
     elif choice == "No":
      print("You hear a women crying behind you, Good Luck.")
      sub_choice = input("\nDo you wanna look back? (Death/Coward): ")
      if sub_choice == "Death":
       print("She puts her fingers in your eyes, You died like a soldier.")
       game_running = False
      elif sub_choice == "Coward":
       print("Everything goes silent and you are alive but you live like a coward.")
       game_running = False
     else:
      print("You stand there doing nothing, she is watching you.")