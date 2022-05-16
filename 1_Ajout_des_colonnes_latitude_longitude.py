import mysql.connector

# Coonexion à la base de données
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd = '')

# Vérification de la connexion à la base de données
if(mydb):

    cursor = mydb.cursor()
    cursor.execute("ALTER TABLE  dataengineer.address ADD COLUMN latitude DECIMAL(10,8) NULL DEFAULT NULL, ADD COLUMN longitude DECIMAL(11,8) NULL DEFAULT NULL")
    mydb.commit()
    print("Création des colonne Latitude et longitude dans la table address terminée")

else:
    print('Echec de la connexion à la base de données')