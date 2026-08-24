# Pedra, Papel, Tesoura, Lagarto, Spock

Jogo em Python com o clássico "esquema" criado pelo Sheldon Cooper em The Big Bang Theory: uma versão do pedra-papel-tesoura com duas jogadas a mais (lagarto e Spock), o que reduz bastante as chances de empate e deixa a lógica de decisão mais interessante de programar.

Fiz esse projeto pra treinar estrutura de decisão, controle de fluxo e organização de lógica de jogo em Python, sem depender de bibliotecas externas pesadas.

## Como funciona

O jogador escolhe uma das cinco opções e o computador escolhe a sua de forma aleatória. O programa compara as duas jogadas seguindo as regras do jogo:

- Tesoura corta Papel
- Papel cobre Pedra
- Pedra esmaga Lagarto
- Lagarto envenena Spock
- Spock quebra Tesoura
- Tesoura decapita Lagarto
- Lagarto come Papel
- Papel desmente Spock
- Spock vaporiza Pedra
- Pedra amassa Tesoura

No final, o resultado da rodada (vitória, derrota ou empate) é exibido pro jogador.

## Como rodar

Pré-requisitos: Python 3 instalado na máquina.

```bash
git clone https://github.com/Lrd074/Pedra-Papel-Tesoura-Spock-Lagarto.git
cd Pedra-Papel-Tesoura-Spock-Lagarto/pptsl
python nome_do_arquivo.py
```

Substitua `nome_do_arquivo.py` pelo arquivo principal do jogo dentro da pasta `pptsl`.

## Próxima atualização

A próxima versão vai integrar um banco de dados SQLite para armazenar o histórico de partidas e o placar do jogador contra o computador, persistindo os resultados entre execuções em vez de perdê-los a cada vez que o jogo é fechado.

## Tecnologias

- Python 3

## Autor

Desenvolvido por Leonardo Lima como parte dos estudos de lógica de programação em Python.