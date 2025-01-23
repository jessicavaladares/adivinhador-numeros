import random
print("Bem-vindo ao Jogo do Adivinhador de Números!")
print("Tente adivinhar o número que estou pensando entre 1 e 100.")  

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    chute = int(input("Qual o seu chute? (entre 1 e 100) "))
    tentativas += 1
    if chute > numero_secreto:
        print("Seu chute é MAIOR que o número secreto!")
    elif chute < numero_secreto:
        print("Seu chute é MENOR que o número secreto!")
    else:
        print(f"ACERTOOOOU!!! Você precisou de {tentativas} tentativas!")
        break