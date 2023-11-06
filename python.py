#help()
#explica como funciona os comandos, digitar no terminal (exemplo: print)


#print(4+3+2)
#imprime resultado no terminal

# variável string
#pais="ali"

#type() determina o tipo de variável
#print(type(pais))

#variáveis
#string
#nome="pedro"

#int
#numero=4

#float
#numero=6.5

#bool
#logica = 2>1
#(true)

'''
int()
converte o valor para int

todo input é tratado como string, por isso devemos converter

=
atribui valor

==
compara igualdade
'''

'''
valor=input("tente advinhar o valor")
valor_convertido=int(valor)
resposta=20
if(valor_convertido == resposta):
    print("correto")
else:
    print("errado é vinte")
'''
'''
valor=input("digite o valor")
valor_convertido=int(valor)
if(valor_convertido%2==0):
    print("par")
else:
    print("ímpar")
'''

'''
valor=input("digite o valor")
valor_int=int(valor)

match valor_int:
    case 1:
        # código a ser executado se o valor corresponder ao padrão1
        print(1)
    case 2:
        # código a ser executado se o valor corresponder ao padrão2
        print(2)
    case 3:
        # código a ser executado se o valor corresponder ao padrãoN
        print(3)
    case _:
        # código a ser executado se o valor não corresponder a nenhum dos padrões anteriores
        print("default")
'''
'''
nome="eduardo"

emprego="padeiro"

print("seu nome é {}, e ele trabalha como {}".format(nome,emprego))

'''
'''
for rodada in range(1,11):
    print("rodada {}".format(rodada))
'''
'''
avança de 2 em 2
for rodada in range(1,11,2):
    print("rodada {}".format(rodada))
break
sai do loop

continue
continua o loop
'''