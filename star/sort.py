"""
Modulo responsavel por realizar cordenação dos veteros de cidades ligadas a um vértice do mapa.
"""



import numpy as np


class Sort:
    """
    
    """
    def __init__(self, size:int):
        self.size = size
        self.last_item_index= -1 
        self.array = np.empty(self.size, dtype = object)

    def show_array(self):
        """
        Metodo que lista todos os itens do array ordenado.
        """
        if self.last_item_index == -1:
            print("Veeeeetooorrrr vazio ")
        else:
            for index in range(self.last_item_index + 1):
                print(f"-km{index} -> {self.array[index].vertex.label} ")
                print(f"\t-km{self.array[index].cost} km")
                print(f"\t-Target{self.array[index].vertex.target_distance} km")
                print(f"\t-Star{self.array[index].star_distance} km")

    def insert(self, adjacent):
        """
        Metodo que faz a inserção ordenada no vetor(self.array).
        """
        if self.last_item_index == (self.size -1):
            print("Capacidade maxima atiginda")
            return
    
        position = 0
        for position in range(self.last_item_index + 1):
            if self.array[position].star_distance > adjacent.star_distance:
                break
            if position == self.last_item_index:
                position += 1
        
        last_item_index = self.last_item_index
        while last_item_index >= position:
            next_position = last_item_index + 1
            self.array[next_position] = self.array[last_item_index]
            last_item_index -= 1

        self.array[position] = adjacent
        self.last_item_index += 1



