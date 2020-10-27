import random
print("*********************************")
print("Bem vindo ao treinamento de tabuada!")
print("*********************************")

numeros_lista_normal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #Números da tabuada que serão utilizados para criar a lista da tabuada do 1 até o 10
lista_normal = [] #Lista do modo normal de utilização

#Os contadores que irão aparecer a seguir foram usados para possibilitar a criação das listas do "Modo Normal" e do "Modo Reduzido"

for item in numeros_lista_normal: #Aqui está sendo criado uma lista com as multiplicações e os resultados respectivos
    contador = 1
    while(contador <= 10):
        multiplicacao = "{} X {} = ".format(contador, item)
        resultado = contador * item
        tupla_valores = (multiplicacao, resultado) #Aqui está sendo criado uma tupla, em que o primeiro valor é a multiplicação e o segundo é o resultado
        lista_normal.append (tupla_valores) #Aqui está adicionando a tupla anterior na lista normal
        contador = contador + 1

numeros_lista_reduzida = [3, 4, 5, 6, 7, 8, 9] #Números da tabuada que serão utilizados para criar a lista da tabuada reduzida
lista_reduzida = [] #Lista do modo reduzido de utilização
contador3 = 3 #Começa com o 3 porque a lista reduzida começa pela tabuada do 3
for item in numeros_lista_reduzida:
    contador2 = contador3
    while(contador2 <= 9):
        multiplicacao = "{} X {} = ".format(contador2, item)
        resultado = contador2 * item
        tupla_valores = (multiplicacao, resultado) #Aqui está sendo criado uma tupla, em que o primeiro valor é a multiplicação e o segundo é o resultado
        lista_reduzida.append (tupla_valores) #Aqui está adicionando a tupla anterior na lista reduzida
        contador2 = contador2 + 1
    contador3 = contador3 + 1

acertos = 0 #Váriavel que irá marcar os acertos do usuário
erros = 0 #Váriavel que irá marcar os erros do usuário

print("Qual o modo de utilização?")
print("(1) Normal (2) Reduzido")

modo = int(input("Defina o modo de utilização: ")) #Aqui o usuário definirá o modo de utilização

print("Qual a ordem de utilização?")
print("(1) Sequência (2) Aleatória")

ordem = int(input("Defina a ordem de utilização: ")) #Aqui o usuário definirá a ordem de utilização

if (modo == 1 and ordem == 1): #Aqui está programado o que o sistema fará caso o usuário escolha o modo normal e a ordem sequencial
    for item in lista_normal:
        conta = item [0] #A váriavel "conta" está representando o primeiro valor da tupla de cada item da lista normal
        solucao = item [1] #A váriavel "solucao" está representando o segundo valor da tupla de cada item da lista normal
        resposta_str = input(conta) #Aqui o usuário irá digitar a resposta da conta
        print("Você digitou " , resposta_str) #Aqui é mostrada a resposta do usuário
        resposta = int(resposta_str) #Aqui a resposta do usuário é convertida para inteiro
        if resposta == solucao: #Caso a resposta for correta, o sistema mostrará que o usuário acertou
            print("Você acertou")
            acertos += 1 #Aqui é adicionado mais 1 acerto para a variável "acertos"
        else:
            print("Você errou") #Caso a resposta for errada, o sistema mostrará que o usuário errou
            erros += 1 #Aqui é adicionado mais 1 erro para a variável "erros"
    print("Acertos: ", acertos, "Erros: ", erros) #É mostrado ao usuário a quantidade de acertos e de erros cometidos

elif (modo == 1 and ordem == 2): #Aqui está programado o que o sistema fará caso o usuário escolha o modo normal e a ordem aleatória
    random.shuffle(lista_normal) #Aqui os itens da lista normal estão sendo embaralhados para ficar em ordem aleatória
    for item in lista_normal:
        conta = item [0] #A váriavel "conta" está representando o primeiro valor da tupla de cada item da lista normal
        solucao = item [1] #A váriavel "solucao" está representando o segundo valor da tupla de cada item da lista normal
        resposta_str = input(conta) #Aqui o usuário irá digitar a resposta da conta
        print("Você digitou " , resposta_str) #Aqui é mostrada a resposta do usuário
        resposta = int(resposta_str) #Aqui a resposta do usuário é convertida para inteiro
        if resposta == solucao: #Caso a resposta for correta, o sistema mostrará que o usuário acertou
            print("Você acertou")
            acertos += 1 #Aqui é adicionado mais 1 acerto para a variável "acertos"
        else:
            print("Você errou") #Caso a resposta for errada, o sistema mostrará que o usuário errou
            erros += 1 #Aqui é adicionado mais 1 erro para a variável "erros"
    print("Acertos: ", acertos, "Erros: ", erros) #É mostrado ao usuário a quantidade de acertos e de erros cometidos

elif (modo == 2 and ordem == 1): #Aqui está programado o que o sistema fará caso o usuário escolha o modo reduzido e a ordem sequencial
    for item in lista_reduzida:
        conta = item [0] #A váriavel "conta" está representando o primeiro valor da tupla de cada item da lista reduzida
        solucao = item [1] #A váriavel "solucao" está representando o segundo valor da tupla de cada item da lista reduzida
        resposta_str = input(conta) #Aqui o usuário irá digitar a resposta da conta
        print("Você digitou " , resposta_str) #Aqui é mostrada a resposta do usuário
        resposta = int(resposta_str) #Aqui a resposta do usuário é convertida para inteiro
        if resposta == solucao: #Caso a resposta for correta, o sistema mostrará que o usuário acertou
            print("Você acertou")
            acertos += 1 #Aqui é adicionado mais 1 acerto para a variável "acertos"
        else:
            print("Você errou") #Caso a resposta for errada, o sistema mostrará que o usuário errou
            erros += 1 #Aqui é adicionado mais 1 erro para a variável "erros"
    print("Acertos: ", acertos, "Erros: ", erros) #É mostrado ao usuário a quantidade de acertos e de erros cometidos


elif (modo == 2 and ordem == 2): #Aqui está programado o que o sistema fará caso o usuário escolha o modo reduzido e a ordem aleatória
    random.shuffle(lista_reduzida) #Aqui os itens da lista reduzida estão sendo embaralhados para ficar em ordem aleatória
    for item in lista_reduzida:
        conta = item [0] #A váriavel "conta" está representando o primeiro valor da tupla de cada item da lista reduzida
        solucao = item [1] #A váriavel "solucao" está representando o segundo valor da tupla de cada item da lista reduzida
        resposta_str = input(conta) #Aqui o usuário irá digitar a resposta da conta
        print("Você digitou " , resposta_str) #Aqui é mostrada a resposta do usuário
        resposta = int(resposta_str) #Aqui a resposta do usuário é convertida para inteiro
        if resposta == solucao: #Caso a resposta for correta, o sistema mostrará que o usuário acertou
            print("Você acertou")
            acertos += 1 #Aqui é adicionado mais 1 acerto para a variável "acertos"
        else:
            print("Você errou") #Caso a resposta for errada, o sistema mostrará que o usuário errou
            erros += 1 #Aqui é adicionado mais 1 erro para a variável "erros"
    print("Acertos: ", acertos, "Erros: ", erros) #É mostrado ao usuário a quantidade de acertos e de erros cometidos