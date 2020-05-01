'''
programmanaam:     leapyear
auteur:            Dariush Mirkarimi & Milan Hak
datum:             28-4-2020
functionaliteit:   Gebruikers kunnen checken of jarentallen behoren tot een schrikkeljaar of niet. Ook laat het programma het vorige en volgende schrikkeljaar zien indien mogelijk.
'''

from os import system
import programs.library as lib

title = lib.Title.set_title('Schrikkel Jaar')

def leapyear():


    title()
    
    while True:
        try:
            input_year = lib.dummy_numeric(True, 'Voer hier je jaartal in:')
            if input_year < 1582: raise ValueError('')
            else: break
        except:
            print('Het jaartal mag niet lager zijn dan 1582\n')
    
    title()
    
    #checkt of de invoer een schrikkeljaar is
    #een jaar is een schrikkeljaar als het deelbaar is door 4, tenzij het een eeuwwisseling is want dan moet het deelbaar zijn door 400
    if input_year%4 == 0 and input_year%100 != 0 or input_year%100==0 and input_year%400 == 0:
        print('{input year} is een schikkeljaar.'.format(input_year))
    else:
        print('{input year} is geen schikkeljaar.'.format(input_year))
        
    #loopt terug vanaf de invoer om het vorige schrikkeljaar te vinden
    for test_year in range(input_year-1, input_year-8, -1):
        if test_year < 1582:
            print('Er zijn geen kleinere schikkeeljaren volgens de Gregoriaanse kalender')
            break
        if test_year%4 == 0 and test_year%100 != 0 or test_year%100==0 and test_year%400 == 0:
            print('{previous leapyear} is het vorige schikkeljaar.'.format(test_year))
            break
    
    #loopt vooruit vanaf de invoer om het volgende schrikkeljaar te vinden
    for test_year in range(input_year+1,input_year+8):
        if test_year%4 == 0 and test_year%100 != 0 or test_year%100==0 and test_year%400 == 0:
            print('{next leapyear} is het eerstvolgende schikkeljaar.'.format(test_year))
            break

    #zorgt ervoor dat de gebruiker op enter kan drukken om terug naar hoofdmenu te gaan
    input('\nDruk op enter om door te gaan') 
