nome = (input("Qual seu nome: "))
ano_nasc = int(input("qual sua data de nascimento: "))

alistar = 2025 - ano_nasc



if alistar < 18:
    falta = 18 - alistar
    print (f"{nome}, ainda falta(m) {falta} ano(s) para o seu alistamento. ")
elif alistar == 18:
    
    print ("[Nome], voce precisa se alistar IMEDIATAMENTE")

else:
    passou = alistar - 18
    print (f"{nome}, voce deveria ter se alistado ha {passou} ano(s)")
