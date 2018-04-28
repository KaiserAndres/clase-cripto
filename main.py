'''
Esta es la documentación general del archivo, este esta diseñado para ser corrido desde la terminal,
el input para este se da atravez de stdin y su salida será por stdout, para cifrar un archivo en linux por ejemplo se
usa la siguiente sintaxis

$ cat <archivo> | python3 main.py

donde el archivo tiene en su primera linea la cantidad de caracteres a mover en el cifrado.
'''

import string

abecedario = string.ascii_lowercase


def cesar(n):
    '''
    :param n: cantidad de caracteres a mover del abecedario standard hacia la derecha. Debe estar entre 0 y 24.
    :return: Lista de caracteres ordenados movidos n veces hacia la derecha.
    '''
    # Devuelve el cypher movido n veces.
    res = []
    for i in range(n, 0, -1):
        res.append(abecedario[len(abecedario)-i])
    for i in range(0, len(abecedario)-n):
        res.append(abecedario[i])
    return res


def cifrar(texto_secreto, movimiento):
    '''
    :param texto_secreto: Texto plano original a cifrar
    :param movimiento: Grado del cifrado de cesar a usar.
    :return: Texto cifrado del grado especificado.
    '''
    res = ''
    nuevo_abc = cesar(movimiento)
    for letra in texto_secreto:
        if letra in abecedario:
            index_nuevo = abecedario.index(letra)
            res += nuevo_abc[index_nuevo]
    return res


mov = int(input("Que tanto deseas moverte (numero) "))
mensaje = input("Cual es tu mensaje ").lower()

print(cifrar(mensaje, mov))
