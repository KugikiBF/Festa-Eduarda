class Convidado:
    lista_convidados=[]
    def __init__(self):
        self.nome=None
        self.quantidade=1


    def cadastrar_convidado(self):
        # nome e sobrenome do convidado
        nome_convidado=str (input("Nome e sobrenome: ")).capitalize().strip()
        self.nome=nome_convidado
        print (f"Olá {nome_convidado}, quero te convidar para minha festa!")
        resposta=''
        while resposta != "SIM" and resposta != "NAO":
            resposta=str(input("Voce confirma sua presença? [Sim/Nao]: ")).upper().strip()
        # quantidade de pessoas que irão
        if resposta == "SIM":
            self.confirmado=True
            try:
                self.quantidade_convidado=int(input(f'Gostaria de saber quantas pessoas no total da sua familia (incluindo voce {self.nome}) irão comparecer: '))
            except ValueError:
                print ("Somente número por favor!")
            print(f"Ótimo, então estão todos convidados espero voce {self.nome} e mais os seus {self.quantidade_convidado-1} familiares")
        else:
            self.confirmado=False
            print("É uma pena!")
        

    def convite_finalizado(self):
        status=self.confirmado
        if status==True:
            status='Confirmado ✅'
            resumo={'Nome':self.nome,
                    "Acompanhantes":self.quantidade_convidado-1,
                    "Status": status}
        else:
            status='Não virá ❌'
            resumo={'Nome':self.nome,
                    "Status": status}
    
        Convidado.lista_convidados.append(resumo)
        print("\n--- LISTA ATUALIZADA ---")
        print(Convidado.lista_convidados)
        print()
        


