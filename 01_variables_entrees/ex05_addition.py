"""Exercice : Mini calculatrice

Demande deux nombres puis affiche leur somme, différence,
produit et quotient.

Objectifs :
- plusieurs variables
- opérateurs arithmétiques
- formatage des résultats

Ne traite pas encore les erreurs complexes : le cas de division par zéro
sera abordé plus tard.
"""

def main():
    # Écris ta solution ici.
    numberOne = int(input("Veuillez choisir votre premier nombre.\nVotre choix : "))
    numberTwo = int(input("Veuillez choisir votre second nombre.\nVotre choix : "))
    
    print(f"La somme de c'est deux nombres est {numberOne + numberTwo}.")
    print(f"La différence de c'est deux nombres est {numberOne - numberTwo}.")
    print(f"Le produit de c'est deux nombres est {numberOne * numberTwo}.")
    print(f"Le quotient de c'est deux nombres est {numberOne // numberTwo}.")
    
    pass


if __name__ == "__main__":
    main()
