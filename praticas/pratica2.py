# AULA 2 EXERCICIO 01 ==========================================

class Carro:
    def __init__(self, modelo: str, cor: str, ano: int):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f"{self.modelo} | {self.cor} | {self.ano}"

fiat = Carro("Siena", "Preto", 2008)

# AULA 2 EXERCICIO 02 ===========================================

class Restaurante:
    def __init__(self, nome: str, categoria: str, ativo: bool, endereco: str, cardapio: list):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.endereco = endereco
        self.cardapio = cardapio

    def __str__(self):
        return f"{self.nome} | {self.categoria} | {self.ativo} | {self.endereco} | {self.cardapio}"

pizzaria_don_piero = Restaurante("Don Piero", "Italiano", True, "Avenida Jean Carlo Penne, 254", 
                [
                    "Calabresa",
                    "Muçarela",
                    "Portuguesa",
                    "Frango com Catupiry",
                    "Marguerita",
                    "Rúcula com Tomate Seco",
                    "Alho-Poró com Bacon",
                    "Pera com Gorgonzola",
                    "Creme de Avelã com Morango",
                    "Banana com Canela"
                ])

# AULA 2 EXERCICIO 03 & 04 ===========================================
class Restaurante:
    def __init__(self, nome: str, categoria: str):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def __str__(self):
        return f"{self.nome} | {self.categoria} | {self.ativo}"


restaurante = Restaurante("Mos", "Gourmet")

print(restaurante)

# AULA 2 EXERCICIO 05 ===============================================

class Cliente:
    def __init__(self, nome, email, endereco, cpf):
        self.nome = nome
        self.email = email
        self.endereco = endereco
        self.cpf = cpf

cliente1 = Cliente("Pedro", "p@b.com", "Rua Mais, 493", "123456789-00")
cliente2 = Cliente("Maria", "m@b.com", "Rua Menos, 999", "123456789-01")
cliente3 = Cliente("João", "j@b.com", "Rua Igual, 555", "123456789-02")
        