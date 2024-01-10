from principal import *
from configuracion import *
import random
import math
import string

#Lee el archivo y carga en la lista diccionario todas las palabras.
def lectura(diccionario):
    listaPalabras = open("lemario.txt", "r",encoding="latin1")
    for elem in listaPalabras:
        diccionario.append(elem[:-1])


#Devuelve una cadena de 7 caracteres sin repetir con 2 o 3 vocales y a lo sumo
#con una consonante dificil (kxyz).
def vocalCheck(Cadena):
    voc = 0
    vocales = "aeiou"
    for char in Cadena:
     if char in vocales:
      voc = voc + 1
    return voc

def dameConsonante(cad):
    vocales = "aeiou"
    cons = 0
    azar = ""
    while cons < 1:
        nums = random.randint(0, len(cad)-1)
        if cad[nums] not in vocales:
         azar = azar + cad[nums]
         cons = cons + 1
    return azar

def dame7Letras(cadena):
    o = 1
    vocales = "aeiou"
    cadena = ""
    cont = random.randint(2, 3)
    while (o <= 7):
        letra = random.choice(string.ascii_lowercase)
        if letra not in cadena:
            cadena = cadena + letra
            o = o + 1
    vocs = vocalCheck(cadena)
    while vocs < cont:
         consonanteAzar = dameConsonante(cadena)
         num = random.randint(0, 4)
         while vocales[num] not in cadena:
                cadena = cadena.replace(consonanteAzar, vocales[num])
                vocs= vocs + 1
    return cadena

def dameLetra(letrasEnPantalla):            #Elige una letra de las letras en pantalla.
    dame7Letras(letrasEnPantalla)
    letraAzar = random.randint(0, len(letrasEnPantalla)-1)
    return letrasEnPantalla[letraAzar]


#Si es valida la palabra devuelve puntos sino resta.
def procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario):
    #sonidos extras:
    sumaPuntos = pygame.mixer.Sound("efecto_suma_puntos.mp3")
    restaPuntos = pygame.mixer.Sound("efecto_resta_puntos.mp3")
    validez = esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario)
    if validez == True:
        sumaPuntos.play()
        puntaje = puntos(candidata)
    else:
        restaPuntos.play()
        puntaje = -1
    return puntaje


#Chequea que se use la letra principal, solo use letras de la pantalla y
#exista en el diccionario.
def esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario):
    if letraPrincipal not in candidata:         #Verifica que se use la letre principal, si letraPrincipal no está en candidata da False.
        return False
    for letra in candidata:                     #Recorre la variable "candidata" con "letra".
        if letra not in letrasEnPantalla:
            return False
    if candidata.lower() not in diccionario:
        return False
    return True


#Devuelve los puntos.
def puntos(candidata):
    pts = 0
    if len(candidata) == 3:
        pts += 1
    if len(candidata) == 4:
        pts += 2
    if len(candidata) >= 5 and len(candidata) < 7:
        pts += len(candidata)
    if len(candidata) == 7:
        pts += 10
    return pts


#Busca en el diccionario paralabras correctas y devuelve una lista de estas.
def dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario):
    palabras_correctas = []
    for palabra in diccionario:
        if letraPrincipal in palabra and estanTodas(palabra, letrasEnPantalla):
            palabras_correctas.append(palabra)
    print(palabras_correctas)
    return palabras_correctas

def estanTodas(palabra, letrasEnPantalla):
    for letra in palabra:
        if letra not in letrasEnPantalla:
            return False
    return True
