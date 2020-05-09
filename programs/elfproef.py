'''
programmanaam:     elfproef
auteur:            Dariush Mirkarimi & Milan Hak
datum:             28-4-2020
functionaliteit:   Gebruikers kunnen checken of een BSN geldig kan zijn. Ook laat het programma het volgende geldige BSN zien indien mogelijk.
'''

import programs.library as lib

title = lib.title_show('Elf Proef')

#checkt of de invoer voldoet aan de elfproef
def elfproef_check(BSN): 

    '''
    Functie die checkt of een gegeven 9-cijferig nummer voldoet aan de elfproef en dus een geldig BSN kan zijn.
    Geeft als returnwaarde een boolean.
    STAPGEWIJZE BESCHRIJVING:
    
    1. Er wordt een list gemaakt van 9 tot en met 1. De laatste waarde is hierbij als uitzondering negatief.
    2. Invoer "BSN" wordt omgezet in een list.
    3. Beide lists worden samengevoegd, waardoor er één nieuwe list wordt gevormd. Variabelen met dezelfde index vormen tuples.
    4. Er wordt met een list comprehension weer een nieuwe array gemaakt die bestaan uit het product van de individuele tuples.
    5. De som van alle producten in de list wordt genomen.
    6. Als de modulus van de som gedeeld door 11 gelijk is aan nul, is de returnwaarde True, zo niet is de returnwaarde False
    
    '''
    
    return sum([y*z for y,z in zip([*range(9,1,-1)]+[-1], [int(x) for x in BSN])]) % 11 == 0


def elfproef():

    ''' Dit is de hoofdfunctie van dit bestand. Het zorgt ervoor dat de gebruiker een BSN  kan laten checken.
    Foute invoer waardes worden afgehandeld. Als het BSN niet aan de elfproef voldoet word het eerstvolgende BSN nummer
    dat wel aan de proef voldoet getoond 
    
    '''

    title()
    
    #neemt de input en checkt voor juiste lengte
    input_BSN = lib.length_check(lib.dummy_numeric, 9, [True, 'Voer hier je BSN in:', 'Dat is geen geldige waarde!', True])
    
    title()

    #als de invoer voldoet aan elfproef wordt dit geprint, zo niet laat het dat ook weten
    if elfproef_check(input_BSN): print(input_BSN+' is een geldig BSN')
    else: 
        print(input_BSN+' is geen geldig BSN')
        

        #gaat vooruit op de invoer, checkt of deze geldig is en print het volgende geldige BSN
        for test_BSN in lib.number_gen(int(input_BSN),'add'):
        
            test_BSN_string = str(test_BSN)
            #voegt een 0 toe aan het begin van de BSN als deze 8 karakters lang is i.p.v. 9
            if len(test_BSN_string) == 8:
                test_BSN_string = '0'+test_BSN_string

            #voert elfproef uit op de tijdelijke BSN, als het er niet aan voldoet herhaalt de loop
            #en als het wel voldoet wordt het geldige BSN geprint
            
            
            if elfproef_check(test_BSN_string): 
                print(test_BSN_string+' is het eerst volgende geldige BSN')
                break
        
    #zorgt ervoor dat de gebruiker terug gaan naar het hoofdmenu door op enter te drukken      
    input('\nDruk op enter om door te gaan') 
