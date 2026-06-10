class Pokemon:
    """
    Essa classe cria um Pokemon, que é um monstro que possui atributos como nome,
    ataque, defesa, velocidade e hp. Além disso, o Pokemon possui um metodo copy
    para poder retornar uma copia da instancia.
    """
    def __init__(self, nome, ataque, defesa, velocidade, hp):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.velocidade = velocidade
        self.hp = hp

    def copy(self):
        return Pokemon(
            self.nome,
            self.ataque,
            self.defesa,
            self.velocidade,
            self.hp
        )