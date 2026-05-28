"""Vinicius Lira Hansen"""
equipamento=[]
def cadastro_equipamento():
    while True:
        aparelho = input("Qual o aparelho? ")
        quantidade = int(input("Quantos você tem? "))
        tempo = input("Quanto tempo você usa os aparelhos? (ex: 2h, 5h, 2,5h) ")
        tempo_list = tempo.split(", ")
        tempo_total = 0
        for posicao in range(len(tempo_list)):
            tempo_posicao = tempo_list[posicao]
            tempo_certo = tempo_posicao.replace("h", "").replace(",", ".")
            tempo_total += float(tempo_certo)
        potencia = input("Qual a potência de cada aparelho? (ex: 300w, 100w) ")
        potencia_list= potencia.split(", ")
        potencia_total=0
        for posicao in range(len(potencia_list)):
            potencia_posicao = potencia_list[posicao]
            potencia_certo = potencia_posicao.replace("w", "").replace(",", ".")
            potencia_total += float(potencia_certo) 
        cadastro= {
            "Aparelho": aparelho,
            "Quantidade": quantidade,
            "Tempo usado": tempo_total,
            "Potência total gasta": potencia_total
        }
        equipamento.append(cadastro)
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
            s = 0
            if cadastrar=='S' or cadastrar=='s':
                cadastro_equipamento()
                break
            elif cadastrar=='N' or cadastrar=='n':
                break
            else:
                print("ERROR\nDigites as opções corretas")
    else:
        for i in equipamento:
            print(f"Aparelho: {i['Aparelho']}\nQuantidade: {i['Quantidade']}\nTempo usado total dos aparelhos: {i['Tempo usado']}\nPotência total dos aparelhos: {i['Potência total gasta']}")            print(f"Aparelho: {i['Aparelho']}\nQuantidade: {i['Quantidade']}\nTempo usado total dos aparelhos: {i['Tempo usado']}\nPotência total dos aparelhos: {i['Potência total gasta']}")
    return
