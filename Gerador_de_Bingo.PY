import random


qtd = int(input("Quantas cartelas voce precisa? "))

for i in range(qtd):

    bingo = [[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

    # Criar uma lista e embaralhar
    numbers = list(range(10, 60))
    random.shuffle(numbers)

    for i in range(5):
        for j in range(5):
            bingo[i][j] = numbers.pop(0)
        bingo[2][2] = 'x'

    print("\n", "  B   I   N   G   O")
    for linha in bingo:
        print(linha)