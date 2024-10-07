"""
Module principal pour vérifier si un nombre est premier.
"""

#### Fonction secondaire

def isprime(p):
    """
    Vérifie si un nombre entier p est un nombre premier.

    :param p: L'entier à vérifier.
    :return: True si p est premier, False sinon.
    """
    if not isinstance(p, int):
        return False
    if p<2:
        return False
    for i in range(2,p):   # Vérifier jusqu'à p
        if p % i == 0:
            return False
    return True
#### Fonction principale


def main():
    """
    Point d'entrée du programme. 
    Affiche si certains nombres sont premiers et liste tous les 
    nombres premiers jusqu'à 99.
    """
    print(isprime(8))
    print(isprime(3.4))
    print(isprime(15))
    print(isprime(3))

    # vos appels à la fonction secondaire ici
    print("Nombre premier jusqu'à 99 :")
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
