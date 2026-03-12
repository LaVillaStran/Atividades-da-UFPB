###Atividade 5
a = int(input("Digite o valor do primeiro lado: "))
b = int(input("Digite o valor do segundo lado: "))
c = int(input("Digite o valor do terceiro lado: "))

if a == b and b == c and c == a:
    print("Esse triângulo é Equilátero!")
elif a == b or b == c or c == a:
    print("Esse triângulo é Isósceles")
else:
    print("Esse triângulo é Escaleno")