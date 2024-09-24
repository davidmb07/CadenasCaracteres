#1. Teniendo en cuenta las siguientes variables que describen su edad,
# nombre y comida favorita, genera una cadena para presentarse:
name = 'Luis'
age = 27
favoriteFood = 'Pasta con salsa Boloñesa'
text = f'''Hola! Mi nombre es {name}.
Yo tengo {age} años, 
y mi comida favorita es {favoriteFood}!!'''
print(text)
print('____________________________________')
print('')

#2. Crea un código que solicite al usuario su nombre completo. Luego deberá
# contar el número de letras de su nombre, ignorando los espacios. Finalmente,
# debe saludar al usuario e informarle la longitud de su nombre.
fullName = input("Por favor, introduce tu nombre completo: ")
longitud = len(fullName.replace(' ', ''))
text1 = f"Hola, {fullName}! Tu nombre tiene {longitud} letras, excluyendo los espacios."
print(text1)
print('____________________________________')
print('')

#3. El analista de datos de una prestigiosa empresa láctea de la ciudad de Popayán,
# calculó las cifras de ventas del último trimestre: el porcentaje de aumento de las
# ventas y crecimiento de ingresos. Genere una cadena que le permita mostrar los porcentajes.
increaseSalesPercent = 12.93720081
revenueGrowthPercent = 18.33206078
text2 = f'''Las ventas de la empresa láctea aumentaron un {increaseSalesPercent:.2f}%,
 y los ingresos crecieron un {revenueGrowthPercent:.2f}%.'''
print(text2)
print('____________________________________')
print('')

#4. Se proporciona un mensaje secreto codificado en una cadena, para decodificar
# el mensaje: "Omita los primeros tres caracteres y luego omita todos los demás caracteres".
secretMessage = 'aS!Ir waQm  VL!eDafrcnXi n=gS .P,yytahgoln.!'
decodedMessage = secretMessage[3::2]
print(decodedMessage)
print('____________________________________')
print('')

#5. Se proporciona una frase y luego se debe mostrar el número de palabras en esa frase.
text = 'EL nombre "Python" viene dado por la afición de Van Rossum al grupo Monty Python.'
contador = len(text.split())
print(f'El número de palabras que hay en la frase es: {contador}')
print('____________________________________')
print('')

#6. Escriba un programa que tome una cadena como entrada y reemplace todas las apariciones
# de la letra "a" con la letra "e".
word = 'Camila'
new_word = word.replace('a', 'e')
print(new_word)
print('____________________________________')
print('')

#7. Dada la siguiente frase, escriba un programa que invierta el orden de las palabras en
# esa frase.
sentence = 'La historia del lenguaje de programación Python'
inverted_sentence = sentence.split()[::-1]
print(*inverted_sentence)
