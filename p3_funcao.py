

def verificar_voto(idade):
    if (idade >= 16 and idade < 18) or (idade > 70):
        v = 'Voto facultativo'
    elif (idade <=70):
        v =  'Voto obrigatorio'
    else:
        v =  'Voto proibido'
    return v

idade = float(input('Digite sua idade: '))    
voto = verificar_voto(idade)   

print (voto)
 
  