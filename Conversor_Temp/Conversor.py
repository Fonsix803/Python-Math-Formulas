import math

def convertTemp():
    tempC = float(input("insira a temperatura em Celsius:"))
    tempC = 9/5 * tempC + 32  # Formula de Conversão
    print(tempC, "Fahrenheit")


def IMC():
    peso = float(input("O teu peso é:"))
    altura = float(input("A tua altura é:"))
    indiceMC = peso/(altura ** 2)  # Formula para calcular o IMC
    print("O teu IMC é ", indiceMC)


def volumeCone():
    r = float(input("Insere o raio "))
    h = float(input("insere a altura "))
    volume = (math.pi * (r ** 2) * h) / 3  # Formula para calcular volume de um cone
    print("O volume do cone é:", volume)

def calcPolinomio(x):
    pol = (x ** 4) + (x ** 3) + (2 * x ** 2) - x  # Formula para calcular polinomio de um numero
    print("o valor do polinomio", x, "é", pol)

calcPolinomio(1.1)
calcPolinomio(5)
calcPolinomio(3/2)