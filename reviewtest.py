inventory = ["Flashlight", "Rusty Key"]
health = 50
inventory.append("First Aid Kit")
print("You find a First Aid Kit on the floor.")
if "First Aid Kit" in inventory:
    health += 50
else:
    print("You don't have any Heal")
# The player picks it up and adds it to inventory