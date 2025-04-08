"""
exemplo de divisao e conquista com ordenação e mesclagem

"""


def merge_sort(elements: list) -> list:
    # Caso base: lista com 0 ou 1 elemento já está ordenada
    if len(elements) <= 1:
        return elements
    
    # Divide a lista ao meio (Divisão)
    mid = len(elements) // 2
    left_half = merge_sort(elements[:mid])
    right_half = merge_sort(elements[mid:])
    
    # Combina as listas ordenadas (Conquista/Mesclagem)
    return merge(left_half, right_half)


def merge(first: list, second: list) -> list:
    result = []
    i = j = 0

    # Mescla comparando os elementos um por um
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1

    # Adiciona o que sobrou (caso sobre elementos em qualquer das listas)
    result.extend(first[i:])
    result.extend(second[j:])
    
    return result


# Testando com a sua lista de exemplo:
elements = [12, 11, 7, 41, 61, 13, 16, 14]

print(f'Lista original: {elements}')
sorted_elements = merge_sort(elements)
print(f'Lista ordenada: {sorted_elements}')

