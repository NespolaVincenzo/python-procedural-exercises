"""Exercice : Convertisseur Celsius / Fahrenheit

Demande une température en Celsius puis convertis-la en Fahrenheit.

Formule :
F = C × 9 / 5 + 32

Objectifs :
- float()
- formule mathématique
- résultat lisible
"""

def main():
    # Écris ta solution ici.
    temparetureCelsius = int(input("Quelle est la température que vous-souhaitez convertir ?\n"))
    temperatureFahrenheit = temparetureCelsius * 9 / 5 + 32
    print(f"{temparetureCelsius}°C convertis en fahrenheit font {temperatureFahrenheit}°F")
    pass


if __name__ == "__main__":
    main()
