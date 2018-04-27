import string

abecedario = string.ascii_lowercase


def cesar(n):
    # Devuelve el cypher movido n veces.
    res = []
    for i in range(n, 0, -1):
        res.append(abecedario[len(abecedario)-i])
    for i in range(0, len(abecedario)-n):
        res.append(abecedario[i])
    return res


def cifrar(texto_secreto, movimiento):
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
