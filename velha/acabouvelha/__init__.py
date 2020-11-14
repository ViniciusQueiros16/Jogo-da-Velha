def fimdejogo(ma, ve=0):
    for l in range(0, 3):
        for c in range(0, 3):
            # linhas
            if ma[l][0] == ma[l][1] and ma[l][1] == ma[l][2]:
                let = ma[l][2]
                return let
            # Colunas
            if ma[0][c] == ma[1][c] and ma[1][c] == ma[2][c]:
                let = ma[2][c]
                return let
            # Diagonais
            if ma[0][0] == ma[1][1] and ma[1][1] == ma[2][2]:
                let = ma[2][2]
                return let
            if ma[0][2] == ma[1][1] and ma[1][1] == ma[2][0]:
                let = ma[2][0]
                return let
    # Velha
    if ve == 9:
        let = 'niguem'
        return let
    # Retorna se o jogo acabou
