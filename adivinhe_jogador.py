import random

# Projeto: Adivinhe o Jogador da Copa
# Estrutura central: dicionario em Python

jogadores = {
    "BRA10_PELE": {
        "nome": "Pele",
        "selecao": "Brasil",
        "posicao": "Atacante",
        "camisa": 10,
        "geracao": "1950 a 1970",
        "dicas": [
            "Comecou a brilhar em Copas ainda muito jovem.",
            "Fez parte de uma geracao historica da selecao brasileira.",
            "Participou de titulos mundiais do Brasil.",
            "Seu apelido esta ligado a realeza.",
            "E conhecido como Rei do Futebol."
        ]
    },

    "BRA10_RONALDINHO": {
        "nome": "Ronaldinho Gaucho",
        "selecao": "Brasil",
        "posicao": "Meio-campista",
        "camisa": 10,
        "geracao": "Anos 2000",
        "dicas": [
            "Ficou marcado pela alegria jogando futebol.",
            "Tinha dribles, passes e jogadas muito criativas.",
            "Foi campeao mundial no inicio dos anos 2000.",
            "Brilhou muito jogando no Barcelona.",
            "Tambem e conhecido como Bruxo."
        ]
    },

    "BRA09_RONALDO": {
        "nome": "Ronaldo Fenomeno",
        "selecao": "Brasil",
        "posicao": "Atacante",
        "camisa": 9,
        "geracao": "1990 a 2000",
        "dicas": [
            "Foi um atacante muito rapido e forte.",
            "Superou lesoes graves durante a carreira.",
            "Foi artilheiro em uma Copa vencida pelo Brasil.",
            "Usava a camisa 9.",
            "E conhecido como Fenomeno."
        ]
    },

    "BRA10_NEYMAR": {
        "nome": "Neymar",
        "selecao": "Brasil",
        "posicao": "Atacante",
        "camisa": 10,
        "geracao": "2010 a 2020",
        "dicas": [
            "Ficou conhecido por dribles e jogadas individuais.",
            "Foi destaque brasileiro em Copas recentes.",
            "Jogou em clubes importantes da Europa.",
            "Usou a camisa 10 da selecao brasileira.",
            "Seu nome e Neymar."
        ]
    },

    "BRA10_ZICO": {
        "nome": "Zico",
        "selecao": "Brasil",
        "posicao": "Meio-campista",
        "camisa": 10,
        "geracao": "Anos 1970 e 1980",
        "dicas": [
            "Foi um dos grandes nomes do futebol brasileiro.",
            "Era conhecido pela tecnica e pelas cobrancas de falta.",
            "Jogava no meio-campo.",
            "Seu apelido tem relacao com o bairro de Quintino.",
            "E conhecido como Galinho de Quintino."
        ]
    },

    "ARG10_MESSI": {
        "nome": "Lionel Messi",
        "selecao": "Argentina",
        "posicao": "Atacante",
        "camisa": 10,
        "geracao": "2000 a 2020",
        "dicas": [
            "E conhecido por dribles curtos e muita precisao.",
            "Construiu grande parte da carreira no Barcelona.",
            "E canhoto e usa a camisa 10.",
            "Foi campeao mundial pela Argentina.",
            "Seu nome e Lionel Messi."
        ]
    },

    "ARG10_MARADONA": {
        "nome": "Diego Maradona",
        "selecao": "Argentina",
        "posicao": "Meio-campista",
        "camisa": 10,
        "geracao": "Anos 1980 e 1990",
        "dicas": [
            "Liderou sua selecao em uma Copa historica.",
            "Era baixo, habilidoso e muito tecnico.",
            "Marcou dois gols lendarios em uma mesma partida de Copa.",
            "Um desses gols ficou conhecido como mao de Deus.",
            "Seu nome e Diego Maradona."
        ]
    },

    "POR07_CRISTIANO": {
        "nome": "Cristiano Ronaldo",
        "selecao": "Portugal",
        "posicao": "Atacante",
        "camisa": 7,
        "geracao": "2000 a 2020",
        "dicas": [
            "E conhecido pela forca fisica e pelo faro de gol.",
            "Fez historia usando a camisa 7.",
            "E um dos maiores nomes da selecao portuguesa.",
            "Tambem e chamado de CR7.",
            "Seu nome e Cristiano Ronaldo."
        ]
    },

    "FRA10_ZIDANE": {
        "nome": "Zinedine Zidane",
        "selecao": "Franca",
        "posicao": "Meio-campista",
        "camisa": 10,
        "geracao": "1990 a 2000",
        "dicas": [
            "Era conhecido pela elegancia no meio-campo.",
            "Foi destaque da selecao francesa.",
            "Marcou gols importantes em final de Copa.",
            "Usava a camisa 10 da Franca.",
            "Seu sobrenome e Zidane."
        ]
    },

    "FRA10_MBAPPE": {
        "nome": "Kylian Mbappe",
        "selecao": "Franca",
        "posicao": "Atacante",
        "camisa": 10,
        "geracao": "2010 a 2020",
        "dicas": [
            "E conhecido pela velocidade.",
            "Foi campeao mundial ainda jovem.",
            "E um dos grandes nomes recentes da Franca.",
            "Seu primeiro nome comeca com K.",
            "Seu nome e Kylian Mbappe."
        ]
    }
}


def ler_texto_obrigatorio(mensagem):
    texto = input(mensagem)
    texto = texto.strip()

    while texto == "":
        print("Entrada invalida. Esse campo nao pode ficar vazio.")
        texto = input(mensagem)
        texto = texto.strip()

    return texto


def ler_numero_obrigatorio(mensagem):
    numero = input(mensagem)
    numero = numero.strip()

    while not numero.isdigit():
        print("Entrada invalida. Digite apenas numeros.")
        numero = input(mensagem)
        numero = numero.strip()

    return int(numero)


def mostrar_menu():
    print("\n===== ADIVINHE O JOGADOR DA COPA =====")
    print("1 - Listar jogadores cadastrados")
    print("2 - Buscar jogador pela chave")
    print("3 - Jogar adivinhacao")
    print("4 - Cadastrar novo jogador")
    print("5 - Atualizar jogador")
    print("6 - Remover jogador")
    print("0 - Sair")


def listar_jogadores():
    print("\n--- JOGADORES CADASTRADOS ---")

    if len(jogadores) == 0:
        print("Nao existem jogadores cadastrados.")
        return

    for chave in jogadores:
        print("\nChave:", chave)
        print("Nome:", jogadores[chave]["nome"])
        print("Selecao:", jogadores[chave]["selecao"])
        print("Posicao:", jogadores[chave]["posicao"])
        print("Camisa:", jogadores[chave]["camisa"])
        print("Geracao:", jogadores[chave]["geracao"])


def buscar_jogador():
    print("\n--- BUSCAR JOGADOR ---")
    chave = ler_texto_obrigatorio("Digite a chave do jogador: ")
    chave = chave.upper()

    if chave in jogadores:
        print("\n--- JOGADOR ENCONTRADO ---")
        print("Chave:", chave)
        print("Nome:", jogadores[chave]["nome"])
        print("Selecao:", jogadores[chave]["selecao"])
        print("Posicao:", jogadores[chave]["posicao"])
        print("Camisa:", jogadores[chave]["camisa"])
        print("Geracao:", jogadores[chave]["geracao"])
    else:
        print("Jogador nao encontrado. Verifique se a chave foi digitada corretamente.")


def jogar():
    print("\n--- JOGO DE ADIVINHAR JOGADOR ---")

    if len(jogadores) == 0:
        print("Nao existem jogadores cadastrados para jogar.")
        return

    chaves = list(jogadores.keys())
    chave_sorteada = random.choice(chaves)
    jogador = jogadores[chave_sorteada]

    pontos = 50

    print("Tente acertar o nome do jogador pelas dicas.")
    print("Digite o nome sem acentos, como aparece no cadastro.")
    print("Cada dica usada diminui 10 pontos.")

    for dica in jogador["dicas"]:
        print("\nDica:", dica)

        resposta = input("Quem e o jogador? ")
        resposta = resposta.strip()

        if resposta.lower() == jogador["nome"].lower():
            print("\nParabens! Voce acertou.")
            print("Jogador:", jogador["nome"])
            print("Pontuacao:", pontos)
            return
        else:
            print("Resposta incorreta.")
            pontos = pontos - 10

    print("\nVoce nao acertou dessa vez.")
    print("O jogador correto era:", jogador["nome"])


def cadastrar_jogador():
    print("\n--- CADASTRAR NOVO JOGADOR ---")

    chave = ler_texto_obrigatorio("Digite a chave do jogador: ")
    chave = chave.upper()

    if chave in jogadores:
        print("Essa chave ja existe. Cadastro cancelado.")
        return

    nome = ler_texto_obrigatorio("Nome do jogador: ")
    selecao = ler_texto_obrigatorio("Selecao: ")
    posicao = ler_texto_obrigatorio("Posicao: ")
    camisa = ler_numero_obrigatorio("Numero da camisa: ")
    geracao = ler_texto_obrigatorio("Geracao: ")

    dicas = []

    print("Digite 5 dicas para esse jogador.")

    for numero in range(1, 6):
        dica = ler_texto_obrigatorio("Dica " + str(numero) + ": ")
        dicas.append(dica)

    jogadores[chave] = {
        "nome": nome,
        "selecao": selecao,
        "posicao": posicao,
        "camisa": camisa,
        "geracao": geracao,
        "dicas": dicas
    }

    print("Jogador cadastrado com sucesso.")


def atualizar_jogador():
    print("\n--- ATUALIZAR JOGADOR ---")

    chave = ler_texto_obrigatorio("Digite a chave do jogador que deseja atualizar: ")
    chave = chave.upper()

    if chave not in jogadores:
        print("Jogador nao encontrado.")
        return

    print("\nO que deseja atualizar?")
    print("1 - Nome")
    print("2 - Selecao")
    print("3 - Posicao")
    print("4 - Camisa")
    print("5 - Geracao")
    print("6 - Dicas")

    opcao = input("Escolha uma opcao: ")
    opcao = opcao.strip()

    if opcao == "1":
        novo_nome = ler_texto_obrigatorio("Novo nome: ")
        jogadores[chave]["nome"] = novo_nome
        print("Nome atualizado com sucesso.")

    elif opcao == "2":
        nova_selecao = ler_texto_obrigatorio("Nova selecao: ")
        jogadores[chave]["selecao"] = nova_selecao
        print("Selecao atualizada com sucesso.")

    elif opcao == "3":
        nova_posicao = ler_texto_obrigatorio("Nova posicao: ")
        jogadores[chave]["posicao"] = nova_posicao
        print("Posicao atualizada com sucesso.")

    elif opcao == "4":
        nova_camisa = ler_numero_obrigatorio("Nova camisa: ")
        jogadores[chave]["camisa"] = nova_camisa
        print("Camisa atualizada com sucesso.")

    elif opcao == "5":
        nova_geracao = ler_texto_obrigatorio("Nova geracao: ")
        jogadores[chave]["geracao"] = nova_geracao
        print("Geracao atualizada com sucesso.")

    elif opcao == "6":
        novas_dicas = []

        print("Digite as 5 novas dicas.")

        for numero in range(1, 6):
            dica = ler_texto_obrigatorio("Dica " + str(numero) + ": ")
            novas_dicas.append(dica)

        jogadores[chave]["dicas"] = novas_dicas
        print("Dicas atualizadas com sucesso.")

    else:
        print("Opcao invalida. Nenhuma alteracao foi feita.")


def remover_jogador():
    print("\n--- REMOVER JOGADOR ---")

    chave = ler_texto_obrigatorio("Digite a chave do jogador que deseja remover: ")
    chave = chave.upper()

    if chave in jogadores:
        del jogadores[chave]
        print("Jogador removido com sucesso.")
    else:
        print("Jogador nao encontrado. Nenhuma remocao foi feita.")


def executar_programa():
    while True:
        mostrar_menu()

        opcao = input("\nEscolha uma opcao: ")
        opcao = opcao.strip()

        if opcao == "1":
            listar_jogadores()

        elif opcao == "2":
            buscar_jogador()

        elif opcao == "3":
            jogar()

        elif opcao == "4":
            cadastrar_jogador()

        elif opcao == "5":
            atualizar_jogador()

        elif opcao == "6":
            remover_jogador()

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opcao invalida. Escolha uma opcao do menu.")


executar_programa()