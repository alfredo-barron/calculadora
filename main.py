from app.modulo1 import suma, resta
from app.modulo2 import producto, division
from app.utils import imprimir_bienvenida

if __name__ == '__main__':
    imprimir_bienvenida()
    print("Suma: ", suma(5, 3))
    print("Resta: ", resta(10, 4))
    print("Multiplicación: ", producto(6, 7))
    print("División: ", division(10, 2))
