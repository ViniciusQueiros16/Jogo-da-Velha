def quadrados(m):
    # Mostra o desenho da velha
    for l in range(0, 3):
        print('\033[32m+---+---+---+\033[m')
        for c in range(0, 3):
            print(f'\033[32m|', m[l][c], end=' ')
        print('|\033[m')
    print('\033[32m+---+---+---+\033[m')
