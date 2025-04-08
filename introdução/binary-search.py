"""

exemplo ce busca binaria 

"""

def search(elements: list, element: int, end: int, start: int = 0):

    while start <= end:
        mid = start + ((end - start ) // 2)

        if elements[mid] == element:
            return mid
        elif elements[mid] < element:
            start = mid + 1
        else: 
            end = mid - 1

    return "elemento não encontrado"


elements = [4,6,9,13,14,18,21,24,38]
element = 38

result = search(elements, element, len(elements) - 1)
print(f"O numero é:{result}")

