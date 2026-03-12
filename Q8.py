###Atividade 8
valor = int(input("Valor: "))

print("Só é aceito 'Cheque' ou 'Dinheiro' ou 'Cartão'!")

forma = input("Forma Pagamento: ")

if forma == "Dinheiro" and valor >= 100:
    valor *= 0.9
    print(f"R$ {valor:.2f}")
elif forma == "Cartão":
    print("São aceitos: 'Débito' ou 'Crédito'")
    funcao = input("Função: ")

    if funcao == "Crédito":
        print("São aceitos até 3 parcelas")
        parcela = int(input("Parcelas: "))
        if  parcela <= 3:
            valor_parcelado = valor/parcela
            print(f"R$ {valor:.2f}")
            print(f"{parcela} parcelas de {valor_parcelado:.2f}")
        else:
            print("Parcela inválida!")
    else:
        print(f"R$ {valor:.2f}")    
else:
    print(f"R$ {valor:.2f}")