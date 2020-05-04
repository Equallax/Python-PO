'''
programmanaam:     menu
auteur:            Dariush Mirkarimi & Milan Hak
datum:             28-4-2020
functionaliteit:   Een text-based interface waar de gebruiker het gewenste programma mee kan openen
'''

# importeert alle benodigde modules
import programs.library as lib
import webbrowser
import winsound
import programs.primenumber as prime
import programs.leapyear as leap
import programs.solarsystem as solarsystem
import programs.zodiac as zodiac
import programs.elfproef as elfproef
import programs.spotify as spotify
import matplotlib.pyplot as plt
from os import system

title = lib.Title.set_title('Hoofd Menu')

aantal_opties = 7

#het startmenu
def menu():
    #print alle opties
    title()
    
    print('1. Priemgetal')
    print('2. Schrikkeljaar')
    print('3. Dieren Ring')
    print('4. Zonnestelsel')
    print('5. Elfproef')
    print('6. Spotify')
    print('7. Sluiten\n')
    #haalt de user input op als int d.m.v. de input check module
    choice = int(lib.dummy_list(lib.str_list(range(1,aantal_opties+1)),'Kies een optie:'))
    #zorgt ervoor dat het gekozen programma wordt geopend
    if choice == 1:
        prime.primenumber()
    elif choice == 2:
        leap.leapyear()
    elif choice == 3:
        zodiac.zodiac()
    elif choice == 4:
        plt.show()
    elif choice == 5:
        elfproef.elfproef()
    elif choice == 6:
        spotify.spotify()    
    elif choice == 7:
        exit()

while True:
    menu()
