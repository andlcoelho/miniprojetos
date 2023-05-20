print("Bem vindos ao meu quiz para computador")

jogando = input("Gostaria de iniciar o jogo?: ")

if jogando != "sim":
    quit()

print("OK então, vamos brincar :)")

pontuacao = 0

pergunta = input("Qual o significado de CPU?: ")
if pergunta == "unidade de processamento central":
    print("Acertou, mizeravi!")
    pontuacao += 1
else:
    print("Errou, ja era!")

pergunta = input("Qual o significado de GPU?: ")
if pergunta == "unidade de processamento gráfico":
    print("Acertou, mizeravi!")
    pontuacao += 1
else:
    print("Errou, ja era!")

pergunta = input("Qual o significado de CPD?: ")
if pergunta == "central de Processamento de Dados":
    print("Acertou, mizeravi!")
    pontuacao += 1
else:
    print("Errou, ja era!")

pergunta = input("Qual o significado de RAM?: ")
if pergunta == "random access memory":
    print("Acertou, mizeravi!")
    pontuacao += 1
else:
    print("Errou, ja era!")

print("Você acertou " + str(pontuacao) + " perguntas!")