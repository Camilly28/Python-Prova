palavra = str(input())
caracter_troca = [str(i) for i in input().split()]
substituto = [str(i) for i in input().split()]

for i in range (len(caracter_troca)):
  palavra = palavra.replace(caracter_troca[i],substituto[i])
    
print(palavra) 
