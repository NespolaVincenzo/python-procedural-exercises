"""Exercice : Calculer l'âge

Demande l'âge de l'utilisateur et affiche son âge dans 5 ans.

Objectifs :
- convertir une entrée avec int()
- effectuer un calcul simple
"""

def main():
    # Écris ta solution ici.
    age = int(input("Quelle âge avez-vous ?\n"))
    age += 5
    print(f"Dans 5 ans, vous aurez {age} ans.")
    pass


if __name__ == "__main__":
    main()
