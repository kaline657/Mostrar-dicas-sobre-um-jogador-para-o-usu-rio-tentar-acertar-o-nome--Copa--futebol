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

## Decisão de implementação

No início do desenvolvimento, foi planejada uma versão com interface gráfica local usando Tkinter. Nessa primeira tentativa, a estrutura foi separada em pastas, como `dados`, `funcoes` e `interface`, com o objetivo de deixar o código mais organizado e visualmente mais próximo de um sistema com tela própria.

A ideia inicial era entregar o projeto com uma interface local, em que o usuário pudesse jogar clicando em botões, visualizando dicas e respostas em uma janela gráfica. Porém, durante os testes, percebi que essa versão estava ficando mais difícil de ajustar e explicar dentro do prazo. Além disso, a interface gráfica estava tornando o projeto mais complexo do que o necessário para o objetivo principal da atividade.

Como o foco do trabalho era o uso de dicionários em Python como estrutura central, optei por refazer o projeto em uma versão mais simples, funcionando pelo terminal, com menu interativo. Essa decisão deixou o código mais claro, mais fácil de testar e mais alinhado com os requisitos da disciplina.

A versão final manteve as principais ideias planejadas desde o início:

- jogadores armazenados em dicionários;
- dicas para o usuário tentar adivinhar o jogador;
- busca por chave;
- cadastro de novos jogadores;
- atualização de dados;
- remoção de jogadores;
- tratamento de entradas inválidas.

Também decidi usar o GitHub para registrar o desenvolvimento por etapas, fazendo commits separados para cada parte importante do projeto. Dessa forma, foi possível mostrar a evolução do trabalho, desde a estrutura inicial até a versão final no terminal.

## Observação sobre a tentativa com interface

Antes da versão final, foi feita uma tentativa de desenvolver uma interface gráfica local usando Tkinter. Essa tentativa ajudou no planejamento da estrutura do sistema, mas não foi mantida como versão final porque aumentava a complexidade do projeto e dificultava a explicação do código.

A versão escolhida para entrega foi a versão em terminal, pois ela demonstra melhor o uso de dicionários, funções, menu, consultas e modificações de dados, que são os pontos centrais da atividade.
<img width="1918" height="1017" alt="image" src="https://github.com/user-attachments/assets/3d509c8f-b469-40d9-8ba3-6bea22df64d9" />


## Relatório de uso de IA

Foi utilizada a ferramenta ChatGPT como apoio durante o desenvolvimento do trabalho.

A IA foi usada para auxiliar na interpretação do enunciado, organização das etapas, revisão da modelagem com dicionários, sugestão de funções, explicação do funcionamento do código e estruturação do README.

No início, também foi solicitado apoio para tentar criar uma interface gráfica local usando Tkinter. Porém, após testes e análise, essa ideia foi adaptada. A versão com interface não foi escolhida para a entrega final, pois deixava o projeto mais complexo do que o necessário.

Depois disso, o projeto foi refeito em uma versão mais simples, usando terminal e menu interativo. Essa escolha foi feita para manter o foco no conteúdo da disciplina: uso de dicionários em Python, escolha de chaves, consultas, inserção, atualização, remoção e tratamento de erros.

O código foi desenvolvido por etapas, com commits separados no GitHub, para registrar a evolução do trabalho. As funcionalidades foram testadas durante o desenvolvimento, incluindo listagem, busca, jogo de adivinhação, cadastro, atualização, remoção e tratamento de entradas inválidas.

Algumas sugestões da IA foram aceitas, outras foram adaptadas, e outras foram deixadas de lado. A principal adaptação foi abandonar a interface gráfica e seguir com uma versão mais simples e explicável no terminal.

Com o desenvolvimento do projeto, foi possível compreender melhor:

- como usar dicionários em Python;
- como escolher chaves únicas;
- como buscar valores diretamente por chave;
- como atualizar registros dentro de um dicionário;
- como remover registros;
- como validar entradas do usuário;
- como organizar o desenvolvimento em etapas usando GitHub.



