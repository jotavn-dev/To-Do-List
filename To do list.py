tarefa = []

def adicinar_tarefa():
    while True:
        try:
            nome_tarefa = input("Informe o nome da tarefa: ")
            tarefa.append({"nome": nome_tarefa, "concluida": False})
            print("\nTarefa adiconada!")
            break
        except KeyboardInterrupt:
            print("\nPrograma encerrado pelo usuário.")
            exit()
    

def listar_tarefa():
    while True:
        try:
            if not tarefa:
                print("Sua lista está vázia.")
            else:
                print("\n" + " Minha lista ".center(50, "-"))
                print()
                for indice, cada_tarefa in enumerate(tarefa):
                    status = " [X]" if cada_tarefa["concluida"] else " [ ]"
                    print(f"{indice + 1} - {cada_tarefa["nome"]:<8}{status}", end="\n\n")
            break
        except KeyboardInterrupt:
            print("Programa encerrado pelo usuário!")
            exit()


def remover_tarefa():
    listar_tarefa()
    tarefa_copiada = tarefa.copy()
    while True:
        try:
            if not tarefa:
                break
            else:
                remover_indice = int(input("Digite o indice da tarefa: ")) - 1
                tarefa.pop(remover_indice)
                print(f"\nA tarefa \"{tarefa_copiada[remover_indice]["nome"]}\" foi removida com sucesso!")
                break
        except ValueError:
            print("\nPor favor, digite apenas números.")
        except KeyboardInterrupt:
            print("Programa encerrado pelo usuário!")
            exit()


def marcar_tarefa():
    listar_tarefa()
    while True:
        try:
            if not tarefa:
                break
            else:
                indice = int(input("Digite o número da tarefa concluída: ")) - 1
                if 0 <= indice < len(tarefa):
                    tarefa[indice]["concluida"] = True
                    print("\nTarefa atualizada!")
                break
        except ValueError:
            print("\nPor favor, digite apenas números.")
        except KeyboardInterrupt:
            print("\nPragrama encerrado pelo usuário!")
            exit()
    

while True:
    print("-"*50)
    opcoes = ["Adicionar Tarefa", "Listar Tarefas", "Remover Tarefa", "Marcar como Concluída", "Sair"]   

    for ordem, cada_opcoes in enumerate(opcoes):
        print(f"{ordem+1} - {cada_opcoes}")
    print("-"*50)

    while True:
        try:
            sua_opcao = int(input("\nInforme a sua opção: "))
            print()
            break
        except ValueError:
            print("\nPor favor, digite apenas números.")
        except KeyboardInterrupt:
            print("\nPrograma encerrado pelo usuário!")
            exit()

    if sua_opcao == 1:
        adicinar_tarefa()
    
    elif sua_opcao == 2:
        listar_tarefa()

    elif sua_opcao == 3:
        remover_tarefa()

    elif sua_opcao == 4:
        marcar_tarefa()
    
    elif sua_opcao == 5:
        exit()
