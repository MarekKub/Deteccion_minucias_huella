from PIL import Image       
import numpy as np
import matplotlib.pyplot as plt

# AUTOR: Marek Kubicki
# MÓDULO: PIA
# TAREA: Alogoritmo minucias

imagen = Image.open("huella2.png")

#  PASO 1: hemos cargado la imagen y la hemos convertido en una matriz
def img_to_matrix(imagen):
    # Para imagen a matriz
    imagen_a_matriz = np.asarray(imagen)         #  PASO 1: hemos cargado la imagen y la hemos convertido en una matriz
    return imagen_a_matriz

# PASO 2: PASAR A GRIS IMAGEN

# PASO 2(1/2): Crear matriz copia llena de ceros y tamaño de matriz original. Luego
# esta matriz la llenaremos con la imagen para crear una copia de al imagen, 
# y a la vez la pasaremos a gris.
def crear_imagen_copia(imagen):
    imagen = np.zeros((imagen_a_matriz.shape[0],imagen_a_matriz.shape[1]))
    return imagen

# PASO 3(1/2): 
#   - en un bucle doble voy recorriendo para filas y columnas => con los dos for
#   - para cada elemento del array calcula la media aritmetica , y divido entre 255 para
# obtener un valor entre 0 y 1 para cada pixel:
#                   np.mean(imagen_a_matriz[i,j])/255
#   - y voy recorriendo la matriz 'imagen_copia' y en cada pixel le doy un valor        
# entre 0 y 1 (calculado con la media como pongo en el guion de arriba), por lo 
# que lleno la matriz 'imagen_copia' de valroes entre 0 y 1. 
def imagen_valores_entre_0_y_1(imagen):
    for i in range(imagen_copia.shape[0]):
        for j in range(imagen_copia.shape[1]):
            imagen_copia[i,j] = np.mean(imagen_a_matriz[i,j])/255
    return imagen_copia


# BINARIZADO
# PASO 4: BINARIZADO -> Converitir todos los pixeles o en Blanco o Negro
#   Se utiliza el mismo codigo del PASO 3 pero 2 cosas distintas:
#   - 1º) se parte de la imagen pasada a array de antes: imagen_copia
#   - 2º) se pinta cada pixel o bien de Negro o bien de Blanco, segun el valor
# del pixel sea menor o mayor a un valor umbral.

# PASO 4: BINARIZADO
#   Crearemos un array con el tamaño de la imagen en BN.
# Luego  esta imagen la llenaremos con la imagen binarizada de la imagen
# original.
def binarizado(imagen):
    # PASO 4(1/2): Crear matriz copia llena de ceros y tamaño de imagen copia.
    imagenBN = np.zeros((imagen.shape[0], imagen.shape[1]))

    # PASO 4(2/2): Creamos dos bucles for anidados para ir recorriendo
    # el array de 'imagen_copia' y vamos pintando cada pixel de blanco o negro
    # segun el valor de ese pixel sea mayor o menor a un valor umbral
    # que establecemos a discrecion.

    # PASO 4 (2/2): Creamos dos bucles for anidados para ir recorriendo
    # el array de 'imagen_copia'. 
    imagenBN = np.zeros((imagen.shape[0], imagen.shape[1]))
    for i in range(imagen.shape[0]):
        for j in range(imagen.shape[1]):

            # vamos pintando en array 'imagenBN' cada pixel de blanco o negro
            # segun el valor de ese pixel sea mayor o menor a un valor umbral
            # que establecemos a discrecion: np.mean(imagen_copia[i][j] < 0.72)
            if np.mean(imagen[i][j]) < 0.72:
                imagenBN[i][j] = 1
            else:
                imagenBN[i][j] = 0
    return imagenBN


def encontrar_minutas(imagen):
    # Matriz para llenar de imagen con minutas encerradas
    imagen_minutas_encerradas = np.zeros((imagen_a_matriz.shape[0],imagen_a_matriz.shape[1]))

    # 1) ir recorriendo fila a fila - Quito las 10 primeras y ultimas filas y las 
    # 10 primeras y ultimas columnas.
    for f in range(10,len(imagen_delgada)-10):
        for c in range(10,len(imagen_delgada[0])-10):
        
            # 2) buscar un 1
            if imagen_delgada[f,c] == 1:
                print(f"hay un 1 en esta posicion {imagen_delgada[f,c]} de la matriz")

                # 3) si encuentro un 1  => sumo el valor de los vecinos - que casteo a entero
                sum_surrounding_elements = int(imagen_delgada[f-1][c-1]) + int(imagen_delgada[f-1][c]) + int(imagen_delgada[f-1][c+1]) 
                + int(imagen_delgada[f][c-1]) + int(imagen_delgada[f][c+1]) + int(imagen_delgada[f+1][c-1]) + int(imagen_delgada[f+1][c]) 
                + int(imagen_delgada[f+1][c+1]) 

                print(f"SUM_SURROUNDING_ELEMENTS = {sum_surrounding_elements}")
                
                #   Si sum_surrongin_elemntents vale 1 => entonces es un punto terminal(minuta) y tengo que encerrar
                # la minuta en unos.
                #   Si no lo es => no hacer nada
                #
                #   Y luego pintar el resultado en una nueva imagen.

                # Si la suma de los elementos alrededor del elemento es 1,
                # este es una minuta.
                #   Y voy pintado en la imagen_minutas_encerradas
                if sum_surrounding_elements == 1:
                    imagen_minutas_encerradas[f-2][c-2] = 1 
                    imagen_minutas_encerradas[f-2][c-1] = 1
                    imagen_minutas_encerradas[f-2][c] = 1
                    imagen_minutas_encerradas[f-2][c+1] = 1
                    imagen_minutas_encerradas[f-2][c+2] = 1

                    imagen_minutas_encerradas[f-1][c-2] = 1 
                    imagen_minutas_encerradas[f-1][c-1] = 0
                    imagen_minutas_encerradas[f-1][c] = 0
                    imagen_minutas_encerradas[f-1][c+1] = 0
                    imagen_minutas_encerradas[f-1][c+2] = 1

                    imagen_minutas_encerradas[f][c-2] = 1 
                    imagen_minutas_encerradas[f][c-1] = 0
                    imagen_minutas_encerradas[f][c] = 1
                    imagen_minutas_encerradas[f][c+1] = 0
                    imagen_minutas_encerradas[f][c+2] = 1

                    imagen_minutas_encerradas[f+1][c-2] = 1 
                    imagen_minutas_encerradas[f+1][c-1] = 0
                    imagen_minutas_encerradas[f+1][c] = 0
                    imagen_minutas_encerradas[f+1][c+1] = 0
                    imagen_minutas_encerradas[f+1][c+2] = 1

                    imagen_minutas_encerradas[f+2][c-2] = 1 
                    imagen_minutas_encerradas[f+2][c-1] = 1
                    imagen_minutas_encerradas[f+2][c] = 1
                    imagen_minutas_encerradas[f+2][c+1] = 1
                    imagen_minutas_encerradas[f+2][c+2] = 1
    return imagen_minutas_encerradas        

def chararray(intmatrix):
    '''Change a 2d list of lists of 1/0 ints into lines of 1/0 chars'''
    return '\n'.join(''.join(str(p) for p in row) for row in intmatrix)

def toTxt(intmatrix):
    '''Change a 2d list of lists of 1/0 ints into lines of '#' and '.' chars'''
    return '\n'.join(''.join(('#' if p else '.') for p in row) for row in intmatrix)

def neighbours(x, y, image):
    '''Return 8-neighbours of point p1 of picture, in order'''
    i = image
    x1, y1, x_1, y_1 = x+1, y-1, x-1, y+1
    #print ((x,y))
    return [i[y1][x],  i[y1][x1],   i[y][x1],  i[y_1][x1],  # P2,P3,P4,P5
            i[y_1][x], i[y_1][x_1], i[y][x_1], i[y1][x_1]]  # P6,P7,P8,P9

def transitions(neighbours):
    n = neighbours + neighbours[0:1]    # P2, ... P9, P2
    return sum((n1, n2) == (0, 1) for n1, n2 in zip(n, n[1:]))

def zhangSuen(image):
    changing1 = changing2 = [(-1, -1)]
    while changing1 or changing2:
        # Step 1
        changing1 = []
        for y in range(1, len(image) - 1):
            for x in range(1, len(image[0]) - 1):
                P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, image)
                if (image[y][x] == 1 and    # (Condition 0)
                    P4 * P6 * P8 == 0 and   # Condition 4
                    P2 * P4 * P6 == 0 and   # Condition 3
                    transitions(n) == 1 and # Condition 2
                    2 <= sum(n) <= 6):      # Condition 1
                    changing1.append((x,y))
        for x, y in changing1: image[y][x] = 0
        # Step 2
        changing2 = []
        for y in range(1, len(image) - 1):
            for x in range(1, len(image[0]) - 1):
                P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, image)
                if (image[y][x] == 1 and    # (Condition 0)
                    P2 * P6 * P8 == 0 and   # Condition 4
                    P2 * P4 * P8 == 0 and   # Condition 3
                    transitions(n) == 1 and # Condition 2
                    2 <= sum(n) <= 6):      # Condition 1
                    changing2.append((x,y))
        for x, y in changing2: image[y][x] = 0
        #print changing1
        #print changing2
    return image


#  CREACION DE VARIABLES , LLAMADA A METODOS Y EJECUCION DE CODIGO

#  Resultado de PASO 1
imagen_a_matriz = img_to_matrix(imagen)

plt.imshow(imagen_a_matriz)
plt.show()
print(imagen_a_matriz)

# CREAR COPIA IMAGEN
imagen_copia = crear_imagen_copia(imagen_a_matriz)

#  Resultado de PASO 2(2/1)
print(f"PRINT imagen a gris")
print(imagen_copia)

# Resultado de PASO 3(1/2)
imagen_copia = imagen_valores_entre_0_y_1(imagen_copia)

# PASO 3(2/2):
#   Y ahora al imprimir la imagen la paso a gris, pasandole como 2º parametro a
# metodo imshow() el valor cmap='gray'
plt.imshow(imagen_copia, cmap='gray')

print(f"PRINT imagen a gris sacando valores de cada pixel entre 0 y 1 y pasado a gray")

plt.show()

#  BINARIZADO 
imagenBN = binarizado(imagen_copia)

# Resultado de PASO 4 -PASO 4 (2/2): Con esto la imagen sale binarizada en su formato normal 
# de binarizado, es decir, binarizad en Amarillo y Violeta.
plt.imshow(imagenBN)

print(f"PRINT imagen BN - BINARIZADA en POR DEFECTO: en VIOLETA y AMARILLO")

plt.show()

# PASO 4 (2/2): Con esto la imagen sale binarizada en su formato blnaco y
# negro.
#   Para que la imagen salga binarizada en Blanco o negro le pasamos
# a imshow como 2º parametro: cmap='gray'
plt.imshow(imagenBN, cmap='gray')

print(f"PRINT imagen BN - BINARIZADA con parametro cmap='graY': en BLANCO y NEGRO")

plt.show()

# Resultado de PASO 5 ADELGAZAMIENTO - Zang Sueng
imagen_delgada = zhangSuen(imagenBN)

#Si se desea visualizar la imagen sin la tonalidad violeta-amarilla hay que indicarlo
plt.imshow(imagen_delgada, cmap='gray')

print(f"Imagen delgada - ADELGAZAMIENTO despues de ZHANG SUEN")

plt.show()

print(imagen_delgada)   

# Resultado de PASO - ENCONTRAR MINUTAS
imagen_minutas_encerradas = encontrar_minutas(imagen_delgada)

plt.imshow(imagen_minutas_encerradas)

print(f"PRINT imagen con MINUTAS LOCALIZADAS s- encerradas e cuadrado de unos")

plt.show()

print(imagen_minutas_encerradas)