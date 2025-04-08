"""
Exemplo de divisão e Conquista, com Ordenação e mesclagem.
"""

def merge_sort(elements: list)-> list:
    """
    Recebe uma lista nao ordenada, entao utilizando o conceito de divesão e conquista, fara a divisão da lista,
    em sub-lista ate que reste apenas um elemento. Em paralelo invoca a função merge para fazer as meclagem ja ordenando oos elementos.
    """
    if len(elements)==1:
        return elements
    

    mid = len(elements) // 2

   
    first = elements[:mid]
    second = elements[mid:]

    first_half = merge_sort(first)
    second_half = merge_sort(second)
    
    return merge(first_half,second_half)
    

def merge(first: list, second: list):
    """
    Juntar os elementos de forma ordenada em uma lista.
    """
    index1 = index2 = 0
    elements = []

    while index1 < len(first) and index2 < len(second):
        if first[index1] < second[index2]:
            elements.append(first[index1])
            index1 += 1
        else:
            elements.append(second[index2])
            index2 += 1
    
    while index1 < len(first):
        elements.append(first[index1])
        index1 += 1

    while index2 < len(second):
        elements.append(second[index2])
        index2 += 1

    return elements

elements = [12,11,7,41,61,13,16,14]
print(merge_sort(elements))