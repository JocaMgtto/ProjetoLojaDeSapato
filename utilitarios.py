
from estoque import Estoque
from sapato import Sapato
from venda import Venda
from receita import Receita


# Variavies globais
sapatos_totais = []
list_vendas = []

# cadastra um sapato no estoque
def cadastrar_sapato(modelo, marca, cor, tamanho, preco):
    novo_sapato = Sapato(modelo=modelo, marca=marca, cor=cor, tamanho=tamanho, preco=preco)
    sapatos_totais.append(novo_sapato)
    print(f' {sapatos_totais}')
    novo_sapato.exibir()

# retorna o numero de sapatos no estoque da loja
def estocado():
    total = len(sapatos_totais)
    total_estoque = Estoque(num_total_sapato=total)
    total_estoque.exibir()

# retorna a lista de vendas feitas, atualiza total_venda a cada venda
def fazer_uma_venda(modelo, marca, cor, tamanho, preco):
    produto = Sapato(modelo = modelo, marca= marca, cor=cor, tamanho= tamanho, preco=preco)
    list_vendas.append(produto)
    print(f'Vendas cadastradas: \n{list_vendas}')
    total_venda = len(list_vendas)
    venda = Venda(num_venda_feito = total_venda)
    venda.exibir()

#retorna a média do lucro total, ou apenas o lucro bruto, obtido atraves da venda de sapatos.
def receitas(lucro, media_lucro):
    Receita(lucro=lucro, media_lucro= media_lucro )

    lucro = sum(venda.preco for venda in list_vendas)

    print()
    print(f'O lucro bruto é: {lucro}')
    print()
    if len(list_vendas) > 0:
        media_lucro = lucro // len(list_vendas)
        print(f'O lucro bruto médio é: {media_lucro}')
    else: 
        print(f'Nao foi feito nenhuma venda: \n {list_vendas}')
        print(f'-'*30)
        media_lucro = 0
        print(f'lucro bruto médio: {media_lucro}')
        print(f'-'*30)
    print()
    print()

# busca um sapato na lista *sapatos_totais* e remove ele da lista quando a venda for feita, caso sapato nao estiver no estoque, nao remove o sapato.
def busca_sapato(modelo, marca, cor, tamanho):
    for produto in sapatos_totais:
        if modelo == produto.modelo and marca == produto.marca and cor == produto.cor and tamanho == produto.tamanho:
            sapatos_totais.remove(produto)
            print()
            print(f'os sapatos no estoque agora sao: \n {sapatos_totais}')
            print()

            fazer_uma_venda(produto.modelo, produto.marca, produto.cor, produto.tamanho, produto.preco)

        else: 
            print(f'produto nao encontrado no estoque.')




          
                

