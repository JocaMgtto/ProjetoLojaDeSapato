from utilitarios import (
    cadastrar_sapato,
    estocado,
    fazer_uma_venda,
    receitas,
    busca_sapato
    
)

if __name__ == "__main__":

    
        print("-"*30)
        print(f'Preencha os campos para cadastrar ou <ENTER> para sair')
        print("-"*30)
        while True:
            try:
                print("Para cadastrar um produto no estoque digite: 1")
                print("Para cadastrar uma venda, digite: 2")
                print("para ver receita, digite: 3")
                print("para sair, tecle <ENTER>")
                inicializar = (input("opção: "))
            except ValueError:
                print(f'Caracter invalido, digite <1 ou 2>')
                print()

            if inicializar == "":
                break

            elif inicializar == "1":
                print()
                modelo = input("   Digite o modelo do sapato: ") 
                if modelo == "": 
                    break
                marca = input("   Digite a marca do sapato: ")
                cor = input("   Digite a cor do sapato: ")
                try:
                    tamanho = int(input("   Digite o tamanho do sapato: "))
                    preco = float(input("   Digite o preço do sapato: "))
                except ValueError:
                    print(f'Erro: tamanho ou preco com valor invalido. Digite um valor valido   para  esses campos.')
                print()
                print()

                cadastrar_sapato(modelo, marca, cor, tamanho, preco)
                print()
                estocado()
                print("-"*30)
                print(f'Preencha os campos para cadastrar ou <ENTER> para sair')
                print("-"*30)
               
            elif inicializar == "2":
                print("-"*30)
                print("Preencha os campos com detalhes da venda: ")
                print("-"*30)

                print()

                modelo = str(input("   Modelo: "))
                marca = input("   Marca: ")
                cor = input("   Cor: ")
                try:
                    tamanho = int(input("   Tamanho: "))
                    preco = float(input("   Preço: "))
                except ValueError:
                    print(f'Erro: tamanho ou preco com valor invalido. Digite um valor valido   para  esses campos.')
                print()
                busca_sapato(modelo, marca, cor, tamanho)
                print()
                
                print()
                print("-"*30)
                print(f'Preencha os campos para cadastrar ou <ENTER> para sair')
                print("-"*30)

            else: 
                lucro = 0
                media_lucro = 0
                receitas(lucro, media_lucro)
