#!/usr/bin/python3
""" Text-based game that follows Hack Sprint Theme: Lost and Found """
""" Goal: 20 scenarios; each scenario will have 3 options, at least one option must end in GAME OVER """
""" GAME OVER: The player has died """

users_choice = []
health_bar = 100
battle_choices = []
num_hits = 0

def start():
    print("You are a fabulous drag queen with a purpose to fulfill!!!")
    print("You have a performance at 10pm.")
    print("You will have many decisions to make today, some will determine your death, others will determine your success.")
    print("Ready to play? Type y or n.")

    start_choice = input("Make your decision!\n").lower()

    if 'y' in start_choice:
        wake_up()
    else:
        exit()
        
def wake_up():
    print("You have just woken up from your slumber, what is your lewk today?")
    print("Hazmat suit")
    print("Bikini with glitter boots")
    print("Favorite waifu")
    print("Type out the full lewk of your choice.")

    users_choice.append(input("Make your decision!\n").lower())

    if "hazmat suit" in users_choice:
        print("We like the way you roll.")
        bag_choice()

    if "bikini with glitter boots" in users_choice:
        print("Get some better style and try again next time.")
        game_over()

    if "favorite waifu" in users_choice:
        print("You're a nerd, but nice one.")
        bag_choice()

def bag_choice():
    print("What supplies do you need for your lewk?")
    print("Blue bag")
    print("Red bag")
    print("Yellow bag")

    users_choice.append(input("Make your decision!\n").lower())

    if "blue bag" in users_choice:
        print("Oh! Well... I hope you have what you need in that bag.")
        place()

    if "red bag" in users_choice:
        print("Oh! Well... I hope you have what you need in that bag.")
        place()

    if "yellow bag" in users_choice:
        print("Who are you? Why do you wear yellow? Blink twice if you need help.")
        game_over()

def place():
    print("Where are you gonna beat your mug?")
    print("Home")
    print("Club")

    users_choice.append(input("Make your decision!\n").lower())

    if "home" in users_choice:
        print("I'm sorry, I think you are confused.")
        users_choice.pop(2)
        place()

    if "club" in users_choice:
        print("Get on the road Betch!!!")
        music_choice()


def music_choice():
    print("You think best while driving, what song will you perform on the main stage 2nite?")
    print("God is a Woman by Ariana Grande")
    print("Fergalicious by Fergie")
    print("Friday by Rebecca Black")
    print("Type the song title only when making your choice.")
    
    users_choice.append(input("Make your decision!\n").lower())

    if "god is a woman" in users_choice:
        print("You betta believe!!")
        snack_choice()
        
    if "fergalicious" in users_choice:
        print("Werk! How fergalicious are you?")
        snack_choice()

    if "friday" in users_choice:
        print("...I think you just died.")
        game_over()


def snack_choice():
    print("Guurrllll, thinkin about your performance made you hongry?!?")
    print("You gonna get a snack, from where though?")
    print("QuikTrip")
    print("Starbucks")
    print("McDonalds")

    users_choice.append(input("Make your decision!\n").lower())

    if "quiktrip" in users_choice:
        print("Why you eat that sushi though? E-coli is a betch! You have passed on.")
        game_over()

    if "starbucks" in users_choice:
        print("Is your name Karen? It's okay if it is, just curious.")
        club_location()

    if "mcdonalds" in users_choice:
        print("You got Mcdonalds money? There's a turkey leg in the glovebox!") 
        club_location()


def club_location():
    print("You have made it to the club and you are ready to step in them heels!")
    print("You need good lighting to make sure the illusion sticks.")
    print("From where, will this beautiful woman emerge?")
    print("Alley")
    print("Parking lot")
    print("Dressing room")

    users_choice.append(input("Make your decision!\n").lower())

    if "alley" in users_choice:
        print("Everyone loves a good trash kween.")
        seat()

    if "parking lot" in users_choice:
        print("You got stabbed by a random pedestrian. Never put on makeup in the car.")
        game_over()
    
    if "dressing room" in users_choice:
        print("Oh you fancyyyyyyy")
        seat()


def seat():
    print("Where are you gonna kiki?")
    print("Your bff is sitting close but you see your newest frenemy nearby.")
    print("Who invited her?!?")
    print("Who are you joining?")
    print("Rival Kween")
    print("Sister bff")
    print("Club owner")

    users_choice.append(input("Make your decision!\n").lower())

    if "rival kween" in users_choice:
        print("Did you bring your glasses for the reading that will ensue?")
        battle()

    if "sister bff" in users_choice:
        print("Good thing you got your girls' back, she needed a spare set of lashes.")
        battle()

    if "club owner" in users_choice:
        print("You tried this before.... just stop. Respect yourself.")
        game_over()

#Battle begins

def battle():
    print("Your rival kween done lost her mind. She's come for Sister Bff's wig!")
    print("In your attempt to diffuse the situation the library opened. You read her to filth.")
    print("She's lunging at your face! What do you do?")
    print("Choose your weapon wisely girl! How will you battle this beast?!")
    print("Weapon")
    print("Fists")
    print("My words")
    
    users_choice.append(input("Make your decision!\n").lower())

    if "weapon" in users_choice:
        print("You out for blood hunty.")
        weapon()

    if "fists" in users_choice:
        print("Finally get to use them claws.")
        fists()

    if "my words" in users_choice:
        print("Your tongue really that sharp boo?")
        tongue_lash()

def weapon():
    print("You want a weapon? We got some options in your {}.".format(users_choice[1]))
    print("Here are your choices:")
    print("Pepper spray")
    print("Stiletto dagger")
    print("Brass knuckles")

    battle_choices.append(input("Make your decision!\n").lower())

    if "pepper spray" in battle_choices:
        print("Good choice for distance attacks!")

    if "stiletto dagger" in battle_choices:
        print("You have to get close, but you will do some damage.")

    if "brass knuckles" in battle_choices:
        print("Close to no weapon, but still a great choice!")

    armor()

def armor():
    print("You have your offense. Now, how are you gonna defend yo'self?")
    print("Choose from the following:")
    print("Trash Can")
    print("Breastplate")
    print("Sister bff")

    battle_choices.append(input("Make your decision!\n").lower())

    if "trash can" in battle_choices:
        print("You can't always get what you want can you?")

    if "breastplate" in battle_choices:
        print("Rubber can protect a person from many things.")

    if "sister bff" in battle_choices:
        print("You are ruthless!")

    hit_spot()

def hit_spot():
    print("Take your aim and strike!")
    print("Where is your first hit gonna land?")
    print("Face")
    print("Foot")
    print("Unmentionables")

    battle_choices.append(input("Make your decision!\n").lower())

    if "face" in battle_choices:
        print("You are going to actually beat her face, huh?")

    if "foot" in battle_choices:
        print("You may not win the fight, but you'll win on the dance floor.")

    if "unmentionables" in battle_choices:
        print("*gasp* How dare you?!.")

    hit_number()

def hit_number():
    print("You are gonna hurt this queen, bad.")
    print("How many times are you going to stike?")
    print("It's gotta be between 1 and 10 max.")

    num_hits = int(input("Make your decision!\n"))

    for n in range(num_hits):
        print("Smack!")

def dodge():
    print("Good hit girl! But you better get prepared.")
    print("She's comin' in hot with a baseball bat!")
    print("Think quick! How will you dodge?")
    print("Death drop")
    print("Juke")
    print("Cart-wheel")

    battle_choices.append(input("Make your decision!\n").lower())

    if "death drop" in battle_choices:
        print("You have won all the things. That was sickening.")

    if "juke" in battle_choices:
        print("Float like a butterfly, and sting like a bee.")

    if "cart-wheel" in battle_choices:
        print("Why do you think you're Simone Biles? Stop that.")

    lash_quest()

def lash_quest():
    

def game_over():
    exit()


if __name__ == "__main__":
    start()

 
