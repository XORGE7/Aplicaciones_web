import math

def isprime(n):
    """
    Determina si un número es primo o no.

    Args:
        n (int): El número a verificar.

    Returns:
        bool: True si el número es primo, False de lo contrario.
    """
    if n <= 1:
        return False
    for i in range(2,int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def main():

    """tiene toda la lógica principal"""
    for i in range(100):
        if isprime(i):
            print (i, end=' ')
    print()

if __name__ == '__main__':
    main()
