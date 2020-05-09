'''
programmanaam:     leapyear
auteur:            Dariush Mirkarimi & Milan Hak
datum:             28-4-2020
functionaliteit:   Gebruikers kunnen checken of jaartallen behoren tot een schrikkeljaar of niet. Ook laat het programma het vorige en volgende schrikkeljaar zien indien mogelijk.
'''

from os import system
import programs.library as lib

title = lib.title_show('Schrikkeljaar')

def leapyear():

    '''
    Deze functie controleerd of een invoer een schrikkeljaar is of niet door te checken of het deelbaar is door 4, is dit het geval dan is het getal een schrikkeljaar.
    Is het getal deelbaar door 100 dan moet het deelbaar zijn door 400 om een schrikkeljaar te zijn
    Omdat in de Gregoriaanse calender pas schrikkeljaren zijn vanaf 1582 gaat het programma ook niet verder terug dan 1582.
    '''

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
        print(f'{input_year} is een schrikkeljaar.')
    else:
        print(f'{input_year} is geen schrikkeljaar.')
        
    #loopt terug vanaf de invoer om het vorige schrikkeljaar te vinden
    for test_year in range(input_year-1, input_year-8, -1):
        if test_year < 1582:
            print('Er zijn geen kleinere schikkeeljaren volgens de Gregoriaanse kalender')
            break
        if test_year%4 == 0 and test_year%100 != 0 or test_year%100==0 and test_year%400 == 0:
            print(f'{test_year} is het vorige schrikkeljaar.')
            break
    
    #loopt vooruit vanaf de invoer om het volgende schrikkeljaar te vinden
    for test_year in range(input_year+1,input_year+8):
        if test_year%4 == 0 and test_year%100 != 0 or test_year%100==0 and test_year%400 == 0:
            print(f'{test_year} is het eerstvolgende schrikkeljaar.')
            break

    #zorgt ervoor dat de gebruiker op enter kan drukken om terug naar hoofdmenu te gaan
    input('\nDruk op enter om door te gaan') 
