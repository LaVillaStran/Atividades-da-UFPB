def verificador_cpf(soma):
    resto = soma % 11
    if resto < 2:
        return 0
    return 11 - resto

def cadastro_Pessoal (f1):
    lista_termo = []
    d10 = 0
    d11 = 0
    for i in f1:
        if i == "." or i == "-":
            continue
        else: lista_termo.append(int(i))
    
    for i in range(9,0,-1):
        d10 += (lista_termo[9 - i] * (i + 1))
    d10 = verificador_cpf(d10)
    
    for i in range(9,0,-1):
        d11 += (lista_termo[10 - i] * (i + 1))
    d11 = verificador_cpf(d11)

    if d10 == lista_termo[-2] and d11 == lista_termo[-1]:
        return "CPF válido"
    else:
        return "CPF inválido"

def main():
    print("(Deve ser CPF no formato: xxx.xxx.xxx-xx)")
    cpf = input("Digite um CPF: ")

    print(cadastro_Pessoal(cpf))

if __name__ == "__main__":
    main()