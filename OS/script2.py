import os
import argparse

def rechercher_mot_dans_dossier(mot_a_chercher, chemin_dossier, chemin_resultats):
    try:
        with open(chemin_resultats, 'w') as fichier_resultats:
            # Parcourir tous les fichiers et sous-dossiers du dossier spécifié
            for dossier_racine, _, fichiers in os.walk(chemin_dossier):
                for nom_fichier in fichiers:
                    chemin_fichier = os.path.join(dossier_racine, nom_fichier)
                    # Lire chaque ligne du fichier et rechercher le mot
                    with open(chemin_fichier, 'r') as fichier:
                        for numero_ligne, ligne in enumerate(fichier, 1):
                            if mot_a_chercher in ligne:
                                # Écrire le résultat dans le fichier de résultats
                                fichier_resultats.write(f"{chemin_fichier}, ligne {numero_ligne}: {ligne.strip()}\n")
    except PermissionError:
        print("Erreur : vous n'êtes pas autorisé à lire le dossier ou à écrire le fichier de résultats.")
    except FileNotFoundError:
        print("Erreur : le chemin spécifié n'existe pas.")
    except OSError as e:
        print(f"Erreur liée au système d'exploitation : {e}")
    except Exception as e:
        print(f"Une erreur inconnue s'est produite : {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Recherche d'un mot dans un répertoire.")
    parser.add_argument("mot", type=str, help="Mot ou phrase à rechercher.")
    parser.add_argument("chemin_dossier", type=str, help="Chemin du dossier où effectuer la recherche.")
    parser.add_argument("chemin_resultats", type=str, help="Chemin du fichier où écrire les résultats de la recherche.")
    args = parser.parse_args()

    # Exécuter la recherche
    rechercher_mot_dans_dossier(args.mot, args.chemin_dossier, args.chemin_resultats)
