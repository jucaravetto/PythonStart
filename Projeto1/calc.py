print("Olá, vamos calcular!")

number1 = float(input("Primeiro número: "))
number2 = float(input("Segundo número: "))

soma=number1+number2
print("\nA soma é: ", soma)

subtracao1=number1-number2
print("\nA subtração número 1 - número 2 é: ", subtracao1)

mult=number1*number2
print("\nA multiplicação é: ", mult)

#Fazer correção em caso de divisão por zero - avisar o usuário
if number2 == 0:
  print("\nO segundo número é 0, não se pode realizar a divisão")
  number2 = float(input("\nDigite outro valor para o segundo número: "))

div1=number1/number2
print("\nA divisão número 1 / número 2 é: ", div1)

#fazer opções para seleção da operação matemática
