from dataclasses import dataclass

@dataclass

class Sapato:
    modelo: str
    marca: str 
    cor: str
    tamanho: int
    preco: float

    def exibir(self):
        print()
        print(f'o sapato é do modelo: {self. modelo};\n da marca: {self.marca};\n da cor: {self.cor};\n do tamanho: {self.tamanho};\n com o valor de: {self.preco}.')



        
        


