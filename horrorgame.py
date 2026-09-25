Inventory = ["Flashlight", "Needle"]
print("You came across a dark hallway. A door to the basement blocks your.")
print("\nYou search inside the deadbody pockets and find Rusty Key")
Inventory.append("Rusty Key")

if ("Rusty Key") in Inventory:
      print("You tried to insert the rusty key in the basement door...")
      print("The door opens with a creaking sound. Hope you make it out alive :).")
      Inventory.remove("Rusty Key")
else:
     print("The door is locked. Hope she lets you get to the keys... Good Luck.")

print("\nFinal Inventory:", Inventory)
    