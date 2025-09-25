from dataclasses import dataclass
@dataclass

class Estoque:
    num_total_sapato: int

    def exibir(self):
        print(f'o numero de sapatos no estoque é: {self.num_total_sapato}')