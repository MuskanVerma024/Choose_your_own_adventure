import time

def pause(text):
    print(text)
    time.sleep(1.5)

name = input("Enter your name, brave adventurer: ")
pause(f"\nWelcome, {name}, to the Enchanted Forest Adventure!")
pause("You find yourself at the edge of a mysterious forest under a twilight sky.")
pause("A narrow dirt path splits into two — one veers LEFT into dark woods, the other RIGHT toward glowing mushrooms.")

choice1 = input("\nWhich path do you choose? (left/right): ").lower()

if choice1 == "left":
    pause("\nYou step into the shadowy woods. The trees whisper as the wind howls.")
    pause("Soon, you reach a wide river. It rushes violently.")

    choice2 = input("Do you want to SWIM across or BUILD a raft with fallen logs? (swim/build): ").lower()

    if choice2 == "swim":
        pause("\nYou dive into the icy water...")
        pause("But a dark shape swims below you... A river beast pulls you under.")
        pause("You fought bravely, but alas...")
        print("⚰️ You were eaten by the river beast. GAME OVER.")
    
    elif choice2 == "build":
        pause("\nYou gather logs and vines, tying them into a makeshift raft.")
        pause("You float safely across the river!")
        pause("On the other side, a golden key glimmers on a rock.")

        choice3 = input("Do you TAKE the key or LEAVE it? (take/leave): ").lower()
        if choice3 == "take":
            pause("\nThe key unlocks a hidden gate in the forest... You find a treasure chest!")
            pause("Inside is a magical crown. You are crowned the ruler of the forest.")
            print("👑 YOU WIN, King/Queen of the Enchanted Forest!")
        else:
            pause("\nYou walk away, but get lost in the fog.")
            print("💨 You vanish into the mist. GAME OVER.")
    else:
        print("❌ Invalid choice. The forest swallows you. GAME OVER.")

elif choice1 == "right":
    pause("\nYou follow the glowing mushrooms. They light your path softly.")
    pause("Suddenly, a wooden bridge appears over a deep chasm.")

    choice2 = input("Do you CROSS the bridge or SEARCH the area around? (cross/search): ").lower()

    if choice2 == "cross":
        pause("\nYou step cautiously onto the creaky bridge...")
        pause("It holds! You reach the other side where a wizard stands, smiling.")

        choice3 = input("The wizard asks: 'Will you help me defeat the shadow beast?' (yes/no): ").lower()
        if choice3 == "yes":
            pause("\nThe wizard grants you a glowing sword!")
            pause("Together, you battle the shadow beast and defeat it.")
            print("⚔️ You are hailed as a hero across the lands. YOU WIN!")
        else:
            pause("\nThe wizard frowns and vanishes.")
            print("🙁 You walk alone into darkness. GAME OVER.")

    elif choice2 == "search":
        pause("\nYou discover a hidden lever under a mushroom.")
        pause("Pulling it reveals a tunnel leading to a secret village of fairies!")
        print("🧚‍♂️ You live a magical life among the fairies. YOU WIN!")
    
    else:
        print("❌ Invalid choice. You fall into the chasm. GAME OVER.")

else:
    print("❌ You stand still for too long... and vanish into legend. GAME OVER.")
