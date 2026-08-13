import random

opcióndecomputadora=["piedra","papel","tijera"]
Victoriadelusuario=0
Victoriadelcomputadora=0
Victoriadelusuariostring="¡Ganaste!"
Victoriadelcomputadorastring="Perdiste."


#make a function to decide who wins
def ganador(eleccióncomputadora,eleccióndelusuario):
    if eleccióncomputadora==eleccióndelusuario:
        return "Empataste."
    elif eleccióncomputadora=="papel":
        if eleccióndelusuario=="tijera":
            return Victoriadelusuariostring
        else:
            return Victoriadelcomputadorastring
    elif eleccióncomputadora=="tijera":
        if eleccióndelusuario=="piedra":
            return Victoriadelusuariostring
        else:
            return Victoriadelcomputadorastring
    else:
        # eleccióncomputadora=="piedra"
        if eleccióndelusuario=="papel":
            return Victoriadelusuariostring
        else:
            return Victoriadelcomputadorastring
      
    
#Adaptar las respuestas del ordenador para vencer al jugador.
def añadiralalista(opcióndecomputadora,eleccióndelusuario):
    if(eleccióndelusuario=="piedra"):
        opcióndecomputadora.append("papel")
        opcióndecomputadora.append("papel")
    elif (eleccióndelusuario=="papel"):
        opcióndecomputadora.append("tijera")
        opcióndecomputadora.append("tijera")
    else:
        opcióndecomputadora.append("piedra")
        opcióndecomputadora.append("piedra")
    return


#programa principal
while(True):
    eleccióndelusuario=input("¿Qué elegirás? (¿Piedra, papel o tijera, o retirarse?)")
    if eleccióndelusuario=="retirarse":
        print("¡Adiós! ¡Gracias por jugar!")
        break
    else:
        if eleccióndelusuario=="piedra" or eleccióndelusuario=="tijera" or eleccióndelusuario=="papel":
            eleccióncomputadora=random.choice(opcióndecomputadora)
            print("La computadora eligió "+eleccióncomputadora)
            resultado=ganador(eleccióncomputadora,eleccióndelusuario)
            print(resultado)
            if resultado==Victoriadelusuariostring:
                #Hagámoslo más difícil.
                
                if Victoriadelusuario-Victoriadelcomputadora>5:
                    #Restablece la lista.
                    opcióndecomputadora=["piedra","papel","tijera"]
                else:
                    añadiralalista(opcióndecomputadora,eleccióndelusuario)

                Victoriadelusuario=Victoriadelusuario+1
            elif resultado==Victoriadelcomputadorastring:
                Victoriadelcomputadora=Victoriadelcomputadora+1
 
            print("Puntuación del computadora. ="+str(Victoriadelcomputadora))
            print("Puntuación del jugador ="+str(Victoriadelusuario))

        else:
            print("Elige piedra, papel o tijera.")
                                                                                                                                                                                                                                                                                                                      