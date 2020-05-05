'''
programmanaam:     zodiac
auteur:            Dariush Mirkarimi & Milan Hak
datum:             28-4-2020
functionaliteit:   Neemt als invoer een datum en weergeeft het bijbehorende sterrenbeeld
'''

import datetime
import programs.library as lib

title = lib.title_show('Dieren Ring')

def zodiac():

    '''
    Deze functie controleert bij welk sterrenbeeld de invoer hoort door te kijken of de datum binnen bepaalde waardes valt
    
        1. Invoer van gebruiker halen als een list
        2. De list omzetten in losse invoerwaardes voor dag, maand en jaar
        3. Checken bij welk sterrebeeld de invoer hoort
        
    '''
    
    title()
    while True:  
        while True:
            try:
                #neemt de invoer als een datum
                day,month,year = [int(i) for i in input('Voer hier je geboortedatum in, in het formaat \'dd/mm/jj\' : \n').split('/')]
                break
            except:
                print('Dat is geen geldige datum')


        isValidDate = True
        try :
            #haalt jaar, maand en dag uit elkaar om te kijken welk sterrenbeeld erbij hoort
            datetime.datetime(int(year),int(month),int(day))

            #controleert bij welk sterrenbeeld de invoerdatum hoort
            #door te kijken tussen welke waardes de invoer zit
            if month == 12 and 22 <= day <= 31 or month==1 and 1 <= day <= 19:
                sterrenbeeld = 'Steenbok'

            if month == 1 and 20 <= day <= 31 or month==2 and 1 <= day <= 18:
                sterrenbeeld = 'Waterman'

            if month == 2 and 19 <= day <= 31 or month==3 and 1 <= day <= 20:
                sterrenbeeld = 'Vissen'
            
            if month == 3 and 21 <= day <= 31 or month==4 and 1 <= day <= 19:
                sterrenbeeld = 'Ram'

            if month == 4 and 20 <= day <= 30 or month==5 and 1 <= day <= 20:
                sterrenbeeld = 'Stier'

            if month == 5 and 21 <= day <= 31 or month==6 and 1 <= day <= 20:
                sterrenbeeld='Tweelingen'

            if month == 6 and 21 <= day <= 30 or month==7 and 1 <= day <= 22:
                sterrenbeeld = 'Kreeft'

            if month == 7 and 23 <= day <= 31 or month==8 and 1 <= day <= 22:
                sterrenbeeld = 'Leeuw'

            if month == 8 and 23 <= day <= 30 or month==9 and 1 <= day <= 22:
                sterrenbeeld = 'Maagd'

            if month == 9 and 23 <= day <= 31 or month==10 and 1 <= day <= 22:
                sterrenbeeld = 'Weegschaal'

            if month == 10 and 23 <= day <= 30 or month==11 and 1 <= day <= 21:
                sterrenbeeld = 'Schorpioen'

            if month == 11 and 22 <= day <= 31 or month==12 and 1 <= day <= 21:
                sterrenbeeld = 'Boogschutter'

            #print het sterrenbeeld dat bij de invoerdatum hoort      
            title()
            print('Jouw sterrenbeeld is '+sterrenbeeld)
            
            input('\nDruk op enter om door te gaan')
            break
        #zorgt ervoor dat er geen error komt als iemand een foute datum invoert
        except ValueError :
            print ('Dat is geen geldige datum')    
