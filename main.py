from random import randint
from velha import Velha
velha = Velha()
while True:
    controle = []
    c = 0
    p2 = None
    
    print("=-"*10,"Jogo da velha","-="*10)
    print("Escolha entre bolinha e xisinho:\nO\nX")
    x_or_o = input(">>").upper()

    if x_or_o != "X" and x_or_o != "O":
        print("\n!!!! Apenas x e O !!!!\n")
        continue
    if x_or_o == "X":
        p2 = "O"
    else:
        p2 = "X"

    print("!! OK vamos joagar !!\n")

    while c != 4:
        print(velha.menu())
        print("\nEscolha um numero corresponde a posição que deseja:")
        a = int(input())
        if not a in [x for x in range(1,10)] and a in controle:
            print("apenas os números indicados e não selecionados")
            continue
        velha.pos(b,p2)
        velha.pos(a,x_or_o)
        b = randint(1,9)
        if b in controle:
            continue
        velha.pos(b,p2)
       
        controle.append(b)
        if velha.verify()[1]:
            print(velha.verify()[0])
            break
        c += 1

    print("=-"*10,"Vencedor","-="*10)
    if not velha.verify()[1]:
        print(velha.verify()[0])
    print()

    cont = input("deseja continuar??(s/n)").lower()
    if cont != "n" and cont != "s":
        print("Apenas S e N")
        continue
    elif cont == "n":
        break
    
