import time
import random


def print_pause(words):
    print(words)
    time.sleep(3)


def intro():
    print_pause("Let's begin your adventure.\n")
    full_name = input("What is your full name?\n\n")
    name = full_name.split(" ")
    names.extend(name)


def valid_input2(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print("Sorry, please make a valid entry.")
    return response


def valid_input3(prompt, option1, option2, option3):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        elif option3 in response:
            break
        else:
            print("Sorry, please make a valid entry.")
    return response


def first_choice2():
    if "a" in items:
        print_pause("\nLet's try this again\n")
        response = valid_input3("1. Rever Encore.\n2. "
                                "Unessential Insanities.\n"
                                "3. Residue of Regret. \n"
                                "(Pick a number)\n\n", "1",
                                "2", "3")
        if "1" in response:
            a()
        elif "2" in response:
            b()
        elif "3" in response:
            c()
    else:
        print_pause("\nLet's try this again\n")
        response = valid_input3("1. Reverie.\n2. ESSENTIAL "
                                "Insanities.\n3. Residue "
                                "of regret.\n(Pick a number)\n\n",
                                "1", "2", "3")
        if "1" in response:
            a()
        elif "2" in response:
            b()
        elif "3" in response:
            c()


def first_choicec():
    print_pause("\nLet's find something suitable.\n")
    print_pause("Start by judging a book by it's cover, or "
                "rather an adveture by its name. \n")
    response = valid_input2("1. Reverie.\n2. Unessential Insanitie"
                            "s.\n\n", "1", "2")
    if "1" in response:
        a()
    elif "2" in response:
        b()


def first_choice():
    print_pause("\nLet's find something suitable "
                "for your taste.\n")
    print_pause("Start by judging a book by "
                "it's cover, or rather an adventure "
                "by its title. \n")
    response = valid_input3("1. Reverie.\n2. Unessential "
                            "Insanities.\n3. Residue of Regret.\n"
                            "(Pick a number)\n\n", "1", "2", "3")
    if "1" in response:
        a()
    elif "2" in response:
        b()
    elif "3" in response:
        c()


def second_choice():
    response = valid_input2("""\nWhich one will you choose?
    E
    M
    """, "e", "m",)
    while True:
        if "e" in response:
            e()
            break
        elif "m" in response:
            m()
            break


def over():
    response = valid_input3("""Would you like to play again?
    (yes, no or from scratch.)\n\n""", "yes", "no", "from scratch")
    if "yes" in response:
        first_choicec()
    elif "no" in response:
        print("\nGoodbye")
    elif "from scratch" in response:
        items.clear()
        intro()
        first_choice()


def begin_again():
    response = valid_input3("""Would you like to start again?
    (yes, no, or from scratch.)\n\n""", "yes", "no", "from scratch")
    if "yes" in response:
        first_choice2()
    elif "no" in response:
        print("goodbye")
    elif "from scratch" in response:
        items.clear()
        intro()
        first_choice()


def interlude():
    print_pause("\nYou head for the door but it seems to be locked.\n")
    print_pause("Then, someone appears out of nowhere...\n")
    print_pause("They hold out two keys, one engraved with an 'E', "
                "and the other with a 'M'")


def dream():
    print_pause("\nYou start to drift off but suddenly "
                "an earthquake wakes you!")
    interlude()


def a():
    name = random.choice(names)
    print_pause(f"\nIn the mood for a dream, {name}...\n")
    time.sleep(2)
    print_pause("As you look up, is seems as "
                "if the trees are reaching up to the sky.\n")
    print_pause("You turn to the left and find a stump "
                "with the word 'fable'\n ")
    print_pause("You wake up in a coffee shop.\n")
    print_pause("But how did you get here?\n")
    response = valid_input2("""Do you...
    1. Fall back asleep?
    2. Get your things together and leave?
    (pick 1, or 2)

    """, "1", "2")
    if "1" in response:
        dream()
    elif "2" in response:
        interlude()
    items.append("a")
    second_choice()


def b():
    name = random.choice(names)
    books = ["In the Woods", "The Lost Constellation", "The "
             "Invisible Growth"]
    book = random.choice(books)
    print_pause("\nAs you make your way into the "
                "coffee shop you see three books "
                "on the table\n")
    print_pause(f"you pick one up. Its titled '{book}'\n")
    print_pause("When you open it a note falls out. "
                f"It reads '{name}, Every entry is an exit.' \n")
    print_pause("All of a sudden you get a weird feeling in your stomach.\n")
    print_pause("You head for the door.\n")
    print_pause("When you try to open it, it's locked!\n")
    print_pause("Then, someone appears out of nowhere...\n")
    print_pause("They hold out two keys, one engraved with "
                "an 'E', and the other with a 'M'")
    items.append("b")
    second_choice()


def c():
    name = random.choice(names)
    print_pause("\nUnfortunatly, this adventure "
                f"is no longer running, {name}.\n")
    print_pause("The regret slowly dissolved all the magic.\n")
    print_pause("I'm sorry this game is over for you.\n")
    print_pause("The next one might be better suited.\n")
    items.append("c")
    over()


def e():
    name = random.choice(names)
    if "a" and "b" in items:
        print_pause(f"\nGood choice, {name}\n")
        print_pause("You found the clues in the dream and the note.\n")
        print_pause("You saw the word 'fable' which has 5 letters\n")
        print_pause("The fifth letter of the alphabet is an E.\n")
        print_pause("You also must have noticed all of "
                    "the 'E's in the note that fell out of the book\n")
        over()

    elif "a" in items:
        print_pause(f"\nGood choice, {name}\n")
        print_pause("That was an important dream.\n")
        print_pause("You saw the word 'fable' which has 5 letters\n")
        print_pause("The fifth letter of the alphabet is an E.\n")
        print_pause("You made it out!\n")
        over()
        items.append("e")

    elif "b" in items:
        name = random.choice(names)
        print_pause(f"\nGood choice, {name}\n")
        print_pause("""It must have been fate, you picked
         up the book with the note 'Every entry is an exit'\n""")
        print_pause("What a strange note, you must "
                    "have noticed whoever wrote it knew that 'E' would "
                    "be an important letter for you\n")
        over()
        items.append("e")


def m():
    if "a" and "b" in items:
        print_pause("\nThis key doesn't seem to fit. \n")
        print_pause("Look back on your dream, and the note "
                    "you found they should have some clues.\n")
    elif "a" in items:
        print_pause("\nThis key doesn't seem to fit.\n")
        print_pause("Your dream should have clue.\n")
    elif "b" in items:
        print_pause("\nThis key doesn't seem to fit.\n")
        print_pause("Think about the note that fell out "
                    "of the book.\n")
        print_pause("It might have some clues\n")
    print_pause("Let's try from the beginning.\n")
    begin_again()


names = []
items = []
intro()
first_choice()
