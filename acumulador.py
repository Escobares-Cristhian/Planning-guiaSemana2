import sys

# Verifica que se proporcionó un valor para n
if len(sys.argv) != 2:
    print("Uso: python3 script_acumulador.py <n>")
    sys.exit(1)

# Obtiene el valor de n de los argumentos de línea de comandos
n = int(sys.argv[1])

# Ejemplo de programa con variable acumulador
acumulador = 0

for i in range(1, n + 1):
    acumulador += i
    print("El acumulador es:", acumulador)
