print("Bem vindos ao meu quiz para computador")

jogando = input("Gostaria de iniciar o jogo?: ")

if jogando != "sim":
    quit()

print("OK então, vamos brincar :)")

pergunta = input("Qual o significado de CPU?: ")
if pergunta == "Unidade de processamento central":
    print("Acertou, mizeravi!")
else:
    print("Errou, ja era!")