import os 
import calendar
import locale
import argparse

# Fonction pour créer des dossiers et des fichiers
def generer_dossier_fichiers(path_dossier : str) -> None:
    """
    Crée un répertoire dont le chemin est passé en paramètre puis un dossier pour chacun 12 mois en français avec 15 fichiers de logs numérotés dans chaque dossier.

    Paramètre : Chemin du répertoire parent où créer la structure.
    """
    try:
        # Création du répertoire parent
        # Nom du dossier à créer
        nom_dossier = "RepertoireParent"

        # Chemin complet du répertoire
        chemin_nouveau_dossier = os.path.join(path_dossier, nom_dossier)
        os.makedirs(chemin_nouveau_dossier, exist_ok=False)

        # Noms des mois en français
        locale.setlocale(locale.LC_TIME, 'fr_FR')
        moisdelannee = calendar.month_name[1:]
        print(moisdelannee)


        # Création des sous-dossiers puis de fichiers

        for mois in range(len(moisdelannee)):
            # Obtenir le nom du mois
            nom_mois = (moisdelannee[mois])
            # Ajouter un zéro devant les mois de 1 à 9
            numero_mois_str = str(mois+1).zfill(2)
            # Créer le répertoire pour le mois
            mois_path = os.path.join(chemin_nouveau_dossier, f"{numero_mois_str}-{nom_mois}")
            os.makedirs(mois_path, exist_ok=False)
                
            # Création des fichiers dans le sous-dossier pour chaque mois
            for i in range(1, 16):
                # Ajouter un zéro devant les nombres de 1 à 9
                numero_fichier = str(i).zfill(2)
                nom_fichier = f"log{numero_fichier}.txt"
                chemin_fichier = os.path.join(mois_path, nom_fichier)
                os.system(f"echo. > {chemin_fichier}")

    except PermissionError:
        print("Erreur : vous n'êtes pas autorisé à lire ou à écrire dans ce dossier.")
    except FileNotFoundError:
        print("Erreur : le chemin spécifié n'existe pas.")
    except OSError:
        print(f"Erreur liée au système d'exploitation : {e}")
    except Exception as e:
        print(f"Une erreur inconnue s'est produite : {e}")
     

# Section principale du script
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Recherche d'un mot dans un répertoire.")
    parser.add_argument("chemin_dossier", type=str, help="Chemin du dossier central")
    args = parser.parse_args()
    generer_dossier_fichiers(args.chemin_dossier)


