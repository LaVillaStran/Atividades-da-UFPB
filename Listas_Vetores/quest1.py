vetor1 = []
for i in range(5):
    vetor1.append(int(input("Digite os valor do vetor 1: ")))
vetor2 = []
for i in range(5):
    vetor2.append(int(input("Digite os valor do vetor 2: ")))
vetor3 = []

for i in range(5):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

print(vetor3)