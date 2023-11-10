import random

print('*** Bem vindo ao ***\n*** Jo-Ken-Po Vs Máquina ***')

jokenpo=[1,2,3]
'''
legenda
1 = pedra
2 = papel
3 = tesoura
'''
pontos_jogador=0
pontos_maquina=0

txt_vez_do_jogador='\n*** Sua vez, Digite o número da Escolha: ***\n1- Pedra\n2- Papel\n3- Tesoura\n:'
txt_escolha_invalida='\n*** Dígito inválido, tente novamente ***'
txt_jogar_novamente='\n*** jogar novamente? ***\n1- sim\nOutro caractere- não\n:'
txt_vitoria='\n Vencedor !'
txt_derrota='\n Perdedor !'
txt_empate='\n Empate !'
game_over=False


while game_over==False:

    int_escolha_jogador=None
    escolha_maquina=random.choice(jokenpo)
    print('máquina escolheu: ',escolha_maquina)

    while int_escolha_jogador not in jokenpo:
        escolha_jogador=input(txt_vez_do_jogador)
        try:
            int_escolha_jogador=int(escolha_jogador)
            if int_escolha_jogador not in jokenpo:
                print(txt_escolha_invalida)
        except ValueError:
            print(txt_escolha_invalida)
      
    match int_escolha_jogador:
        #PEDRA
        case 1:
            if escolha_maquina==3:
                print(txt_vitoria)
                pontos_jogador+=1
               
            elif escolha_maquina==int_escolha_jogador:
                print(txt_empate)
            else:
                print(txt_derrota)
                pontos_maquina+=1
        #PAPEL 
        case 2:
            if escolha_maquina==1:
                print(txt_vitoria)
                pontos_jogador+=1
               
            elif escolha_maquina==int_escolha_jogador:
                print(txt_empate)
            else:
                print(txt_derrota)
                pontos_maquina+=1
        #TESOURA       
        case 3:
            if escolha_maquina==2:
                print(txt_vitoria)
                pontos_jogador+=1
               
            elif escolha_maquina==int_escolha_jogador:
                print(txt_empate)
            else:
                print(txt_derrota)
                pontos_maquina+=1
      
    txt_placar='\n*** PLACAR ({} - {}) ***'.format(pontos_jogador, pontos_maquina)
    print(txt_placar)
    jogar_novamente=input(txt_jogar_novamente)
    int_jogar_novamente=int(jogar_novamente)

    if int_jogar_novamente!=1:
        game_over=True
    else:
        continue

print("FIM DE JOGO")