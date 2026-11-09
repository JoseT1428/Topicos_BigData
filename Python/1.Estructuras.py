print("Estructuras Condicionales")

# Condicional simple
notaTBI = 17
if notaTBI >= 10.51:
    print("Aprobastes")

#Condiciona Doble
edad = 17
if edad >= 18 :
    print("Tomar bebidas en exceso no es bueno")
else:
    print(" No apto pra menores")

#condicional anidado
nota = 20
if nota >17 & nota <=20:
    print("Alumno brillante")
elif nota >=14&nota<17:
    print("Alumno excelente")
elif nota >=10.5 & nota<113:
    print("Alumno regular")
else:
    print("BAjo rendimiento")

#Condicional Multiple

"""
Python 3.9.0 a versiones anteriores no existe 
"""
num = 4 
match num:
    case 1: print("Vocal A")
    case 2: print("Vocal A")
    case 3: print("Vocal A")
    case 4: print("Vocal A")
    case 5: print("Vocal A")
    case 6: print("Vocal A")
    case _: print("NUmero no corresponde a vocal")