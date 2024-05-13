import os
import argparse

def rechercher_mot_dans_dossier(mot_a_chercher, chemin_dossier, chemin_resultats):
    try:
        with open(chemin_resultats, 'w') as fichier_resultats:
            # Parcourir tous les fichiers et sous-dossiers du dossier spécifié
            for dossier_racine, dossiers, fichiers in os.walk(chemin_dossier):
                for nom_fichier in fichiers:
                    chemin_fichier = os.path.join(dossier_racine, nom_fichier)
                    # Ouvrir le fichier en mode lecture
                    with open(chemin_fichier, 'r') as fichier:
                        # Parcourir chaque ligne du fichier
                        numero_ligne = 1
                        for ligne in fichier:
                            if mot_a_chercher in ligne:
                                fichier_resultats.write(f"{chemin_fichier}, ligne {numero_ligne}: {ligne.strip()}\n")
                            numero_ligne += 1

    except Exception as e:
        print(e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Recherche d'un mot dans un répertoire.")
    parser.add_argument("mot", type=str, help="Mot ou phrase à rechercher.")
    parser.add_argument("chemin_dossier", type=str, help="Chemin du dossier où effectuer la recherche.")
    parser.add_argument("chemin_resultats", type=str, help="Chemin du fichier où écrire les résultats de la recherche.")
    args = parser.parse_args()

    # Exécuter la recherche
    rechercher_mot_dans_dossier(args.mot, args.chemin_dossier, args.chemin_resultats)
    rechercher_mot_dans_dossier("police", "c:/Users/Utilisateur/Downloads", "c:/Users/Utilisateur/Downloads/script1.py")
