from velha import acabouvelha

for l in range(0, 3):
    for c in range(0, 3):
        # linhas
        if ma[l][0] == ma[l][1] and ma[l][1] == ma[l][2]:
            acabou = True
            let = ma[l][2]
        # Colunas
        if ma[0][c] == ma[1][c] and ma[1][c] == ma[2][c]:
            acabou = True
            let = ma[2][c]
        # Diagonais
        if ma[0][0] == ma[1][1] and ma[1][1] == ma[2][2]:
            acabou = True
            let = ma[2][2]
        if ma[0][2] == ma[1][1] and ma[1][1] == ma[2][0]:
            acabou = True
            let = ma[2][0]
        # Falta fazer o deu velha
        if ve == 9:
            acabou = True
            let = 'NIGUEM'
# Retorna se o jogo acabou


