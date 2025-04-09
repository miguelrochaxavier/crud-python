class CRUDPython():

    def __init__(self, cargas):
        self.cargas = cargas

    def MenuCRUDPython(self):
        print("Seja bem vindo ao CRUDPython")
        while True:
            try:
                choise = int(input("\n[1] Adicionar cargas [C] \n[2] Visualizar cargas[R] \n[3] Atualizar cargas[U] \n[4] Apagar cargas [D] \n[5] Sair \nInsira o número para acessar o destino: "))
            except ValueError:
                print("Error! Insira uma seção válida.")
                continue

            if choise == 1:
                self.adicionar_carga()
            elif choise == 2:
                self.visualizar_cargas()
            elif choise == 3:
              self.atualizar_cargas()
            elif choise == 4:
                self.apagar_cargas()
            elif choise == 5:
                print("Finalizando programa....")
                break
            else :
                print("Error! Insira um valor válido.")

    def adicionar_carga(self):
        carga = input("Adiciono o nome da carga que deseja adicionar: ")
        self.cargas.append(carga)
        print("Carga adicionada com sucesso")
        self.MenuCRUDPython()

    def visualizar_cargas(self):
        print("Cargas atuais:")
        for i, carga in enumerate(self.cargas): #Enumerando as cargas // Diferente de for in range(0, 10) que gera um TETO;
            print(f"{i + 1}. {carga}")
        self.MenuCRUDPython()

    def atualizar_cargas(self):
        self.visualizar_cargas()
        i = int(input("Digite o número da carga que deseja atualizar: ")) - 1
        if 0 <= i < len(self.cargas):
            new_carga = input("Digite o novo nome da carga: ")
            self.cargas[i] = new_carga
            print("Carga atualizada com sucesso!")
        else:
            print("Localização inválida! Tente novamente")
        self.MenuCRUDPython()

    def apagar_cargas(self):
        self.visualizar_cargas()
        try:
            i = int(input("Digite o número da carga que deseja deletar: ")) - 1
            if 0 <= i < len(self.cargas):
                delete_carga = self.cargas.pop(i)
                print(f"A Carga '{delete_carga}' foi removida com sucesso!")
            else:
                print("Localização inválida! Tente novamente")
        except ValueError:
            print("Error! Insira uma seção válida.")
        self.MenuCRUDPython()

AllCargas = []
crud = CRUDPython(AllCargas)
crud.MenuCRUDPython()

        