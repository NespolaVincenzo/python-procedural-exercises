"""Exercice : Aire et périmètre d'un rectangle

Demande la longueur et la largeur d'un rectangle puis affiche :
- son aire
- son périmètre

Objectifs :
- nombres flottants
- calculs arithmétiques
- affichage de plusieurs résultats
"""

def main():
    # Écris ta solution ici.
    length = int(input("De quelle longeur est ce rectangle ?\n"))
    width = int(input("De quelle largeur est ce rectangle ?\n"))
    
    area = length * width
    scope = (length + width) * 2
    
    print(f"L'aire de ce rectangle est de {area} mètre² et le périmètre est de {scope} mètre.")
    pass


if __name__ == "__main__":
    main()
