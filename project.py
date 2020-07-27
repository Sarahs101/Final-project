name = input("What's your name? ")
print("Nice to meet you " + name + "! Welcome to my adventure game!!!")

adventure = input("Do you want your adventure to start at home, at night in the street or in the forest? ")
if adventure == "at home":
    print("Your adventure will start now at home.")

elif adventure == "at night in the street":
    print("Your adventure will start now in the dark lonely streets!")

elif adventure == "in the forest":
    print (" Your adventure will start now in the creepy forest!")

else:
    print("You have to make a choice!")

# def adventure(home):
