"""
Enunciado:

https://www.programcreek.com/2012/12/leetcode-median-of-two-sorted-arrays-java/https://www.programcreek.com/2012/12/leetcode-median-of-two-sorted-arrays-java/

"""
from itertools import islice
from numbers import Number


def encontrar_k_esimo_elemento(a, indice_inicial_de_a, indice_final_de_a, b, indice_inicial_de_b, indice_final_de_b, k):
    m = indice_final_de_a - indice_inicial_de_a + 1  # 7
    n = indice_final_de_b - indice_inicial_de_b + 1  # 11  k= 9
    if m == 0:
        return b[indice_inicial_de_b + k]
    elif n == 0:
        return a[indice_inicial_de_a + k]
    if k == 0:
        primeiro_elemento_de_a = a[indice_inicial_de_a]
        primeiro_elemento_de_b = b[indice_inicial_de_b]
        return min(primeiro_elemento_de_a, primeiro_elemento_de_b)

    delta_para_o_meio_de_a = k * m // (m + n)
    indice_do_meio_de_a = indice_inicial_de_a + delta_para_o_meio_de_a  # 3
    indice_do_meio_de_b = indice_inicial_de_b + k - delta_para_o_meio_de_a - 1  # 5

    elemento_do_meio_de_a = a[indice_do_meio_de_a]  # 4
    elemento_do_meio_de_b = b[indice_do_meio_de_b]  # 6

    if elemento_do_meio_de_b > elemento_do_meio_de_a:
        k -= indice_do_meio_de_a - indice_inicial_de_a + 1
        indice_inicial_de_a = indice_do_meio_de_a + 1
        indice_final_de_b = indice_do_meio_de_b
    else:
        k -= indice_do_meio_de_b - indice_inicial_de_b + 1
        indice_inicial_de_b = indice_do_meio_de_b + 1
        indice_final_de_a = indice_do_meio_de_a
    return encontrar_k_esimo_elemento(a, indice_inicial_de_a, indice_final_de_a, b, indice_inicial_de_b,
                                      indice_final_de_b, k)



def mediana_de_duas_listas_sub_linear(a: list, b: list) -> Number:
    """
    >>> mediana_de_duas_listas_sub_linear([1], [])
    1
    >>> mediana_de_duas_listas_sub_linear([], [2])
    2
    >>> mediana_de_duas_listas_sub_linear([1], [2])
    1.5
    >>> mediana_de_duas_listas_sub_linear([1], [2, 3000])
    2
    >>> mediana_de_duas_listas_sub_linear([1, 3], [2, 3000])
    2.5
    >>> mediana_de_duas_listas_sub_linear([1, 3, 4], [2, 3000])
    3
    >>> mediana_de_duas_listas_sub_linear([1, 3, 4], [2, 3000, 5000])
    3.5
    >>> mediana_de_duas_listas_sub_linear([1, 3, 4], [2, 3000, 5000, 5002])
    4
    >>> mediana_de_duas_listas_sub_linear([1, 3, 4], [2, 3000, 5000, 5002, 5004])
    1502.0
    >>> mediana_de_duas_listas_sub_linear([1, 3, 4, 4], [2, 3000, 5000, 5002, 5004])
    4

    Complexidade de tempo de execução:
    Complexidade de memória:


    :param a:
    :param b:
    :return:
    """

    # a=[1], b=[2]
    m = len(a)
    n = len(b)

    tamanho_vetor_fundido = m + n

    k = tamanho_vetor_fundido // 2
    if tamanho_vetor_fundido % 2 == 1:
        # retornar k-ésimo elmento
        return encontrar_k_esimo_elemento(a, 0, m - 1, b, 0, n - 1, k)
    else:
        # retornar média entre o k-ésimo elemento e o (k-1)-ésimo elemento
        k_esimo = encontrar_k_esimo_elemento(a, 0, m - 1, b, 0, n - 1, k)
        k_esimo_menos_um = encontrar_k_esimo_elemento(a, 0, m - 1, b, 0, n - 1, k - 1)
        return (k_esimo + k_esimo_menos_um) / 2


def mediana_de_duas_listas_linear(a: list, b: list) -> Number:
    """
    >>> mediana_de_duas_listas_linear([1], [2])
    1.5
    >>> mediana_de_duas_listas_linear([1], [2, 3000])
    2
    >>> mediana_de_duas_listas_linear([1, 3], [2, 3000])
    2.5

    Complexidade de tempo de execução: O(n+m)
    Complexidade de memória: O(1)


    :param a:
    :param b:
    :return:
    """
    m = len(a)
    n = len(b)
    elementos_fundidos = fundir(a, b)
    tamanho = m + n

    indice_do_elemento_do_meio = tamanho // 2
    if tamanho % 2 == 1:
        segunda_metade = islice(
            elementos_fundidos, indice_do_elemento_do_meio, indice_do_elemento_do_meio + 1)
        return next(iter(segunda_metade))
    segunda_metade = islice(
        elementos_fundidos, indice_do_elemento_do_meio - 1, indice_do_elemento_do_meio + 1)
    iter_metade_maior = iter(segunda_metade)
    return (next(iter_metade_maior) + next(iter_metade_maior)) / 2


def fundir(a, b):
    iter_a = iter(a)
    iter_b = iter(b)
    elemento_atual_de_a = next(iter_a)
    elemento_atual_de_b = next(iter_b)
    while True:
        if elemento_atual_de_a > elemento_atual_de_b:
            yield elemento_atual_de_b
            try:
                elemento_atual_de_b = next(iter_b)
            except StopIteration:
                yield elemento_atual_de_a
                break
        else:
            yield elemento_atual_de_a
            try:
                elemento_atual_de_a = next(iter_a)
            except StopIteration:
                yield elemento_atual_de_b
                break

    yield from iter_a
    yield from iter_b


def mediana_de_duas_listas(a: list, b: list) -> Number:
    """
    >>> mediana_de_duas_listas([1], [])
    1
    >>> mediana_de_duas_listas([1], [2])
    1.5
    >>> mediana_de_duas_listas([1], [2, 3000])
    2
    >>> mediana_de_duas_listas([1, 3], [2, 3000])
    2.5

    Complexidade de tempo de execução: O((n+m)log(n+n))
    Complexidade de memória: O(n+m)


    :param a:
    :param b:
    :return:
    """
    lista_concatenada = a + b
    return mediana(lista_concatenada)


def mediana(lista: list) -> Number:
    """
    >>> mediana([1])
    1
    >>> mediana([1, 2])
    1.5
    >>> mediana([1, 3000, 2])
    2
    >>> mediana([1, 3000, 2, 3])
    2.5


    :param lista:
    :return:
    """
    lista.sort()
    return mediana_de_lista_ordenada(lista)


def mediana_de_lista_ordenada(lista):
    tamanho = len(lista)
    indice_do_elemento_do_meio = tamanho // 2
    if tamanho % 2 == 1:
        return lista[indice_do_elemento_do_meio]
    return (lista[indice_do_elemento_do_meio] + lista[indice_do_elemento_do_meio - 1]) / 2
