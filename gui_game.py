import tkinter as tk

# Initialize the game window
root = tk.Tk()
root.title("Nightmare - Horror Game")
root.geometry("1920x1080")
root.config(bg="#0d0d0d") # Dark creepy background

# Game state variables
inventory = []

# Scrollable or display text box for the story
story_display = tk.Text(root, height=16, width=75, bg="#1a1a1a", fg="#00ff66", font=("Courier", 11), wrap=tk.WORD)
story_display.pack(pady=20)
story_display.insert(tk.END, "Banging on door...\n...\nLet me help you... I love you.\n\nDo you want to open the door?")
story_display.config(state=tk.DISABLED) # Make it read-only so user types via buttons

def update_story(text):
    story_display.config(state=tk.NORMAL)
    story_display.insert(tk.END, "\n" + text + "\n")
    story_display.see(tk.END)
    story_display.config(state=tk.DISABLED)

def choose_door_yes():
    update_story("\n> You chose: Yes")
    update_story("A rotting smell came into your room. You found a letter on the ground.")
    inventory.append("Letter")
    update_story(f"[Inventory Updated: {inventory}]")
    update_story("Its written with blood, 'MEET ME DOWNSTAIRS'. You hear someone walking behind you.")
    
    # Change buttons for the next choice (Window)
    btn_choice1.config(text="Open Window", command=choose_window_yes)
    btn_choice2.config(text="Ignore Window", command=choose_window_no)

def choose_door_no():
    update_story("\n> You chose: No")
    update_story("You hear a women crying behind you, Good Luck.")
    update_story("GAME OVER: You stayed frozen.")
    disable_buttons()

def choose_window_yes():
    update_story("\n> You opened the window.")
    update_story("You see a shade of a woman in the light of streetlight, She has a blooded knife. You are Fucked!")
    update_story("GAME OVER")
    disable_buttons()

def choose_window_no():
    update_story("\n> You ignored the window.")
    update_story("You hear someone walking above your roof. You start running towards exit door, but realize you are trapped in a loop!")
    update_story("GAME OVER: Trapped forever.")
    disable_buttons()

def disable_buttons():
    btn_choice1.config(state=tk.DISABLED)
    btn_choice2.config(state=tk.DISABLED)

# Control Buttons at the bottom
button_frame = tk.Frame(root, bg="#0d0d0d")
button_frame.pack(pady=10)

btn_choice1 = tk.Button(button_frame, text="Open Door (Yes)", width=20, bg="#330000", fg="white", font=("Courier", 10, "bold"), command=choose_door_yes)
btn_choice1.pack(side=tk.LEFT, padx=15)

btn_choice2 = tk.Button(button_frame, text="Ignore Door (No)", width=20, bg="#003300", fg="white", font=("Courier", 10, "bold"), command=choose_door_no)
btn_choice2.pack(side=tk.RIGHT, padx=15)

# Run the app window
root.mainloop()