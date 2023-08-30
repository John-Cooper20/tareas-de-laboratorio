#Inversión de palabras en una frase: Dada la frase "Aprendiendo Python con Edem". Escribe un
#programa que invierta el orden de las palabras en la frase, pero mantenga el orden de los caracteres en cada
#palabra. El resultado debería ser: "Edem con Python Aprendiendo"

def invertir_frase(frase):
    palabras = frase.split()  
    palabras_invertidas = palabras[::-1]  
    frase_invertida = ' '.join(palabras_invertidas)  

    return frase_invertida

frase_original = "Aprendiendo Python con Edem"
frase_invertida = invertir_frase(frase_original)
print(frase_invertida)