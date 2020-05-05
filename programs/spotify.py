'''
programmanaam:     spotify
auteur:            Dariush Mirkarimi & Milan Hak
datum:             28-4-2020
functionaliteit:   Laat met behulp van SQL-queries gebruikers zoeken en luisteren naar nummers uit een database
'''

import mysql.connector
import programs.library as lib
import webbrowser


title = lib.title_show('Spotify')


def spotify():


    '''
    Functie die ervoor zorgt dat het programma nummers kan ophalen uit een SQL-database, gehost door remotemysql.com.
    De gebruiker kan desbetreffende nummers daarna afspelen in de standaard webbrowser op het systeem.
    '''
    
    #in een loop zodat je nog een liedje kan zoeken als je er al eentje hebt afgespeeld
    while True:
        
        title()
        #de database op https://remotemysql.com/phpmyadmin verbinden met het programma
        mydb = mysql.connector.connect(
          host='remotemysql.com',
          user='zZ591I7Nne',
          passwd='qTbLGCG2YI',
          database='zZ591I7Nne'
        )

        #cursor is een functie van de mysql module die ervoor zorgt dat je met python query's kan uitvoeren
        cursor = mydb.cursor()
        search = input('Type een zoekterm. Laat leeg voor een volledige lijst. Type \'terug\' om terug te gaan:\n')
        title()
        #zorgt ervoor dat de gebruiker terug kan aan naar het main menu door terug in te voeren
        if search == 'terug':
            break

        print('Liedjes:\n')
        #haalt de gerelateerde liedjes op uit de database m.b.v. een query
        cursor.execute('SELECT songs.title, group_concat(artists.name SEPARATOR \', \') FROM ((main INNER JOIN artists ON main.artist_id = artists.artist_id) INNER JOIN songs ON main.song_id = songs.song_id) WHERE songs.title like %s or artists.name like %s GROUP BY songs.title',('%'+search+'%','%'+search+'%'))

        #toont de resultaten van de query en maakt er een list van
        
        song_results = []

        for c,x in enumerate(cursor,1):
        
            print('{}.{}-{}'.format(c,x[0],x[1]))
            song_results.append(x)

        #maakt een lijst met de mogelijke opties zodat er niet een niet bestaande optie wordt gekozen
        if song_results:
            choice = lib.dummy_list(lib.str_list(range(1,len(song_results)+1))+['terug'],'\nKies een optie, of type \'terug\' om terug te gaan:')
            try:
                choice=int(choice)
                #haalt de url van het nummer op
                cursor.execute('SELECT song_url from songs where title = %s',(song_results[choice-1][0],))
                output = cursor.fetchone()
                #opent de url in de standaard webbrowser
                webbrowser.open(output[0])
            except:
                pass
        else:
            print('n.v.t')
            input('\nWe hebben niks kunnen vinden. Druk op enter om opnieuw te zoeken')

