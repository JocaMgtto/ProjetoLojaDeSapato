from dataclasses import dataclass
@dataclass

class Venda:
    num_venda_feito: int

    def exibir(self): 
        print()
        print(f'o numero de vendas feito foi: {self.num_venda_feito}')
