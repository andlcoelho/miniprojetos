#Apresentação do programa
print("Bem vindos ao meu quiz para computador")

#primeira interação com o usuário
jogando = input("Gostaria de iniciar o jogo?: ")

#checa a resposta do usuário, se quer iniciar o quiz ou não
if jogando.lower() != "sim":
    quit()

print("OK então, vamos brincar :)")

#variável que vai receber a contagem de acertos
pontuacao = 0

#inicio das perguntas, interagindo com o usuário fazendo-o responder via terminal
pergunta = input("Qual o significado de CPU?: ")
if pergunta.lower() == "unidade de processamento central":
    print("Acertou, mizeravi!")
    pontuacao += 1
else:
    print("Errou, ja era!")

pergunta = input("Qual o significado de GPU?: ")
if pergunta.lower() == "unidade de processamento gráfico":
    print("Acertou, mizeravi!")
    pontuacao += 1
else:
    print("Errou, ja era!")

pergunta = input("Qual o significado de CPD?: ")
if pergunta.lower() == "central de processamento de Dados":
    print("Acertou, mizeravi!")
    pontuacao += 1
else:
    print("Errou, ja era!")

pergunta = input("Qual o significado de RAM?: ")
if pergunta.lower() == "random access memory":
    print("Acertou, mizeravi!")
    pontuacao += 1
else:
    print("Errou, ja era!")

print("Você acertou " + str(pontuacao) + " perguntas!")
print("Seu quiz teve uma eficácia de " + str((pontuacao / 4) * 100) + "%.")