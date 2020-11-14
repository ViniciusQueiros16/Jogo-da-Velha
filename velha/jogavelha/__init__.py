def jogar(ma, s='', po=0):
    mudou = False
    # Recebe o simbolo na posição e retorna se mudou ou não
    for l in range(0, 3):
        for c in range(0, 3):
            if ma[l][c] == po:
                ma[l][c] = s
                mudou = True
    return mudou
