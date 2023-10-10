import argparse

# 1. Incorporo la descripción del programa
parser = argparse.ArgumentParser(
  description='Este programa imprime el nombre de los primero cinco números'
)

# 2. Agrego argumentos que quiero aceptar
parser.add_argument('-c', '--color', metavar='color', required=True, help='el color a usar')

# 3. Parseo los argumentos que haya agregado
args = parser.parse_args()

# 4. Imprimo en consola el argumento color
print(args.color)