'''
    Este programa genera un abecedario al azar por medio del algoritmo de barajeo, y encripta un texto el cual
    pasa por stdin.

    Para encriptar de manera aleatoria un archivo de texto se puede usar el siguiento comando en una consola:

    $ cat <archivo> | python3 barajeada.py
'''

import random
import string


def swap(lista, n1, n2):
    '''
    Intercambia dos elementos en una lista.
    :param lista: Lista a ser trabjada (Nota: se pasa por referencia, este operación permuta la lista).
    :param n1: index del primer elemento.
    :param n2: index del segundo elemento.
    :return: void.
    '''
    temp = lista[n1]
    lista[n1] = lista[n2]
    lista[n2] = temp


def barajear():
    '''
    Genera un abecedario al azar.
    :return: lista de letras, es una permutación de string.ascii_lowercase
    '''
    abc = string.ascii_lowercase
    cypher = list(abc)
    for i in range(len(abc)):
        dado = random.randint(0, len(abc)-1)
        swap(cypher, i, dado)
    return cypher


def cifrar(texto_secreto, abecedario):
    '''
    Genera un texto ecriptado por medio de sustitución de caracteres.
    :param texto_secreto: texto plano a ser encriptado.
    :param abecedario: abecedario para usar.
    :return: el texto encriptado.
    '''
    res = ''
    for letra in texto_secreto:
        if letra in abecedario:
            index_nuevo = string.ascii_lowercase.index(letra)
            res += abecedario[index_nuevo]
    return res


secreto = barajear()
mensaje = input("Dime que quieres que encrípte ")
print(cifrar(mensaje, secreto))