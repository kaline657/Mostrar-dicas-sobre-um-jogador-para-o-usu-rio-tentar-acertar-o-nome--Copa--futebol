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