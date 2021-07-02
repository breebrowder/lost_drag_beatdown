#!/usr/bin/python3
from time import sleep

""" Text-based game that follows Hack Sprint Theme: Lost and Found """
""" Goal: 20 scenarios; each scenario will have 3 options, at least one option must end in GAME OVER """
""" GAME OVER: The player has died """

users_choice = []
health_bar = 100
battle_choices = []

def start():
    color = '\033[35m'
    print(color + "You are a fabulous drag queen with a purpose to fulfill!!!")
    sleep(2)
    print("For some reason, you always lose things at the worst possible time.")
    sleep(2)
    print("What have you lost already?")
    sleep(2)
    print("What will you lose today?")
    sleep(2)
    print("You have a performance at 10pm.")
    sleep(2)
    print("Will you be prepared and slay?")
    sleep(2)
    print("You will have many decisions to make today, some will determine your death, others will determine your success.")
    sleep(2)
    print("Ready to play? Type y or n.")
    print()
    sleep(2)

    start_choice = input("Make your decision!\n").lower()
    print()

    if 'y' in start_choice:
        wake_up()
    else:
        exit()
        
def wake_up():
    sleep(2)
    print("You have just woken up from your beauty slumber")
    sleep(2)
    print("You feel refreshed and ready for the day.")
    sleep(2)
    print("You get up and go to your nightstand to look at your performance planner.")
    sleep(2)
    print("You have ALL THE THINGS in this planner. It is your life.")
    sleep(2)
    print("*gasp* Escandalo! It's not there!")
    sleep(2)
    print("You quickly look under your bed and the other night stand, and alas it's not there!")
    sleep(2)
    print("You take some deep breaths and remind yourself you are a PROFESSIONAL.")
    sleep(2)
    print("You got this. You'll just have to think of everything quickly. As in RIGHT NOW!")
    sleep(2)
    print("You first must decide on your outfit/lewk for the evening.")
    sleep(2)
    print()
    print("Hazmat suit")
    sleep(2)
    print("Bikini with glitter boots")
    sleep(2)
    print("Favorite waifu")
    sleep(2)
    print("Type out the full lewk of your choice.")
    print()
    sleep(2)

    users_choice.append(input("Make your decision!\n").lower())
    print()

    if "hazmat suit" in users_choice:
        sleep(2)
        print("We like the way you roll.")
        bag_choice()

    if "bikini with glitter boots" in users_choice:
        sleep(2)
        print("Oh no girl...")
        sleep(2)
        print("This game is rated 'E' for Everyone. You need to go back to sleep.")
        game_over()

    if "favorite waifu" in users_choice:
        sleep(2)
        print("You're a nerd, but excellent choice!")
        bag_choice()

def bag_choice():
    print()
    sleep(2)
    print("What supplies do you need for your lewk?")
    print()
    sleep(2)
    blue = '\033[34m'
    print(blue + "Blue bag")
    sleep(2)
    red = '\033[31m'
    print(red + "Red bag")
    sleep(2)
    yellow = '\033[33m'
    print(yellow + "Yellow bag")
    cyan = '\033[36m'
    print(cyan + ' ')
    sleep(2)

    
    users_choice.append(input("Make your decision!\n").lower())
    print()

    if "blue bag" in users_choice:
        sleep(2)
        print("Oh! Well... I hope you have what you need in that bag.")
        place()

    if "red bag" in users_choice:
        sleep(2)
        print("Oh! Well... I hope you have what you need in that bag.")
        place()

    if "yellow bag" in users_choice:
        sleep(2)
        print("Who are you? Why do you wear yellow? Blink twice if you need help.")
        game_over()

def place():
    print()
    sleep(2)
    print("Where are you gonna beat your mug?")
    print()
    sleep(2)
    print("Home")
    sleep(2)
    print("Club")
    print()
    sleep(2)

    users_choice.append(input("Make your decision!\n").lower())

    print()
    if "home" in users_choice:
        sleep(2)
        print("I'm sorry, I think you are confused.")
        sleep(2)
        print("Please try again. You're welcome.")
        users_choice.pop(2)
        place()

    if "club" in users_choice:
        sleep(2)
        print("Get on the road!!!")
        sleep(2)
        print("You still have choices to make!")
        sleep(2)
        music_choice()


def music_choice():
    print()
    sleep(2)
    print("You think best while driving, what song will you perform on the main stage 2nite?")
    sleep(2)
    print()
    print("God is a Woman by Ariana Grande")
    sleep(2)    
    print("Fergalicious by Fergie")
    sleep(2)
    print("Friday by Rebecca Black")
    sleep(2)
    print("Type the song title only when making your choice.")
    print()
    sleep(2)
    
    users_choice.append(input("Make your decision!\n").lower())

    print()
    if "god is a woman" in users_choice:
        sleep(2)
        print("You betta believe!!")
        sleep(2)
        snack_choice()
        
    if "fergalicious" in users_choice:
        print("Werk! How fergalicious are you?")
        sleep(2)
        snack_choice()

    if "friday" in users_choice:
        print("...I just said you are a professional. Why are you doing this to me?")
        sleep(2)
        game_over()


def snack_choice():
    print()
    print("Guurrllll, thinkin' about your performance made you hungry?!?")
    sleep(2)
    print("You gonna get a snack, from where though?")
    sleep(2)
    print()
    print("QuikTrip")
    sleep(2)
    print("Starbucks")
    sleep(2)
    print("McDonalds")
    print()
    sleep(2)

    users_choice.append(input("Make your decision!\n").lower())

    print()
    if "quiktrip" in users_choice:
        sleep(2)
        print("Why you eat that sushi though? E-coli is not your friend!")
        sleep(2)
        game_over()

    if "starbucks" in users_choice:
        sleep(2)
        print("Nothing peps a queen up more than caffeine and sugar!")
        sleep(2)
        club_location()

    if "mcdonalds" in users_choice:
        sleep(2)
        print("Are you sure? There's a turkey leg in the glovebox!") 
        sleep(2)
        club_location()


def club_location():
    print()
    print("You have made it to the club and you are ready to step in them heels!")
    sleep(2)
    print("You need good lighting to make sure the illusion sticks.")
    sleep(2)
    print("From where, will this beautiful entertainer emerge?")
    sleep(2)
    print()
    print("Alley")
    sleep(2)
    print("Parking lot")
    sleep(2)
    print("Dressing room")
    print()
    sleep(2)

    users_choice.append(input("Make your decision!\n").lower())

    print()
    if "alley" in users_choice:
        sleep(2)
        print("OooOOOoooOOOooo! Maybe you can find some supplies for your next trash bag eleganza darling.")
        sleep(2)
        seat()

    if "parking lot" in users_choice:
        sleep(2)
        print("You got stabbed by a random pedestrian. Never put on makeup in the car.")
        sleep(2)
        game_over()
    
    if "dressing room" in users_choice:
        sleep(2)
        print("Oh you fancyyyyyyy!")
        sleep(2)
        seat()


def seat():
    print()
    sleep(2)
    print("Where are you gonna sit?")
    sleep(2)
    print("Your bff is sitting close but you see your newest frenemy nearby.")
    sleep(2)
    print("Who invited her?!?")
    sleep(2)
    print("You also spot your former fling, the club owner.")
    sleep(2)
    print("Who are you joining?")
    sleep(2)
    print()
    print("Rival Kween")
    sleep(2)
    print("Sister bff")
    sleep(2)
    print("Club owner")
    print()
    sleep(2)

    users_choice.append(input("Make your decision!\n").lower())

    print()
    if "rival kween" in users_choice:
        sleep(2)
        print("Did you bring your glasses for the reading that will ensue?")
        sleep(2)
        battle()

    if "sister bff" in users_choice:
        sleep(2)
        print("Good thing you got your girls' back, she needed a spare set of lashes.")
        sleep(2)
        battle()

    if "club owner" in users_choice:
        sleep(2)
        print("You tried this before.... just stop. Respect yourself.")
        sleep(2)
        game_over()

#Battle begins

def battle():
    print()
    red = '\033[31m'
    print(red + "Your rival kween lost her mind. She's come for Sister Bff's wig!")
    sleep(2)
    print("In your attempt to defuse the situation the library opened. You read her to filth!")
    sleep(2)
    print("She's lunging at your face! What do you do?")
    sleep(2)
    print("Choose your weapon wisely girl! How will you battle this beast?!")
    sleep(2)
    print()
    print("Pepper spray")
    sleep(2)
    print("Stiletto dagger")
    sleep(2)
    print("Brass knuckles")
    print()
    sleep(2)

    battle_choices.append(input("Make your decision!\n").lower())

    print()
    if "pepper spray" in battle_choices:
        sleep(2)
        print("Good choice for distance attacks!")

    if "stiletto dagger" in battle_choices:
        sleep(2)
        print("You have to get close, but you will do some damage.")

    if "brass knuckles" in battle_choices:
        sleep(2)
        print("Close to no weapon, but still a great choice!")

    sleep(2)
    armor()

def armor():
    print()
    print("You have your offense. Now, how are you gonna defend yourself?")
    sleep(2)
    print("Choose from the following:")
    sleep(2)
    print()
    print("Trash Can")
    sleep(2)
    print("Breastplate")
    sleep(2)
    print("Sister bff")
    print()
    sleep(2)

    battle_choices.append(input("Make your decision!\n").lower())

    print()
    if "trash can" in battle_choices:
        sleep(2)
        print("You can't always get what you want can you?")

    if "breastplate" in battle_choices:
        sleep(2)
        print("Covers a good amount of area. Excellent choice!")

    if "sister bff" in battle_choices:
        sleep(2)
        print("You are ruthless!")

    sleep(2)
    hit_spot()

def hit_spot():
    print()
    print("Take your aim and strike!")
    sleep(2)
    print("Where is your first hit gonna land?")
    sleep(2)
    print()
    print("Face")
    sleep(2)
    print("Foot")
    sleep(2)
    print("Unmentionables")
    print()
    sleep(2)

    battle_choices.append(input("Make your decision!\n").lower())
    print()

    if "face" in battle_choices:
        sleep(2)
        print("You are going to actually beat her face, huh?")

    if "foot" in battle_choices:
        sleep(2)
        print("You may not win the fight, but you'll win on the dance floor.")

    if "unmentionables" in battle_choices:
        sleep(2)
        print("*gasp* How dare you?!")

    sleep(2)
    hit_number()

def hit_number():
    print()
    print("How many times are you going to strike?")
    sleep(2)
    print("It's gotta be between 1 and 10 max.")
    print()
    sleep(2)

    battle_choices.append(int(input("Make your decision!\n")))
    num_hits = battle_choices[3]

    print()
    sleep(2)
    for n in range(num_hits):
        sleep(2)
        black = '\033[30m'
        print(black + "Smack!")

    sleep(2)
    dodge()

def dodge():
    print()
    purple = '\033[35m'
    print(purple + "Good hit girl! But you better get prepared.")
    sleep(2)
    print("She's comin' in hot with a baseball bat!")
    sleep(2)
    print("Think quick! How will you dodge?")
    sleep(2)
    print()
    print("Death drop")
    sleep(2)
    print("Juke")
    sleep(2)
    print("Cart-wheel")
    print()
    sleep(2)

    battle_choices.append(input("Make your decision!\n").lower())

    print()
    if "death drop" in battle_choices:
        sleep(2)
        print("You have won all the things. That was sickening!")

    if "juke" in battle_choices:
        sleep(2)
        print("Float like a butterfly, and sting like a bee.")

    if "cart-wheel" in battle_choices:
        sleep(2)
        print("Why do you think you're Simone Biles? Stop that.")

    sleep(2)
    lash_quest()

# Lost and found begins
def lash_quest():
    print()
    print("What a battle! You got in a few good hits.")
    sleep(2)
    print("Were you injured? How's your hair?")
    sleep(2)
    print("Silky smooth as usual... Wait, what's wrong with your face??")
    sleep(2)
    print("OH NO!!! You've lost a lash!")
    sleep(2)
    print("It never stops! It's always the lashes....")
    sleep(2)
    print("No respectable queen performs without lashes. Or worse, just one!")
    sleep(2)
    print("I wonder how your choices so far have affected this...")
    sleep(2)
    print("Can you find your lashes in time for the main stage?")
    print()

    if "sister bff" in users_choice:
        sleep(2)
        print("You gave your second pair to your sister bff.")
        sleep(2)
        print("Could you have dropped a pair while getting a snack?")
        print()

        if "starbucks" in users_choice:
            sleep(2)
            print("Retrace your steps to starbucks? Type y or n.")
            print()
            sleep(2)
            answer = input("Make your decision!\n").lower()
            print()
            if answer == "y":
                sleep(2)
                print("In your mad rush to Starbucks, you got stuck in traffic and missed your performance.")
                sleep(2)
                print("You'll never be a star now...")
                sleep(2)
                game_over()

        elif "mcdonalds" in users_choice:
            sleep(2)
            print("You checked your car but it's not there...")

        sleep(2)
        print("Who will you ask for help?")
        sleep(2)
        print("Your rival")
        sleep(2)
        print("Your bff")
        sleep(2)
        print("Someone else")
        print()
        sleep(2)
        answer = input("Make your decision!\n")
        print()

        if answer == "your bff":
            if "sister bff" in battle_choices:
                sleep(2)
                print("Didn't you try to use her as a human shield?")
                sleep(2)
                print("Not cool.")
                sleep(2)
                game_over()
            else:
                sleep(2)
                print("Your girl has your back too!")
                sleep(2)
                print("She tracks down someone to find some extra lashes!")
                sleep(2)
                success()
        if answer == "someone else":
            if "alley" in users_choice:
                sleep(2)
                print("You asked a friend who you bonded with in the alley")
                sleep(2)
                print("Alley queens unite! She had an extra pair.")
                sleep(2)
                print("You're not sure how sanitary but take the win!")
                sleep(2)
                success()
            if "blue bag" in users_choice:
                sleep(2)
                print("She likes your ", end="")
                blue = '\033[34m'
                purple = '\033[35m'
                print(blue + "blue bag.")
                print(purple + "Great style deserves great lashes.")
                sleep(2)
                success()
            else:
                game_over()
        else:
            if "unmentionables" in battle_choices:
                sleep(2)
                print("After where you hit her?? Are you crazy?")
                sleep(2)
                game_over()

            if int(battle_choices[3]) < 3:
                sleep(2)
                print("You only hit her {} times.".format(battle_choices[3]))
                sleep(2)
                print("Just another Saturday night. She gives you her extras.")
                sleep(2)
                success()
            else:
                game_over()
    else:
        sleep(2)
        print()
        print("You might have an extra pair in your bag.")
        if "red bag" in users_choice:
            sleep(2)
            red = '\033[35m'
            purple = '\033[35m'
            print("No extra lashes in that ", end="")
            print(red + "red bag ")
            print(purple + "but... There's a pb&j in there.")
            sleep(2)
            print("Your rival loves a good sandwich. Bribe her!")
            sleep(2)
            success()
        else:
            sleep(2)
            game_over()
    
def success():
    green  =  '\033[32m'
    print (green + "You found some extra lashes! Great job!", '\033[m')
    exit()

def game_over():
    red =  '\033[31m'
    print (red + "You lost", '\033[m')
    start()

if __name__ == "__main__":
    start()
