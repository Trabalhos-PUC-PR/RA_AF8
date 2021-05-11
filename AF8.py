'''
1) Escreva um Algoritmo e um App em Python que leia três valores inteiros do 
teclado, chame uma função que receba o três valores (a, b, e c) como
parâmetros, sendo a maior que 1. A função deve somar todos nos inteiros entre 
b e c que sejam divisíveis por a (inclusive b e c), retorne o valor para o 
programa principal e imprima resultado. 

2) Escreva um Algoritmo e um App em Python que converta horas, minutos e 
segundos em segundos. A função recebe os valores das horas, minutos e 
segundos lidos do teclado no programa principal, envia os três valores para a 
função e retorna o total de segundos, que será impresso pelo programa
principal. 

3) Escreva um Algoritmo e um App em Python que converta segundos em horas, 
minutos e segundos. A função recebe o valor total de segundos, lidos do teclado
no programa principal, envia o valor para a função e retorna as horas, minutos e 
segundos equivalentes, que será impresso pelo programa principal.
'''
import numpy as np

escolha = int(input("Escolha a atividade (1-3): "))
if(escolha>3 or escolha<1):
    exit("Atividade não existente")
'''
--------------------------------------------- Exercício 1:
ALGORITMO
variaveis
a, b, c = 0
soma = 0

corpo do programa
    definir soma(a, b, c):
        se (a >= 1 e b >= 1 e c >= 1) faca
            para x no raio de b ate c+1 faca
                se( x mod a ) == 0 faca
                    soma = soma + x
            retorna soma
        senao:
            exit("Erro com os valores recebidos.")

    a = inteiro(leia("Digite um valor acima de 1: "))
    b = inteiro(leia("Digite outro valor acima de 1: "))
    c = inteiro(leia("Digite mais um valor acima de 1: "))

    print(soma(a,b,c))
    exit()
PROGRAMA 
'''
if(escolha==1):

    def ex1(a, b, c):
        soma = 0
        if(a >= 1 and b >= 1 and c >= 1):
            for x in range(b, c+1):
                if( ( x % a ) == 0):
                    soma += x
            return soma
        else:
            exit("Erro com os valores recebidos.")

    numeroum = int(input("Digite um valor acima de 1: "))
    numerodois = int(input("Digite outro valor acima de 1: "))
    numerotres = int(input("Digite mais um valor acima de 1: "))

    print("A soma dos valores entre",numerodois,"e",numerotres,"que são divisiveis por",numeroum,"é: ",ex1(numeroum,numerodois,numerotres))
    exit()
'''
--------------------------------------------- Exercício 2:
ALGORITMO
variaveis
s, m, h = 0

corpo do programa
PROGRAMA 
    definir tudoSegundos(s, m, h):
        h = (60 * h)
        m = 60 * (m+h)
        retorna s + m

    segundos = inteiro(leia("Digite um valor de segundos: "))
    minutos = inteiro(leia("Digite um valor de minutos: "))
    horas = inteiro(leia("Digite um valor de horas: "))

    print(tudoSegundos(segundos, minutos, horas))
    exit()
'''
if(escolha==2):

    def tudoSegundos(s, m, h):
        h = (60 * h)
        m = 60 * (m+h)
        return s + m

    segundos = int(input("Digite um valor de segundos: "))
    minutos = int(input("Digite um valor de minutos: "))
    horas = int(input("Digite um valor de horas: "))

    print("O total de segundos dentro dos valores fornecidos é de :", tudoSegundos(segundos, minutos, horas))
    exit()
'''
--------------------------------------------- Exercício 3:
ALGORITMO
variaveis
s, m, h = 0

corpo do programa
    definir tudoOrganizado(s):
        m = arredondar(s / 60)
        s = arredondar(s mod 60)
        h = arredondar(m / 60)
        m = arredondar(m mod 60)

        retornar s, m, h

    segundos = inteiro(leia("Digite um valor de segundos (pode ser absurdamente alto): "))

    print(tudoOrganizado(segundos))
    exit()

PROGRAMA 
'''
if(escolha==3):

    def tudoOrganizado(s):
        m = round(s / 60)
        s = round(s % 60)
        h = round(m / 60)
        m = round(m % 60)

        return s, m, h

    segundos = int(input("Digite um valor de segundos (pode ser absurdamente alto): "))

    print("O total de segundos, minutos e horas dentro dos valor fornecido são, respectivamente :", tudoOrganizado(segundos))
    exit()