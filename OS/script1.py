import os 
import calendar
import locale

# Fonction pour créer des dossiers et des fichiers
def generer_dossier_fichiers(path_dossier : str) -> None:
    """
    Crée une structure de dossiers pour les 12 mois en français avec 15 fichiers numérotés dans chaque dossier.

    :param reportoire : Chemin du répertoire de base où créer la structure.
    """
    try:
        # Création du répertoire parent
        # Nom du dossier à créer
        nom_dossier = "RepertoireParent"

        # Chemin complet du nouveau dossier
        chemin_nouveau_dossier = os.path.join(path_dossier, nom_dossier)
        os.makedirs(chemin_nouveau_dossier, exist_ok=False)

        # if not repertoireParent.exists():
        #     repertoireParent.mkdir(parents=True, exist_ok=True)
        #     #print(f"Répertoire créé avec succes : {repertoire}")

        # Noms des mois en français
        locale.setlocale(locale.LC_TIME, 'fr_FR')
        moisdelannee = calendar.month_name[1:]
        print(moisdelannee)


        # Création des sous-dossiers et fichiers
        for mois in range(len(moisdelannee)):
            # sous_repertoire = repertoireParent/moisdelannee[mois]
            # if not sous_repertoire.exists():
            #     sous_repertoire.mkdir()
            # Obtenir le nom du mois
            nom_mois = (moisdelannee[mois])
            # Ajouter un zéro devant les mois de 1 à 9
            mois_str = str(mois+1).zfill(2)
            # Créer le répertoire pour le mois
            mois_path = os.path.join(chemin_nouveau_dossier, f"{mois_str}_{nom_mois}")
            os.makedirs(mois_path, exist_ok=True)
                
            # Création des fichiers dans le sous-dossier pour chaque mois
            for i in range(1, 16):
                # Ajouter un zéro devant les nombres de 1 à 9
                fichier_num = str(i).zfill(2)
                nom_fichier = f"log{fichier_num}.txt"
                chemin_fichier = os.path.join(mois_path, nom_fichier)
                os.system(f"echo. > {chemin_fichier}")
    except Exception as e:
        print(e)


# Section principale du script
if __name__ == "__main__":
    generer_dossier_fichiers("C:/Users/abelc/Desktop/Python")


