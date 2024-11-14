inventory = []
name = input("Hello, what is your name? ")
greetings = "Welcome to my world, [name]. You wake up after a long night sleep..."
greetings = greetings.replace("[name]", name)
print(greetings)
print("Mysteriously, you find yourself in the body of a hamster, leaping across vast fields in search of the golden dandelion.")
print("You pause, your tiny hamster heart pounding, as you gaze at a [Dandelion] before you. Do you focus on the dandelion or your own mysterious hamster-body?")
choice = input("What do you want to do? You can choose to **look at the dandelion**, **continue walking**, or **sniff the air**")

if "Dandelion" in choice:
    print("You approach the dandelion, its delicate white fluff catching the sunlight.")
    choice2 = input("What do you do? [Pick up] or [Leave]?")
    if "Pick up" in choice2:
        print("You carefully pick up the dandelion, storing it in your cheek pouch for later use.  It might come in handy.")
        inventory.append("Dandelion")
    elif "Leave" in choice2:
        print("You decide to leave the dandelion behind.  Perhaps there are more important things to find.")

elif "continue walking" in choice:
    print("You continue your journey, the sun warming your fur.  As you reach a small hill, you spot a dark hole in the ground.")
    print("Do you **investigate the hole** or **keep walking**?")
    choice2 = input("What do you do?  ")
    if "investigate" in choice2:
        print("You cautiously approach the hole, sniffing the air.  It smells musty and damp.")
        print("Do you **enter the hole** or **turn back**?")
        # ... 
    elif "keep walking" in choice2:
        print("You decide to keep walking, the open field calling to you.")
        # ... 
    else:
        print("You hesitate, unsure of what to do.  You decide to keep walking.")

elif "sniff the air" in choice:
    print("You sniff the air, catching a faint, sweet scent.  It seems to be coming from the direction of a nearby grove of trees.")
    print("Do you **follow the scent** or **ignore it**?")
    choice2 = input("What do you do?  ")
    if "follow" in choice2:
        print("You follow the scent, your tiny nose twitching with excitement.  As you enter the grove, you see a small, furry creature hiding behind a tree...")
        print("Do you **Walk up to the creature** or **Sneak away**")
        choice3 = input("What do you do? ")
        if "Walk up to the Creature":
            print("You slowly walk up to the mysterious creature, filled with courage you...")
            print("Do you **try to talk to it** or **attack it**")
            choice4 = input("What will you do? ")
            if "try to talk to it" in choice4:
                print("You... ")  # Remember to put something here later
    elif "ignore" in choice2:
        print("You decide to ignore the scent.  Perhaps it's not worth the risk.")
        # I'll add more here
    else:
        print("You hesitate, unsure of what to do.  You decide to continue walking.")

else:
    print("You stumble over your words, but continue on your journey.")

print("Well look there...")

for item in inventory:
    print(item)
