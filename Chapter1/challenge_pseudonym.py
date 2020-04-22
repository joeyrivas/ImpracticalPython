"""Generate funny names by randomly combinin names from 2 separate lists."""
import random
import sys


def main():
    """Choose names at random from 2 tuples of names and print to screen."""
    print("Welcome to the Psych Sidekick Name Picker.'\n'")
    print("A name just like Sean would pick for Gus:\n\n")

    first = ('Alex', 'David', 'Lucas', 'Bill', 'Anthony'
             'Bob', 'Beau', 'Alberto', 'Bud',
             'Billy', 'Brewster', 'Bruce', 'Chad', 'Chester',
             'Chewy', 'Cooter', 'Bobby', 'Cletus', 'Corey',
             'Richard', 'Craig', 'Derek', 'Dennis',
             'Dick', 'Alphonso', 'Nancy', 'Finn', 'Francis', 'Gene',
             'Jim', 'Hank', 'Hugh', 'Ignatious', 'Jim',
             'Joseph', 'Johnny', 'Jackson', 'Deborah',
             'Lee', 'Louis', 'Mike', 'Paul',
             'Kenneth', 'Oscar', 'Ollie', 'Oliver', 'Penny',
             'Ben', 'Pete', 'Phil', 'Candy',
             'Frank', 'Marvin', 'Scout', 'Sid',
             'Keith', 'Susan', 'Kyle', 'Oscar', 'Neal', 'Shirley',
             'Spitz', 'Sam', 'Sue', 'Steven', 'Tevin',
             'Tony', 'Joe', 'Winston', 'William')

    middle = ('Baby Oil', 'Bad News', 'Big Burps', 'Beenie-Weenie',
             'Stinkbug', 'Bowel Noises', 'Boxelder', 'Lite',
             'Butterbean', 'Buttermilk', 'Buttocks', 'Chewy', 'Chigger',
             'Cinnabuns', 'Cornbread', 'Crab Meat', 'Crapps', 'Dark Skies',
             'Clawhammer', 'Dicman', 'Fancypants', 'Figgs', 'Foncy', 'Gootsy',
             'Greasy', 'Huckleberry', 'Huggy', 'Pottin Soil', 'Lemongrass',
             'Lil Devil', 'Longbranch', '"Lunch Money"', 'Megatroid',
             '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine',
             'Pennywhistle', 'Pitchfork', 'Potato Bug', 'Pushmeet',
             'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut', '"The Squirts"',
             'Skidmark', 'Slaps', 'Snakes', 'Snoobs', 'Snorki', 'Soupcan',
             'Spitzitout', 'Squids', 'Stinky', 'Storyboard', 'Sweet Tea',
             'TeeTee', 'Wheezy', 'Jazz Hands', 'Worms')

    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
            'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
            'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple',
            'Goodensmith', 'Goodpasture', 'Guster', 'Henderson', 'Hooperbag',
            'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins',
            'Jingley-Schmidt', 'Johnson', 'Kingfish', 'Listenbee', "M'Bembo",
            'McFadden', 'Moonshine', 'Nettles', 'Noseworthy', 'Olivetti',
            'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler', 'Pealike',
            'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton', 'Porkins',
            'Putney', 'Quakenbush', 'Rainwater', 'Rosenthal', 'Rubbins',
            'Sackrider', 'Snuggleshine', 'Splern', 'Stevens', 'Stroganoff',
            'Sugar-Gold', 'Swackhamer', 'Tippins', 'Turnipseed',
            'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax', 'Weiners',
            'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
            'Woolysocks')

    while True:

        first_name = random.choice(first)

        last_name = random.choice(last)

        if random.random() < .1:
            middle_name = ' ' + random.choice(middle)
        else:
            middle_name = ''

        print("\n\n")
        print("{}{} {}".format(first_name, middle_name, last_name), file=sys.stderr)
        print("\n\n")

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")


if __name__ == "__main__":
    main()
