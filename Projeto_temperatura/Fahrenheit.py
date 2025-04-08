#-*- coding: UTF-8 -*-


print("Ola usuario, me de uma tempratura em Celsius e vou lhe retornar em Fahrenheit")
num1 = int(input("Digite um numero em temperatura em Celsius ou Fahrenheit: "))
temp= input("Digite C para converter celcius para fahrenheit e F para converter fahrenheit em calcius: ")
def contagem ():
    global temp, num1
    if temp == "C" or temp == "c":
        contaf = (num1 - 32) * 9/5
        print("A temperatura em Celsius é de", contaf)
    elif temp == "F":
            contc = 9 / 5 * num1 + 32
            print("A temperatura em Fahrenheit é de", contac)
contagem()
