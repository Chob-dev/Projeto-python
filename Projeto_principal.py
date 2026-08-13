equipamento=[]
def cadastro_equipamento():
    while True:
        aparelho = input("Qual o aparelho? ")
        quantidade = int(input("Quantos você tem? "))
        tempo = input("Quanto tempo você usa cada aparelho? (em horas) (ex: 2h, 5h, 2,5h) ")
        tempo_list = tempo.split(", ")
        tempo_total = 0
        for posicao in range(len(tempo_list)):
            tempo_posicao = tempo_list[posicao]
            tempo_certo = tempo_posicao.replace("h", "").replace(",", ".")
            tempo_total += float(tempo_certo)
        potencia = input("Qual a potência de cada aparelho (em whatts)? (ex: 300w, 100w) ")
        potencia_list= potencia.split(", ")
        potencia_total=0
        for posicao in range(len(potencia_list)):
            potencia_posicao = potencia_list[posicao]
            potencia_certo = potencia_posicao.replace("w", "").replace(",", ".").replace("w", "")
            potencia_total += float(potencia_certo) 
        cadastro= {
            "Aparelho": aparelho,
            "Quantidade": quantidade,
            "Tempo usado": tempo_total,
            "Potência total gasta": potencia_total
        }
        equipamento.append(cadastro)
        with open("Relatório.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"CADASTRO:\nAparelho: {aparelho}:\nQuantidade: {quantidade}\nPOtência total gasta: {potencia_total}\n")
        print(f"Cadastro do {aparelho} feito!")
        n = 0
        while True:
            parar = input("Deseja cadastrar outro aparelho? S/N: ")
            if parar=='N' or parar=='n':
                n+=1
                break
            elif parar=='S' or parar=='s':
                break
            else:
                print("ERRROR\nDigite as opções corretas")
        if n==1:
            break
    return
def list_equipamento():
    if len(equipamento)==0:
        print("Não existe aparelho cadastrado:")
        while True:
            cadastrar = input("Deseja iniciar o cadastro? S/N:")
            if cadastrar=='S' or cadastrar=='s':
                cadastro_equipamento()
                for i in equipamento:
                    print(f"Aparelho: {i['Aparelho']}\nQuantidade: {i['Quantidade']}\nTempo usado total dos aparelhos: {i['Tempo usado']}h\nPotência total dos aparelhos: {i['Potência total gasta']:.2f}Wh") 
                break
            elif cadastrar=='N' or cadastrar=='n':
                print("Então não tenho utilidade\nAdeus!")
                return
            else:
                print("ERROR\nDigite as opções corretas")
    else:
        for i in equipamento:
            print(f"Aparelho: {i['Aparelho']}\nQuantidade: {i['Quantidade']}\nTempo usado total dos aparelhos: {i['Tempo usado']}h\nPotência total dos aparelhos: {i['Potência total gasta']:.2f}Wh")
    while True:
        excluir = input("Deseja excluir algum equipamento? S/N")
        if excluir == 's' or excluir == 'S':
            for index, i in enumerate(equipamento):
                print(f"{index+1} Aparelho: {i['Aparelho']}")
            escolha = int(input("Escolha:"))
            if 1 <= escolha <= len(equipamento):
                removido = equipamento.pop(escolha-1)
                print(f"O aparelho {removido['Aparelho']} foi removido da lista de equipamentos")
                with open("Relatório.txt", "a", encoding="utf-8") as arquivo:
                    arquivo.write(f"O aparelho {removido['Aparelho']} foi removido da lista de equipamentos\n")
                    break
        elif excluir == 'n' or excluir == 'N':
            print("Então nenhum arquivo será excluido")
            return
        else:
            print("ERROR\nDigite as opções corretas")
    return
def consumo():
    if len(equipamento)==0:
        print("Não existe aparelho cadastrado:")
        while True:
            cadastrar = input("Deseja iniciar o cadastro? S/N:")
            if cadastrar=='S' or cadastrar=='s':
                cadastro_equipamento()
                consumototal = 0
                for i in equipamento:
                    consumoparcial = (i['Potência total gasta']*i['Tempo usado']*30)/1000
                    consumototal += consumoparcial
                print(f"Seu consumo previsto para esse mês será de: {consumototal}kWh")
                break
            elif cadastrar=='N' or cadastrar=='n':
                print("Então não tenho utilidade\nAdeus!")
                return
            else:
                print("ERROR\nDigites as opções corretas")
    else:
        consumototal = 0
        for i in equipamento:
            consumoparcial = (i['Potência total gasta']*i['Tempo usado']*30)/1000
            consumototal += consumoparcial
        print(f"Seu consumo previsto para esse mês será de: {consumototal}kWh")
    with open("Relatório.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"O consumo total é: {consumototal}kWh\n")
    return
def disjuntor():
    if len(equipamento)==0:
            print("Não existe aparelho cadastrado:")
            while True:
                cadastrar = input("Deseja iniciar o cadastro? S/N:")
                if cadastrar=='S' or cadastrar=='s':
                    cadastro_equipamento()
                    corrente = 0
                    while True:
                        tensao = input("Qual a tensão da sua casa? 127V ou 220V?")
                        if tensao =='127V' or tensao == '127v' or tensao =='127':
                            potenciamax = 0
                            for i in equipamento:
                                potenciamax += i['Potência total gasta']
                            corrente = potenciamax/127
                            break
                        elif tensao == '220V' or tensao == '220v' or tensao == '220':
                            potenciamax = 0
                            for i in equipamento:
                                potenciamax += i['Potência total gasta']
                            corrente = potenciamax/220
                            break
                        else:
                            print("Não exite esse no Brasil.\nTente novamente:")
                    if corrente<10:
                        print(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 10A.")
                        with open("Relatório.txt", "a", encoding="utf-8") as arquivo:
                            arquivo.write(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 10A.\n")
                    elif corrente == 10 or corrente<16:
                        print(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 16A.")
                        with open("Relatório.txt", "a", encoding="utf-8") as arquivo:
                            arquivo.write(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 16A.\n")
                    elif corrente == 16 or corrente<20:
                        print(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 20A.")
                        with open("Relatório.txt", "a", encoding="utf-8") as arquivo:
                            arquivo.write(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 20A.\n")
                    elif corrente == 20 or corrente<25:
                        print(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 25A.")
                        with open("Relatório.txt", "a", encoding="utf-8") as arquivo:
                            arquivo.write(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 25A.\n")
                    elif corrente == 25 or corrente<32:
                        print(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 32A.")
                        with open("Relatório.txt", "a", encoding="utf-8") as arquivo:
                            arquivo.write(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 32A.\n")
                    elif corrente == 32 or corrente<40:
                        print(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 40A.")
                        with open("Relatório.txt", "a", encoding="utf-8") as arquivo:
                            arquivo.write(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 40A.\n")
                    elif corrente == 40 or corrente<50:
                        print(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 50A.")
                        with open("Relatório.txt", "a", encoding="utf-8") as arquivo:
                            arquivo.write(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 50A.\n")
                    elif corrente == 50 or corrente<63:
                        print(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 63A.")
                        with open("Relatório.txt", "a", encoding="utf-8") as arquivo:
                            arquivo.write(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 63A.\n")
                    elif corrente>=63:
                        print(f"ALERTA!! Com conrrente de {corrente:.2f}A, recomenda-se sistema bifásico ou trifásico!\nSolicitar com sua distribuidora de energia.")
                        with open("Relatório.txt", "a", encoding="utf-8") as arquivo:
                            arquivo.write(f"ALERTA!! Com conrrente de {corrente:.2f}A, recomenda-se sistema bifásico ou trifásico!\nSolicitar com sua distribuidora de energia.\n")
                    break
                elif cadastrar=='N' or cadastrar=='n':
                    print("Então não tenho utilidade\nAdeus!")
                    return
                else:
                    print("ERROR\nDigites as opções corretas")
    else:
        corrente = 0
        while True:
            tensao = input("Qual a tensão da sua casa? 127V ou 220V?")
            if tensao =='127V' or tensao == '127v' or tensao =='127':
                potenciamax = 0
                for i in equipamento:
                    potenciamax += i['Potência total gasta']
                corrente = potenciamax/127
                break
            elif tensao == '220V' or tensao == '220v' or tensao == '220':
                potenciamax = 0
                for i in equipamento:
                    potenciamax += i['Potência total gasta']
                corrente = potenciamax/220
                break
            else:
                print("Não exite esse no Brasil.\nTente novamente:")
        if corrente<10:
            print(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 10A.")
            with open("Relatório.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 10A.\n")
        elif corrente == 10 or corrente<16:
            print(f"Com corrente de {corrente:2f}A, recomenda-se para sua residência um disjuntor de 16A.")
            with open("Relatório.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 16A.\n")
        elif corrente == 16 or corrente<20:
            print(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 20A.")
            with open("Relatório.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 20A.\n")
        elif corrente == 20 or corrente<25:
            print(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 25A.")
            with open("Relatório.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 25A.\n")
        elif corrente == 25 or corrente<32:
            print(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 32A.")
            with open("Relatório.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"Com corrente de {corrente:2f}A, recomenda-se para sua residência um disjuntor de 32A.\n")
        elif corrente == 32 or corrente<40:
            print(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 40A.")
            with open("Relatório.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"Com corrente de {corrente:2f}A, recomenda-se para sua residência um disjuntor de 40A.\n")
        elif corrente == 40 or corrente<50:
            print(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 50A.")
            with open("Relatório.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 50A.\n")
        elif corrente == 50 or corrente<63:
            print(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 63A.")
            with open("Relatório.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"Com corrente de {corrente:.2f}A, recomenda-se para sua residência um disjuntor de 63A.\n")
        elif corrente>=63:
            print(f"ALERTA!! Com conrrente de {corrente:.2f}A, recomenda-se sistema bifásico ou trifásico!\nSolicitar com sua distribuidora de energia.")
            with open("Relatório.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"ALERTA!! Com conrrente de {corrente:.2f}A, recomenda-se sistema bifásico ou trifásico!\nSolicitar com sua distribuidora de energia.\n")
    return
def contaluz():
    if len(equipamento)==0:
        print("Não existe aparelho cadastrado:")
        while True:
            cadastrar = input("Deseja iniciar o cadastro? S/N:")
            if cadastrar=='S' or cadastrar=='s':
                cadastro_equipamento()
                conta = input("Quantos reais é por kWh da sua distribuidora? (ex: R$ 0,95)")
                contac = float(conta.replace(",", ".").replace("R$", ""))
                consumototal = 0
                for i in equipamento:
                    consumoparcial = (i['Potência total gasta']*i['Tempo usado']*30)/1000
                    consumototal += consumoparcial
                contab = contac * consumototal
                contaf = consumototal / 100
                print(f"Se for bandeira verde🟩: R$ {contab:.2f}.")
                print(f"Se for bandeira amarela🟨: R$ {(contab + (contaf * 1.88)):.2f}.")
                print(f"Se for bandeira vermelha🟥: R$ {(contab + (contaf * 4.46)):.2f}.")
                print(f"Se a bandeira for vermelha2🟥🟥: R$ {(contab + (contaf * 7.87)):.2f}.")
                break
            elif cadastrar=='N' or cadastrar=='n':
                print("Então não tenho utilidade\nAdeus!")
                return
            else:
                print("ERROR\nDigites as opções corretas")
    else:
        conta = input("Quantos reais é por kWh da sua distribuidora? (ex: R$ 0,95)")
        contac = float(conta.replace(",", ".").replace("R$", ""))
        consumototal = 0
        for i in equipamento:
            consumoparcial = (i['Potência total gasta']*i['Tempo usado']*30)/1000
            consumototal += consumoparcial
        contab = contac * consumototal
        contaf = consumototal / 100
        print(f"Se for bandeira verde🟩: R$ {contab:.2f}.")
        print(f"Se for bandeira amarela🟨: R$ {(contab + (contaf * 1.88)):.2f}.")
        print(f"Se for bandeira vermelha🟥: R$ {(contab + (contaf * 4.46)):.2f}.")
        print(f"Se a bandeira for vermelha2🟥🟥: R$ {(contab + (contaf * 7.87)):.2f}.")
    with open("Relatório.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Se for bandeira verde🟩: R$ {contab:.2f}.\n")
        arquivo.write(f"Se for bandeira amarela🟨: R$ {(contab + (contaf * 1.88)):.2f}.\n")
        arquivo.write(f"Se for bandeira vermelha🟥: R$ {(contab + (contaf * 4.46)):.2f}.\n")
        arquivo.write(f"Se a bandeira for vermelha2🟥🟥: R$ {(contab + (contaf * 7.87)):.2f}.\n")
    return
while True:
        print("--- MENU ELETROSAFE ---")
        print("1 - Cadastrar equipamento")
        print("2 - Listar equipamentos ou remover aparelho de equipamentos")
        print("3 - Calcular consumo")
        print("4 - Analisar disjuntor")
        print("5 - Simular conta de luz")
        print("0 - Sair")
        opcao = input("Escolha: ")
        
        if opcao == '1':
            cadastro_equipamento()
        elif opcao == '2':
            list_equipamento()
        elif opcao == '3':
            consumo()
        elif opcao == '4':
            disjuntor()
        elif opcao == '5':
            contaluz()
        elif opcao == '0':
            print("Encerrando o sistema Eletrosafe... Até logo!")
            break
        else:
            print("Opção inválida. Digite o número correto")