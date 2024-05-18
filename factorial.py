#!/usr/bin/ python3

def factorial(n):
    # Si no es entero, devolver error
    if not isinstance(n, int):
        raise TypeError("El número debe ser un entero")
    
    # Si es negativo, devolver error
    if n < 0:
        print("El número debe ser positivo")
        return None
    # Si es menor o igual que 1, el factorial es 1
    elif n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    
if __name__ == "__main__":
    n_list = [-1, 5, 5000]
    
    for n in n_list:
        print(f"Factorial de {n}: {factorial(n)}")