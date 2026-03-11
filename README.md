# 🍔 Sistema de Pedidos de Restaurante

> Um projeto educacional em **Python** focado em **Programação Orientada a Objetos (POO)**. Simula o fluxo completo de um restaurante, desde o cardápio até o fechamento do pedido.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange)]()

## 🚀 Funcionalidades

- **Cadastro de Produtos:** Criação dinâmica de itens com nome e preço.
- **Gestão de Cardápio:** Listagem e organização dos produtos disponíveis.
- **Sistema de Pedidos:** Histórico de compras por cliente.
- **Cálculo de Total:** Soma automática e formatação de valores.
- **Extensibilidade:** Código preparado para futuras adições (ex: descontos, taxas).

## 🛠️ Conceitos Aplicados

Este projeto é um estudo prático dos pilares da POO:

- **Classes e Objetos:** Modelagem de `Produto`, `Cliente` e `Restaurante`.
- **Encapsulamento:** Proteção de dados internos das classes.
- **Métodos:** Lógicas de negócio para manipulação de listas e cálculos.
- **Atributos:** Gerenciamento de estado das instâncias.

## 📂 Estrutura do Projeto

```text
Sistema-de-Pedidos-de-Restaurante/
│
├── main.py                 # Ponto de entrada do script
├── classes.py              # Definição das classes (Produto, Cliente, Restaurante)
├── requirements.txt        # Dependências (se houver)
├── README.md               # Documentação deste arquivo
└── .gitignore              # Arquivos ignorados pelo Git
```
## 💻 Como Executar
1. Pré-requisitos
- Python 3.8 ou superior instalado.
- Git instalado (opcional, para clonar).
2. Instalação
- Clone o repositório:
```
git clone https://github.com/arthur-lanzoni-macedo/Sistema-de-Pedidos-de-Restaurante.git
```
3. Crie um ambiente virtual (recomendado):
```
python -m venv venv
```
4. Ative o ambiente:
- Windows: venv\Scripts\activate
- Linux/Mac: source venv/bin/activate
5. Execute o script principal:
```
  python main.py
```
## 📖 Exemplo de Uso
Abaixo, um exemplo de como as classes podem ser instanciadas e utilizadas no código:
```
from classes import Restaurante, Produto, Cliente

# 1. Criar o restaurante e adicionar produtos
restaurante = Restaurante("Sabor & Arte")
restaurante.adicionar_produto(Produto("Hambúrguer", 25.00))
restaurante.adicionar_produto(Produto("Refrigerante", 6.00))

# 2. Criar um cliente e fazer pedidos
cliente = Cliente("Arthur")
cliente.adicionar_item(restaurante, "Hambúrguer")
cliente.adicionar_item(restaurante, "Refrigerante")

# 3. Visualizar total
print(f"Total a pagar: R$ {cliente.calcular_total():.2f}")
```

## 👨‍💻 Autor
Arthur Lanzoni
