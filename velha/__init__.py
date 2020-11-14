from velha import desenhodavelha
from velha import jogavelha
from velha import acabouvelha
import sys
ve = 0
ma = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
simb = '\033[31mx\033[m'
desenhodavelha.quadrados(ma)
while True:
    while True:
        po = int(input(f'\033[35mVai jogar \033[m{simb} \033[35mem qual posição? \033[m'))
        r = jogavelha.jogar(ma, simb, po)
        if not r:
            print('\033[31mJOGADA INVALIDA!\033[m')
        if r:
            break
    if simb == '\033[31mx\033[m':
        simb = '\033[34mo\033[m'
    else:
        simb = '\033[31mx\033[m'
    desenhodavelha.quadrados(ma)
    ve += 1
    if acabouvelha.fimdejogo(ma, ve):
        break
print('\033[1;36mJOGO FINALIZADO !!!')
print(f'Quem ganhou foi {acabouvelha.fimdejogo(ma)}!')
sys.exit()
