import mysql.connector
import requests
from requests.structures import CaseInsensitiveDict

# geocode_nominatim :
# Fonction prennant en parametre Numéro municipal, la ville et le code postal
# Elle retourne  un json comprenant en autres la latitide (lat) et la longitude (lon)

def geocode_nominatim(street,city,postal_code):
    parameters = {
        "street": street,
        "city": city,
        "postalcode": postal_code,
        "country": "France",
        "format": "jsonv2",
    }

    url = "https://nominatim.openstreetmap.org/search.php"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    resp = requests.get(url, headers=headers, params=parameters)
    return resp


# Coonexion à la base de données
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd = '')

# Initilisation de la variable servant à afficher la progression
i = 0

# Vérification de la connexion à la base de données
if(mydb):

    cursor = mydb.cursor()
    cursor.execute("SELECT * from dataengineer.address")
    result = cursor.fetchall()

    # Ittération de toutes les lignes de la table address de la base de données
    for row in result:

        # Affectation des valeures respectives pour les différentes variables
        adresse = row[1]
        ville = row[2]
        code_postal = row[3]

        # Résultat de la requête API
        reponse = geocode_nominatim(adresse,ville,code_postal)

        # Vérifier que la réponse de l'API ne soit pas vide afin d'éviter un arret du script
        if (reponse.status_code == 200 and len(reponse.json()) > 0):
            rslt = (reponse.json()[0])

            #Requete SQL mettant à jour la latitude et la longitude de la l'adresse concernée
            cursor.execute("UPDATE dataengineer.address SET latitude ='" + rslt['lat'] + "',  longitude ='" + rslt['lon'] + "' WHERE address_id = " + str(row[0]))
            mydb.commit()

        # Affichage de la progression
        print("progression : "+str(round((i+1)/len(result)*100,2))+"%")

        # Incrémentation de la variable de progression
        i = i +1

else:
    print('Echec de la connexion à la base de données')