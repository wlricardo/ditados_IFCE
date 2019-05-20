import time

def menu_principal():
    print("\n"+66*"=")
    print("DITADOS PUPULARES".center(66))
    print(66*"="+"\n")
    print("  1 - INSERIR")
    print("  2 - REMOVER")
    print("  3 - LISTAR")
    print("  4 - Opção 4")
    print("  ----------------------")
    print("  0 - Sair do Aplicativo\n")
    return input("  Escolha uma opção: ")


#def submenu():
#    print("\n"+66*"=")
#    print("Título do Submenu".center(66))
#    print(66*"="+"\n")
#    print("  1 - Opção 1")
#    print("  2 - Opção 2")
#    print("  3 - Opção 3")
#    print("  4 - Opção 4")
#    print("  ----------------------------")
#    print("  0 - Voltar ao menu principal\n")
#    return input("  Escolha uma opção: ")

def principal():
    alterado = False
    lista = []
    ultimo_codigo = 0
    
    try:
        arq = open("ditados.txt", "rb")
        ultimo_codigo = pickle.load(arq)
        lis_alu = pickle.load(arq)
        arq.close()
    except FileNotFoundError:
        arq = open("ditados.txt", "wb")
        pickle.dump(ultimo_codigo, arq)
        pickle.dump(lista, arq)
        arq.close()
        
    while True:
        op = menu_principal()
        if op == '0':
            if alterado:
                res = input("  Deseja salvar as alterações no arquivo ? (S/N): ")
                while res.upper() != 'S' and res.upper() != 'N':
                    res = input("  Responda S ou N: ")
                if res.upper() == 'S':
                    arq = open("ditados.txt", "wb")
                    pickle.dump(ultimo_codigo, arq)
                    pickle.dump(lista, arq)
                    arq.close()
                    print("  Alterações salvas")
                else:
                    print("  Alterações descartadas")
            print("\n  ** Fim do aplicativo **")
            time.sleep(3)
            break
        elif op == '1':
            while True:
                op2 = submenu()
                if op2 == '0':
                    break
                elif op2 == '1':
                    print(66*"-")
                    print("{:s}".format("Título do Submenu 1".center(66)))
                elif op2 == '2':
                    print(66*"-")
                    print("{:s}".format("Título do Submenu 2".center(66)))
                elif op2 == '3':
                    print(66*"-")
                    print("{:s}".format("Título do Submenu 3".center(66)))
                elif op2 == '4':
                    print(66*"-")
                    print("{:s}".format("Título do Submenu 4".center(66)))
                else:
                    print("\n  * ENTRADA INVÁLIDA *\n")
        elif op == '2':
            print(66*"-")
            print("{:s}".format("Título da Opção 2".center(66)))
            print(66*"-")
        elif op == '3':
            print(66*"-")
            print("{:s}".format("Título da Opção 3".center(66)))
            print(66*"-")
        elif op == '4':
            print(66*"-")
            print("{:s}".format("Título da Opção 4".center(66)))
            print(66*"-")
        else:
            print("\n  * ENTRADA INVÁLIDA *\n")

principal()
