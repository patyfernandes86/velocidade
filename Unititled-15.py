
velocidade = float(input("Qual é a velocidade do carro em km/h? "))


if velocidade > 80:
   
    km_excedidos = velocidade - 80
    
    
    valor_multa = km_excedidos * 20
    
   
    print(f"Você foi multado! O valor da multa é R${valor_multa:.2f}.")
else:
   
    print("Parabéns, você está dentro do limite de velocidade!")