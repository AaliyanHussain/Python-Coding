game_running = True
inventory = []
print ("You are in an abandoned hospital.")
while game_running == True:
    action = input("\nWhat do you do? (Search/Die like a coward): ")
    if action == "Search":
      print("You search the toilet and find a rusty knife")
      inventory.append("Knife")
    elif action == "Die like a coward":
       print("You have chosen to die like a coward, Game Over.")
       game_running = False
    else:
       print("You just stand there doing nothing, she is upset.")
