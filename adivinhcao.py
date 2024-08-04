import random

print("x" * 50)
print("          Bem vindo ao jogo de advinhação")
print("x" * 50)

numero_secreto = round(random.randrange(1,101))
total_de_tentativas = 0

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))
if (nivel == 1):
      total_de_tentativas = 20
elif( nivel == 2):
      total_de_tentativas = 5
else:
      total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
      print("Tentativa {} de {}".format(rodada, total_de_tentativas))
      chute = int(input("Digite um número entre 0 e 100: "))
      print("Você digitou ", chute)

      if chute < 1 or chute > 100:
          print("Você deve digitar um número entre 1 e 100!")

      acertou = chute == numero_secreto
      maior   = chute > numero_secreto
      menor   = chute < numero_secreto

      if acertou:
              print("Você acertou!")
              break
      else:
              if(maior):
                  print("Você erro! O seu chute foi maior que o número secreto.")
              elif(menor):
                  print("Você errou! O seu chute foi menor do que o número secreto")





print("Fim do jogo")