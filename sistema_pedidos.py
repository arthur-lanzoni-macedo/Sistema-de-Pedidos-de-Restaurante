class Produto():
    
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def mostrar_dados(self):
        print(f'Produto: {self.nome}')
        print(f'Preço: R$ {self.preco}')
        
class Cliente():
    
    def __init__(self, nome, pedidos):
        self.nome = nome
        self.pedidos = []
        
    def fazer_pedido(self, produto):        
        self.pedidos.append(produto)
        print(f'{self.nome} pediu {produto.nome}')
        
    def ver_pedidos(self):  
        print(f'Pedidos de {self.nome}:\n')     
        for pedidos in self.pedidos:
            print(pedidos.nome)
    
    def calcular_valor_total(self):
        preco_total = 0
                
        for pedido in self.pedidos:
            preco_total += pedido.preco
        
        print(f'Total do pedido: R$ {preco_total}')
        
class Restaurante():
    lista_de_produtos = []
    
    def adicionar_produto(self, produto):
        self.lista_de_produtos.append(produto)
        print(f'Produto {produto.nome} adicionado ao cardápio')
    
    def mostrar_cardapio(self):
        print('Cardápio:\n')
        
        for produtos in self.lista_de_produtos:
            print(f'{produtos.nome} - R$ {produtos.preco}')
            
# =========================
# TESTE DO SISTEMA
# =========================

# Criando produtos
pizza = Produto("Pizza", 45)
hamburguer = Produto("Hamburguer", 20)
refrigerante = Produto("Refrigerante", 7)

# Criando restaurante
restaurante = Restaurante()

# Adicionando produtos ao cardápio
restaurante.adicionar_produto(pizza)
restaurante.adicionar_produto(hamburguer)
restaurante.adicionar_produto(refrigerante)

print("\n")

# Mostrar cardápio
restaurante.mostrar_cardapio()

print("\n")

# Criando cliente
cliente1 = Cliente("Arthur", [])

# Cliente faz pedidos
cliente1.fazer_pedido(pizza)
cliente1.fazer_pedido(refrigerante)

print("\n")

# Ver pedidos do cliente
cliente1.ver_pedidos()

print("\n")

# Calcular total do pedido
cliente1.calcular_valor_total()