import mysql.connector
import requests
from requests.structures import CaseInsensitiveDict


# Coonexion à la base de données
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd = '')


# Vérification de la connexion à la base de données
if(mydb):
    cursor = mydb.cursor()

    ################################################################################################################

    cursor.execute("SELECT customer_id, COUNT(*) AS num FROM dataengineer.rental GROUP BY customer_id ORDER BY num DESC LIMIT 1")
    donnees_table_rental = cursor.fetchall()

    id_meilleur_client = donnees_table_rental[0][0]
    nombre_de_locations = str(donnees_table_rental[0][1])

    ################################################################################################################

    cursor.execute("SELECT * FROM dataengineer.customer WHERE customer_id ="+str(id_meilleur_client))
    donnees_table_customer = cursor.fetchall()

    prenom = donnees_table_customer[0][2]
    nom = donnees_table_customer[0][3]
    id_adresse = donnees_table_customer[0][5]

    ################################################################################################################

    cursor.execute("SELECT * FROM dataengineer.address WHERE address_id = " + str(id_adresse))
    donnees_table_adresse = cursor.fetchall()

    adresse_num = str( donnees_table_adresse[0][1] )
    adresse_ville = str( donnees_table_adresse[0][2] )
    adresse_cp = str( donnees_table_adresse[0][3] )
    adresse_latitude = str( donnees_table_adresse[0][4] )
    adresse_longitude = str( donnees_table_adresse[0][5] )


    print("Données du client ayant effectué le plus de locations :")
    print("Nom : " + nom)
    print("Prénom : " + prenom)
    print("Nombre de locations : " + nombre_de_locations)
    print("Adresse : " + adresse_num + " " + adresse_cp + " " + adresse_ville)
    print("Latitude : " + adresse_latitude)
    print("Longitude : " + adresse_longitude)







