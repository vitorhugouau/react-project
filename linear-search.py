
"""
exemplo de busca linar
"""

def search (elements: list, element: int) -> int:
 
    for index, value in enumerate(elements):
        if value == element:
            return index
        
    
    return "elemento não encontrado"


elements = [3,4,1,6,14]

result = search(elements, 6)


print(f"O numero é:{result}")