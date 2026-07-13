# Adivinhe o Jogador da Copa

Projeto final da disciplina de Estrutura de Dados.

## Tema escolhido

O tema escolhido foi **Jogo de Adivinhar Jogador da Copa**.

O sistema mostra dicas sobre jogadores reais da história das Copas do Mundo, e o usuário tenta acertar o nome do jogador. A cada resposta incorreta, uma nova dica é exibida.

Esse tema está relacionado à proposta de “Jogo de adivinhar jogador”, em que o sistema apresenta pistas sobre um jogador e permite que o usuário tente descobrir o nome correto.

## Objetivo do projeto

O objetivo do projeto é aplicar o uso de dicionários em Python como estrutura central de armazenamento, consulta e modificação de dados.

O programa permite armazenar jogadores, consultar informações, jogar uma rodada de adivinhação, cadastrar novos jogadores, atualizar dados já cadastrados e remover jogadores do sistema.

## Modelagem dos dicionários

A estrutura central do projeto é o dicionário em Python.

O principal dicionário do sistema se chama `jogadores`. Ele armazena os jogadores cadastrados no formato **chave -> valor**.

Cada chave representa um jogador de forma única. O valor associado a cada chave também é um dicionário, contendo as informações daquele jogador.

Exemplo da estrutura usada:

```python
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
    }
}
```

Dentro de cada jogador, foram armazenados os seguintes dados:

- nome;
- seleção;
- posição;
- número da camisa;
- geração ou período em que jogou;
- lista de dicas.

O sistema já inicia com 10 jogadores reais cadastrados, de diferentes seleções e gerações.

## Justificativa das chaves

As chaves do dicionário foram criadas juntando três informações principais:

- abreviação da seleção;
- número da camisa;
- nome do jogador.

Exemplos de chaves usadas:

```text
BRA10_PELE
ARG10_MESSI
POR07_CRISTIANO
FRA10_ZIDANE
```

Essa escolha foi feita porque a chave precisa ser **única**, **imutável** e **hashable** para ser usada em um dicionário Python.

Como as chaves são strings, elas atendem a esse requisito. Além disso, esse formato facilita a identificação do jogador e evita confusão entre jogadores com nomes parecidos.

Por exemplo, a chave `BRA10_PELE` indica um jogador do Brasil, camisa 10, chamado Pelé.

## Funcionalidades implementadas

O sistema possui as seguintes funcionalidades:

1. **Listar jogadores cadastrados**  
   Exibe todos os jogadores armazenados no dicionário principal.

2. **Buscar jogador pela chave**  
   Permite consultar diretamente um jogador usando sua chave no dicionário.

3. **Jogar adivinhação**  
   Sorteia um jogador e mostra dicas para o usuário tentar acertar o nome.

4. **Cadastrar novo jogador**  
   Permite inserir um novo jogador no dicionário principal.

5. **Atualizar jogador**  
   Permite alterar dados de um jogador já cadastrado.

6. **Remover jogador**  
   Permite excluir um jogador do dicionário principal usando sua chave.

## Explicação das funcionalidades

### 1. Listar jogadores cadastrados

Mostra todos os jogadores armazenados no dicionário principal, exibindo chave, nome, seleção, posição, camisa e geração.

### 2. Buscar jogador pela chave

Permite buscar diretamente um jogador usando sua chave no dicionário.

Se a chave existir, os dados do jogador são exibidos. Se a chave não existir, o programa informa que o jogador não foi encontrado.

### 3. Jogar adivinhação

O programa sorteia um jogador cadastrado no dicionário e mostra dicas para o usuário tentar acertar o nome.

A pontuação começa em 50 pontos. A cada resposta incorreta, o usuário recebe outra dica e perde 10 pontos.

### 4. Cadastrar novo jogador

Permite inserir um novo jogador no dicionário principal.

O usuário informa chave, nome, seleção, posição, camisa, geração e cinco dicas.

O programa verifica se a chave já existe antes de cadastrar.

### 5. Atualizar jogador

Permite alterar os dados de um jogador já cadastrado.

O usuário informa a chave do jogador e escolhe qual campo deseja atualizar: nome, seleção, posição, camisa, geração ou dicas.

### 6. Remover jogador

Permite remover um jogador do dicionário principal usando a chave.

Se a chave existir, o jogador é removido. Se a chave não existir, o programa informa que nenhum jogador foi encontrado.

## Tratamento de erros e robustez

O programa trata os seguintes casos:

- opção inválida no menu;
- busca por chave inexistente;
- atualização de jogador inexistente;
- remoção de jogador inexistente;
- tentativa de cadastrar jogador com chave repetida;
- campo vazio em entradas obrigatórias;
- texto digitado quando se espera número da camisa.

Quando o usuário digita uma opção inválida, o programa mostra uma mensagem e retorna ao menu. Quando o usuário digita uma chave que não existe, o programa informa que o jogador não foi encontrado. Quando o número da camisa é digitado incorretamente, o sistema pede o valor novamente.

## Como executar o programa

Para executar o projeto, é necessário ter o Python instalado no computador.

No terminal, dentro da pasta do projeto, execute:

```bash
python adivinhe_jogador.py
```

Depois disso, o menu será exibido:

```text
===== ADIVINHE O JOGADOR DA COPA =====
1 - Listar jogadores cadastrados
2 - Buscar jogador pela chave
3 - Jogar adivinhacao
4 - Cadastrar novo jogador
5 - Atualizar jogador
6 - Remover jogador
0 - Sair
```

O usuário deve digitar o número da opção desejada e seguir as instruções mostradas no terminal.

## Arquivos do projeto

O projeto possui os seguintes arquivos:

- `adivinhe_jogador.py`: arquivo principal com o código do sistema.
- `README.md`: documentação do projeto.

## Relatório de uso de IA

Foi utilizada a ferramenta ChatGPT como apoio durante o desenvolvimento do trabalho.

A IA foi usada para auxiliar na interpretação do enunciado, organização das etapas, revisão da modelagem com dicionários, sugestão de funções, explicação do funcionamento do código e estruturação do README.

O código foi construído por etapas, com commits separados no repositório, para registrar a evolução do projeto. As funcionalidades foram testadas durante o desenvolvimento, incluindo listagem, busca, jogo de adivinhação, cadastro, atualização, remoção e tratamento de entradas inválidas.

Algumas sugestões foram adaptadas para manter o projeto simples e coerente com o conteúdo da disciplina. Foram evitadas bibliotecas externas, banco de dados, interface web ou estruturas mais avançadas, mantendo o foco no uso de dicionários em Python.

Com o desenvolvimento do projeto, foi possível compreender melhor o uso de dicionários, a escolha de chaves únicas, a busca direta por chave, a atualização de valores e o tratamento de erros em programas interativos.



- O que eu modifiquei em relação às sugestões da IA, e por quê:

- O que eu testei ou verifiquei no programa:

- O que eu rejeitei das sugestões da IA, e a justificativa:

- O que eu aprendi de novo durante o desenvolvimento do projeto:
