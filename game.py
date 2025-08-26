import random

# Lista de palavras
palavras = [
    # Animais
    "gato", "cachorro", "elefante", "girafa", "tigre", "leao", "coelho", "macaco", "urso", "pinguim",

    # Frutas
    "banana", "uva", "abacaxi", "laranja", "morango", "melancia", "manga", "kiwi", "pera", "cereja",

    # Objetos
    "cadeira", "mesa", "computador", "janela", "telefone", "livro", "caneta", "teclado", "foguete", "relogio",

    # Cores
    "azul", "vermelho", "amarelo", "verde", "roxo", "preto", "branco", "cinza", "laranja", "rosa",

    # Países
    "brasil", "argentina", "canada", "japao", "franca", "alemanha", "italia", "espanha", "mexico", "portugal",

    # Profissões
    "professor", "engenheiro", "medico", "advogado", "artista", "programador", "piloto", "bombeiro", "policial", "jornalista"
]

# Desenhos da forca
forca = [
    """
     ------
     |    |
     |
     |
     |
     |
    ====
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
    ====
    """,
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    ====
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    ====
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    ====
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    ====
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    ====
    """
]

# Função principal do jogo
def jogar_forca():
    palavra_secreta = random.choice(palavras)
    letras_descobertas = ["_"] * len(palavra_secreta)
    tentativas = len(forca) - 1
    erros = 0

    print("\n🎮 Bem-vindo ao Jogo da Forca!")

    # Loop do jogo
    while erros < tentativas and "_" in letras_descobertas:
        print(forca[erros])
        print(" ".join(letras_descobertas))
        letra = input("\nDigite uma letra: ").lower()

        if letra in palavra_secreta:
            for i, l in enumerate(palavra_secreta):
                if l == letra:
                    letras_descobertas[i] = letra
            print("✅ Boa! Você acertou uma letra.")
        else:
            erros += 1
            print(f"❌ Letra errada! Você ainda tem {tentativas - erros} tentativas.")

    # Resultado final
    print(forca[erros])
    if "_" not in letras_descobertas:
        print("🎉 Parabéns! Você venceu! A palavra era:", palavra_secreta)
    else:
        print("💀 Você perdeu! A palavra correta era:", palavra_secreta)

# Loop para jogar várias vezes
while True:
    jogar_forca()
    jogar_novamente = input("\n🔄 Deseja jogar novamente? (s/n): ").lower()
    if jogar_novamente != "s":
        print("👋 Obrigado por jogar! Até a próxima!")
        break
