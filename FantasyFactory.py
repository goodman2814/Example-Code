import random
import os
import art

races = ["Elf", "Orc", "Dwarf", "Human", "Gnome", "Avian", "Dragon", "Ent"]
syllables = ['er', 'ak', 'we', 'ori', 'no', 'ba', 'lak', 'tre', 'los', 'of', 'zer', 'vi', 'is', 'ga', 'fo', 'ti', 'ia', 'ris', 'col', 'ki', 'us', 'al', 'ex', 'sio', 'ned', 'fus', 'roh', 'dah']
occupations = ['Builder', 'Blacksmith', 'Farmer', 'Guard', 'Sheriff', 'Accountant', 'Ranger', 'Taxidermist', 'Lawyer', 'Archer', 'Spy']

os.system('cls' if os.name == 'nt' else 'clear')

art.tprint('Welcome to the FANTASY FACTORY')

user_input = ''

while user_input != 'exit':
    user_input = input("Press any key to generate your NEW character!\nOr\nType \"exit\" to quit: ")
    if user_input == "exit":
        art.tprint('Thanks for Playing!')
        break
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    new_race = random.choice(races)
    print('{0:<10} {1:<30}'.format('Race:', new_race.capitalize()))

    
    num = random.randint(3, 5)
    first_name = ''
    last_name = ' '

    for i in range(num):
        first_name = first_name + random.choice(syllables)

    num = random.randint(3, 6) 

    for j in range(num):
        last_name = last_name + random.choice(syllables)

    final_name = first_name + last_name
 
    print('{0:<10} {1:<30}'.format('Name:', final_name.capitalize()))      

    job = random.choice(occupations)

    town = ''
    num = random.randint(2, 5)
    for k in range(num):
        town = town + random.choice(syllables)
    
    city_end = ["burg", "ton", "ville", " City"]

    home = town + random.choice(city_end)

    print('{0:<10} {1:<30}'.format('Town', home.capitalize()))

    print('{0:<10} {1:<30}'.format('Occupation:', job.capitalize()))

    print()


