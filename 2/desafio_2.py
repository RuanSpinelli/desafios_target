

numero1, numero2 = 0, 1  #Declarando o primeiro e segundo termo da sequência
contador = 0 #Declarando o contador
lista_numeros = [] #Declarando a lista aonde os números ficarão quardados



#declarando uma variável que recebe um número inteiro do usuário
numero_user = int(input("Digite o número de termos que deseja na sequência de Fibonacci: "))

#Um laço de repetição para gerar a sequência de fibonacci.

"""
O + 100 está ali para evitar um erro de lógica. quando se digitar o número 2, mesmo ele existindo na sequência, 
o programa consta como se ele não existisse, pois o número é tão baixo que não dá pro laço de repetição gera-lo.
E com isso, ele gera 1 termo a mais apenas para conseguir detectar o 2

"""
while contador < numero_user + 100: 

    #caso deseje visualizar a sequência, basta tirar o comentário da linha abaixo
    print(f"{numero1} ",end="")        
    proximo_numero = numero1 + numero2
    numero1 = numero2
    numero2 = proximo_numero

    lista_numeros.append(numero1)

    contador += 1


#IF e ELSE para determinar o fluxo de decisão do software

if numero_user in lista_numeros:
    print("\nO número informado pertence a sequência fibonacci.\n")
else:
    print("\nO número informado não pertence a sequência fibonacci.\n")


