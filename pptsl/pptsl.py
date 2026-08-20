# importações
from random import randrange
from emoji import emojize
from time import sleep

# cores
cores = {
    "vermelho": "\033[31m",
    "Azul": "\033[34m",
    "Verde": "\033[32m",
    "roxo": "\033[35m",
    "vazio": "\033[m",
}

# pontos
Pontos_pc = 0
Pontos_player = 0
comeco = 0


def nova_partida(Pontos_pc, Pontos_player):  # =={Define a condição de nova partida}
    nova = int(
        input("Deseja começar uma nova partida?\n Sim [1] Não [2]\nDigite aqui:")
    )

    if nova == 1:
        Pontos_player = 0
        Pontos_pc = 0
        sleep(3)


def voce_ganhou(player, pc):  # =={Alerta de vítoria}
    global Pontos_pc
    global Pontos_player
    Pontos_player += 1
    print(f'{cores["Verde"]}{'-+-' * 10}{cores["vazio"]}')
    print(
        f"Você ganhou esse round!!\n Sua escolha foi {player} e a do seu oponente foi {pc}"
    )
    print(f"--Seus Pontos {Pontos_player} x Pontos do Pc {Pontos_pc}--")
    print(f'{cores["Verde"]}{'-+-' * 10}{cores["vazio"]}')


def vitorias(player, pc):  # =={Define a condição de vítoria}
    return (
        player == 0
        and (pc == 1 or pc == 2)
        or player == 1
        and (pc == 2 or pc == 3)
        or player == 2
        and (pc == 3 or pc == 4)
        or player == 3
        and (pc == 0 or pc == 4)
        or player == 4
        and (pc == 0 or pc == 1)
    )


# regras e inicio
if comeco == 0:
    while True:
        comeco = int(
            input(
                "\nVamos começar um jogo?\nBem as regras são as seguinte;\nTesoura corta papel\nPapel cobre pedra\nPedra esmaga lagarto\nLagarto envenena Spock\nSpock esmaga (ou derrete) tesoura\nTesoura decapita lagarto\nLagarto come papel\nPapel refuta Spock\nSpock vaporiza pedra\nPedra amassa tesoura\nGanha quem fizer 3 pontos primeiro\n \nComeçar [1] Parar [2]\n \nDigite aqui:"
            )
        )

        if comeco > 2:
            print("Opa, parece que você não escolheu um dos números!")
            comeco = 0
        elif comeco == 2:
            print(emojize("Certo... até mais:cry:", language="alias"))
            sleep(3)
            break

        # jogo
        if comeco == 1:
            print("Começando...")
            sleep(3)

            while True:
                if Pontos_pc == 3:
                    print(
                        emojize(
                            "Você perdeu, mais sorte na proxima... :cry:",
                            language="alias",
                        )
                    )
                    nova_partida()
                elif Pontos_player == 3:
                    print(emojize("Você ganhou!!:smile:", language="alias"))
                    nova_partida()

                # começo
                print(f'{cores["roxo"]}{'-=-' * 10}{cores["vazio"]}')
                player = int(
                    input(
                        "Escolha um número referente ao que você quer jogar:\n Pedra = 0 \n Tesoura = 1\n Lagarto = 2\n Papel = 3\n Spock = 4\n Digite aqui:"
                    )
                )
                print(f'{cores["roxo"]}{'-=-' * 10}{cores["vazio"]}')
                sleep(1)
                pc = randrange(0, 5)

                # game
                if player >= 5 or player < 0:
                    sleep(1)
                    print("Algo não está certo... Vamos recomeçar!")
                    sleep(1)

                elif player == pc:
                    print(f'{cores["Azul"]}{'-+-' * 10}{cores["vazio"]}')
                    print("Eita, deu empate")
                    print(f"--Seus Pontos {Pontos_player} x Pontos do Pc {Pontos_pc}--")
                    print(f'{cores["Azul"]}{'-+-' * 10}{cores["vazio"]}')

                elif vitorias(player, pc):
                    voce_ganhou(player, pc)

                else:
                    Pontos_pc += 1
                    print(f'{cores["vermelho"]}{'-+-' * 10}{cores["vazio"]}')
                    print(
                        f"Você perdeu esse round!\nSua escolha foi {player} e a do seu oponente foi {pc}"
                    )
                    print(f"--Seus Pontos {Pontos_player} x Pontos do Pc {Pontos_pc}--")
                    print(f'{cores["vermelho"]}{'-+-' * 10}{cores["vazio"]}')
