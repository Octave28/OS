import os 
from pathlib import Path
from typing import List
import sys
import locale

# Fonction pour créer des dossiers et des fichiers
def generer_dossier_fichiers(path : str) -> None:
    """
    Crée une structure de dossiers pour les 12 mois en français avec 15 fichiers numérotés dans chaque dossier.

    :param base_path: Chemin du répertoire de base où créer la structure.
    """
    try:
        # Création du répertoire de base
        repertoire = Path(path)

        if not repertoire.exists():
            repertoire.mkdir(parents=True, exist_ok=True)
            #print(f"Répertoire créé avec succes : {repertoire}")

        # Noms des mois en français
        moisdelannee = [
            "01-janvier", "02-février", "03-mars", "04-avril",
            "05-mai", "06-juin", "07-juillet", "08-août",
            "09-septembre", "10-octobre", "11-novembre", "12-décembre"
        ]

        # Création des sous-dossiers et fichiers
        for mois in moisdelannee:
            sous_repertoire = repertoire/moisdelannee
            if not sous_repertoire.exists():
                sous_repertoire.mkdir()
                
            # Création des fichiers dans le sous-dossier
            for i in range(1, 16):
                fichier = f"log{i:02d}.txt"
                path_fichier = sous_repertoire/fichier
                if not path_fichier.exists():
                    path_fichier.touch()
                    #print(f"Fichier créé : {path_fichier}")

    except PermissionError:
        print("Erreur ! : vous n'êtes pas autorise a creer des items dans ce dossier .")
    except FileNotFoundError:
        print("Erreur ! : le chemin spécifié n'existe pas.")
    except OSError as e:
        print(f"Erreur liée au système d'exploitation : {e}")
    except Exception as e:
        print(f"Une erreur inconnue s'est produite : {e}")


# Section principale du script
if __name__ == "__main__":
    pass