# Instructions d'utilisation

## Lancement du programme

1. **Ouvrir un terminal**  
   Rendez-vous dans le dossier `src` du projet en utilisant la commande :

2. **Exécuter le script principal**  
Lancez le programme avec la commande suivante :

3. **Choix de l'utilisateur et du nombre de répétitions**  
À l'exécution, vous serez invité à choisir votre identifiant utilisateur.  
Vous devez ensuite sélectionner au moins **2 répétitions** (2 blocs).

## Règles du jeu

- **But du jeu :**  
À chaque fois, repérez la cible **colorée en vert** et cliquez dessus.

- **Déroulement d'une partie :**  
Chaque partie comporte **15 cibles** à cliquer.

- **Configuration globale :**  
Au total, vous allez réaliser :
- **27 conditions** différentes, issues des combinaisons de :
 - 3 techniques : *rope*, *bubble* et *normal*
 - 3 densités de cibles : 30, 60 et 90 cibles
 - 3 tailles de cibles : 6, 12 et 18 pixels  
- **5 parties** par bloc (puisque chaque partie correspond à 15 cibles)  
- **2 blocs** de répétition minimum  

Ce qui donne en tout : `27 * 5 * 2` cibles à cliquer.

## Enregistrement des résultats

- **Logs de performance :**  
À la fin de chaque partie, un bloc de **15 lignes** est ajouté au log.  
Ces lignes enregistrent :
- Le temps écoulé pour trouver et cliquer sur chaque cible verte.
- Le nombre d'erreurs (clics sur des cibles incorrectes).

---

Profitez de ce test pour mesurer vos performances dans des conditions variées !
