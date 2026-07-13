# Adivinhe o Jogador da Copa

Projeto final da disciplina de Estrutura de Dados.

## Tema escolhido

O tema escolhido foi um jogo de adivinhar jogador da Copa do Mundo.

O sistema mostrará dicas sobre jogadores reais da história das Copas, e o usuário tentará acertar o nome do jogador.

## Estrutura de dados principal

A estrutura central do projeto será o dicionário em Python.

Os jogadores serão armazenados usando pares chave -> valor, permitindo busca, consulta e modificação dos dados.
## Modelagem inicial

O sistema usa um dicionário chamado `jogadores`.

Cada chave representa um jogador de forma única. A chave foi formada com a abreviação da seleção, o número da camisa e o nome do jogador.

Exemplos:

- `BRA10_PELE`
- `ARG10_MESSI`
- `POR07_CRISTIANO`

Essa escolha foi feita porque a chave é uma string, portanto é imutável e pode ser usada como chave de dicionário. Além disso, ela facilita a identificação do jogador.

Cada valor do dicionário também é um dicionário, contendo nome, seleção, posição, camisa, geração e dicas.
## Funcionalidades implementadas até agora

- Listar jogadores cadastrados.
- Exibir um menu simples no terminal.
- Tratar opção inválida no menu.

Nesta etapa, o programa já permite interação inicial com o usuário por meio de um menu.7
## Atualização: jogo de adivinhação

Foi adicionada a funcionalidade principal do projeto: jogar adivinhação.

O programa sorteia um jogador cadastrado no dicionário principal e mostra dicas para o usuário tentar acertar o nome.

A pontuação começa em 50 pontos e diminui 10 pontos a cada resposta incorreta.
## Atualização: cadastro de jogador

Foi adicionada a funcionalidade de cadastrar novo jogador.

O usuário informa chave, nome, seleção, posição, camisa, geração e cinco dicas. O novo jogador é inserido no dicionário principal `jogadores`.

Também foi adicionado tratamento de entrada inválida para o número da camisa, impedindo que texto seja aceito quando se espera um número.
## Atualização: atualização de jogador

Foi adicionada a funcionalidade de atualizar jogador.

O usuário informa a chave do jogador e escolhe qual campo deseja alterar: nome, seleção, posição, camisa, geração ou dicas.

A atualização é feita diretamente no dicionário principal `jogadores`. Também há tratamento para chave inexistente e para entrada inválida no número da camisa.