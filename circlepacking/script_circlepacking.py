from os import name
import pandas as pd
import json

# On combine les deux fichiers CSV client
combined_clients = pd.concat([pd.read_csv("../Clients_0.csv", encoding='latin-1'), pd.read_csv("../Clients_8.csv", encoding='latin-1')])

# On recupere le fichier Immatriculations.csv
immatriculations = pd.read_csv("../Immatriculations.csv", encoding='latin-1')

# On combine les deux dataframes selon la colonne commune qui est "immatriculation"
combined_client_and_immatriculation = pd.merge(combined_clients[['sexe', 'immatriculation']], immatriculations[['immatriculation', 'marque', 'nom']], on='immatriculation')

# On nettoye les donnees
combined_client_and_immatriculation['sexe'].replace({
        'Féminin': 'F',
        'Femme': 'F',
        'Homme': 'M',
        'Masculin': 'M',
        'N/D': '?',
        ' ': '?',
    }, inplace=True)
combined_client_and_immatriculation = combined_client_and_immatriculation[combined_client_and_immatriculation['sexe'] != '?']
combined_client_and_immatriculation = combined_client_and_immatriculation[:50]
# Traitement
data = []
for index, row in combined_client_and_immatriculation.iterrows():
    if row['sexe'] == 'M':
        newMarque = True
        newModele = False
        for d in data:
            if d['name'] == row['marque']: # Si la marque n'est pas nouvelle
                print("Marque : " + d['name'])
                print("Test : " + row['marque'])
                newMarque = False
                for e in d['children']: # Pour chaque modele de la marque
                    print("Modele : " + str(e))
                    print("Test : " + row['nom'])
                    if e['name'] == row['nom']: # Le modele existe deja
                        e['size'] = int(e['size']) + 1 # On ajoute 1 au nombre de ce modele
                        print("Increase size : " + str(e['size']))
                    else: # Le modele n'existe pas
                        newModele = True
                if newModele: # On ajoute le modele a la marque
                    d['children'].append({'name': row['nom'], 'size': 1})
        if newMarque: # Si la marque est nouvelle on l'ajoute
            data.append({'name': row['marque'], 'children': [{'name': row['nom'], 'size': 1}]})

print(data)

# data_into_json = combined_client_and_immatriculation.to_json()
# with open("data.json", "w") as outfile:
#     json.dump(combined_client_and_immatriculation.to_json(), outfile)