print("Bem vindos ao meu quiz para computador")

jogando = input("Gostaria de iniciar o jogo?: ")

if jogando.lower() != "Sim":
    quit()

print("OK então, vamos brincar :)")

pontuacao = 0

pergunta = input("Qual o significado de CPU?: ")
if pergunta.lower() == "Unidade de processamento central":
    print("Acertou, mizeravi!")
    pontuacao += 1
else:
    print("Errou, ja era!")

pergunta = input("Qual o significado de GPU?: ")
if pergunta.lower() == "Unidade de processamento gráfico":
    print("Acertou, mizeravi!")
    pontuacao += 1
else:
    print("Errou, ja era!")

pergunta = input("Qual o significado de CPD?: ")
if pergunta.lower() == "Central de Processamento de Dados":
    print("Acertou, mizeravi!")
    pontuacao += 1
else:
    print("Errou, ja era!")

pergunta = input("Qual o significado de RAM?: ")
if pergunta.lower() == "Random access memory":
    print("Acertou, mizeravi!")
    pontuacao += 1
else:
    print("Errou, ja era!")

print("Você acertou " + str(pontuacao) + " perguntas!")