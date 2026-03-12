###Atividade 6
A = float(input("Digite a nota da primeira prova: "))
B = float(input("Digite a nota da segunda prova: "))
C = float(input("Digite a nota da terceira prova: "))

media = (A + B + C) / 3

if media >= 6:
    print("Aprovado!")
    if media > 9:
        print("O aluno foi conceito A")
    elif media > 7.5:
        print("O aluno foi conceito B")
    elif media > 6:
        print("O aluno foi conceito C")
    else:
        print("O aluno foi conceito D")
else:
    print("Reprovado!")
    if media > 4.5:
        print("O aluno foi conceito D")
    else:
        print("O aluno foi conceito E")