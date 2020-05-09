'''
programmanaam:     primenumbers
auteur:            Dariush Mirkarimi & Milan Hak
datum:             28-4-2020
functionaliteit:   Gebruikers kunnen checken of getallen priem zijn of niet. Ook laat het programma het vorrige en volgende priem getal zien indien mogelijk.
'''

import math
from os import system
import programs.library as lib

title = lib.title_show('Priem Getal')

def primenumber():

    '''
    Deze functie controleert of een getal een priemgetal is door te checken of het deelbaar is door zichzelf of door 1, als dit het geval is is het een priemgetal.
        1. Invoer van de gebruiker halen
        2. Controleert of de invoer een priemgetal is en print dit
        3. Vindt het vorige en volgende priemgetal en print deze
    '''
    
    title()
    
 
    #checkt of een getal een priemgetal
    def PrimeCheck(input_number):
        
        prime = True
        if input_number == 2: prime=True
        else:
            #zorgt ervoor dat je alleen checkt tot de wortel van input_number
            p = math.ceil(input_number**0.5)
            #een for loop om het getal te delen door 1 tot p en kijken of er een rest overblijft
            for i in range(1,p+1):        
                #als er geen rest is dan is het deelbaar door iets anders dan 1 of zichzelf en dus geen priem
                if input_number%i == 0 and i!=1:
                    prime = False
                    break
                    
        return prime
    
    
    input_number = lib.dummy_numeric(True, 'Voor je natuurlijke getal hier in:', negative_allowed=False)

    #checkt of de invoer een priemgetal is door het door de PrimeCheck functie heen te laten gaan
    if PrimeCheck(input_number): 
        print(f'{input_number} is een priemgetal')
    else: 
        print(f'{input_number} is geen priemgetal')
    
    #loopt terug vanaf de invoer om het vorige priemgetal te vinden door bij elke iteratie de verlaagde waarde door de PrimeCheck functie te laten gaan
    for temp in lib.number_gen(input_number,'subtract'):
        
        if temp<=0: 
            print(f'Er is geen priemgetal, kleiner dan {input_number}')
            break 
            
        if PrimeCheck(temp):
            print(f'{temp} is het vorige priemgetal')
            break
    
    #loopt verder vanaf de invoer om het volgende priemgetal te vinden door bij elke iteratie de verhoogde waarde door de PrimeCheck functie te laten gaan
    for temp in lib.number_gen(input_number,'add'):
        
        if PrimeCheck(temp):
            print(f'{temp} is het volgende priemgetal')
            break
        
    #zorgt ervoor dat de gebruiker terug kan gaan naar het hoofdmenu door op enter te drukken
    input('Druk op enter om door te gaan')            
