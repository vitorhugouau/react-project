import numpy as np


class Sort: 
    def __init__(self, size: int):
        self.size = size
        self.last_item_index = -1
        self.array = np.empty(self.size, dtype=object)

    def show_array(self):  
        """
        Método que lista todos os itens do array ordenado
        """
        if self.last_item_index == -1:
            print("Vetor vazio!")
        else:
            for index in range(self.last_item_index + 1):
                print(f"{index} -> {self.array[index].vertex.label}")#Modificado
                print(f"\t- KM: {self.array[index].cost} KM")#NEW
                print(f"\t- Target: {self.array[index].vertex.target_distance} KM")#NEW
                print(f"\t- Star: {self.array[index].star_distance} KM")#NEW
    
    def insert(self, adjacent):
        """
        Método que faz a inserção ordenada no vetor (self.array)
        """
        if self.last_item_index == (self.size - 1):
            print("Capacidade máxima atingida.")
            return

        position = 0
        for position in range(self.last_item_index + 1):
            if self.array[position].star_distance > adjacent.star_distance:#Modificado
                break
            if position == self.last_item_index:
                position += 1
        
        last_item_index = self.last_item_index
        while last_item_index >= position:
            next_position = last_item_index + 1
            self.array[next_position] = self. array[last_item_index]
            last_item_index -= 1
        
        self.array[position] = adjacent #Modificado
        self.last_item_index += 1