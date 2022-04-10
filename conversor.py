#Conversão de medida
print("\t ----Conversão de medida----")

opçao = int(input("Digite 1 para converter Metros para centimetros: \nOu 2 para converter Centimetros para metros: "))

if opçao == 1:
    metros = int(input("Digite o valor em metros: "))
    print("O valor de {} metros, em centimetros é:".format(metros), metros*100)

elif opçao == 2:
    centimetros = int(input("Digite o valor em Centimetros: "))
    print("O valor de {} centimetros, em metros é de:".format(centimetros), centimetros/100)

else:
    print("Valor não identificado! ")
