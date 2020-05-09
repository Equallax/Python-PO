'''
programmanaam:     library
auteur:            Dariush Mirkarimi & Milan Hak
datum:             28-4-2020
functionaliteit:   Een grote collectie aan functies en een class die veel gebruikt worden door onze andere programma's. 
'''

from os import system


def dummy_list(values, input_text='Voer hier je waarde in: ', error='Dat is geen geldige waarde!'):
    '''
    Deze functie checkt of de invoer van de gebruiker binnen de mogelijke opties valt. Foute invoer waardes worden afgehandeld.
    
    ARG BESCHRIJVING:
        values:             Lijst met mogelijke waardes
        input_text:         Stel een aangepaste invoermelding in
        error:              Stel een aangepaste foutmelding in
        
    '''
    
    while True:
        invoer = input(input_text+'\n')
        if invoer in values:
            break;
        else:
            print(error+'\n')        
    return invoer


def dummy_numeric(exclusive=False, input_text='Voer hier je waarde in: ', error='Dat is geen geldige waarde!', string_output=False, negative_allowed=True):

    '''
    Deze functie check of de invoer van de gebruiker voldoet aan de gestelde eisen.
    De hoofdeis is hierbij dat de invoer van de gebruiker een int of float moet zijn
    
    ARG BESCHRIJVING:
        exclusive:          Alleen integers worden geaccepteerd
        input_text:         Stel een aangepaste invoermelding in
        error:              Stel een aangepaste foutmelding in
        string_output:      Output van de functie moet als string worden gegeven
        negative_allowed:   Negatieve getallen worden geaccepteerd
    
    '''

    
    #als bij het callen van de functie exclusive op true is gezet returnt de functie een integer
    #als bij het callen van de functie exclusive op false blijft returnt de functie een float, mits een integer niet kan
    while True:
        invoer = input(input_text+'\n')
        try:
            if exclusive:  data=int(invoer)
            else: data=float(invoer)

            if not negative_allowed and data<1: raise Exception()
            break;
        except:
            print(error+'\n')
                
    
    #returnt een gevalideerde als een string zodat nullen vooraan niet wegvallen, anders wordt bijvoorbeeld str(int('0010')) = '10'        
    if string_output:
        return invoer
    #als string_output false blijft returnt de functie de invoer als een integer of float            
    else:
        return data
    
    
def length_check(input_function, desired_length , function_args=None):
    '''
    Deze functie checkt de lengte van de returnwaarde van een andere functie de juiste lengte heeft. Zo niet word er een error geprint en de andere functie opnieuwd gerunt.
    
    ARG BESCHRIJVING:
        input_function:     functie waar de check op moet worden uitgevoerd
        desired_length:     de gewenste lengte van de waarde die de input_function returnt
        funtion_args:       OPTIONEEL: Variabelen die de input_function gebruikt 
        
    '''

    while True:
            user_input = input_function(*function_args)
            if len(str(user_input)) == desired_length:
                return user_input
                break;
            else:
                print(f'De invoer moet bestaan uit {desired_length} cijfer, maar {len(str(user_input))} waren gegeven\n')
    
    

def str_list(input_list):
    '''Zet een list met allerlei type variabelen om in een list die bestaat uit strings. '''
    return [str(x) for x in input_list]


def clear():
    '''Maakt het console leeg voor het volgende scherm. '''
    system('cmd /c "cls"')

    
def title_show(name):
    '''Zorgt ervoor dat de titel van het huidige programma mooi in beeld komt maar niet voordat het, het console leegmaakt. '''
    
    def show():
        line_one = '---------[{}]---------'.format(name)
        clear()
            
        print(line_one)
        print('‾'*len(line_one))
     
    return show
        
        
        

def number_gen(start_number, choice):

    ''' Deze functie neemt als invoer een nummer. Hiermee kan daarna in een for-loop elke iteratie een nieuw nummer als output worden gegeven.
    
    ARG BESCHRIJVING:
        start_number:       Beginwaarde van de functie
        choice:             Stelt in of de operator += of -= moet zijn
        
    
    Voorbeeld:
    
    for i in number_gen(100000001, 'add'):
    
        if i < 100000005:
            print(i)
        else:
            break
    
    OUTPUT:
    
    100000002
    100000003
    100000004
  
    '''

    current_number = start_number
    
    if choice == 'add':
        while True:
            current_number+=1
            yield current_number
            
    elif choice == 'subtract':
        while True:
            current_number-=1
            yield current_number
    else:
        Exception('No valid choice given')