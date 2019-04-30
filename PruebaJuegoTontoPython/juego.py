#@@@@    Juego de Hunde la flota v.0.2@@@#
from random import randint
from collections import namedtuple
def validarEntero(min,max,respuesta1,respuesta2):
    """int,int,str,str-->int
    OBJ: valida si el número es entero , si no es el caso lo vuelve a pedir.
    PRE: min<max, ambos numeros deben ser enteros"""
    error= False
    try: entero=int(input(respuesta1))
    except: error= True
    while error or not (min<=entero<=max):
        print('Introduzca un número entre', min, 'y', max,'.', end=' ')
        error= False
        try: entero=int(input(respuesta2))
        except: error=True
    return entero
def juegoHundirFlota(nombre):
    """ str-->str
    OBJ: juego de hundir la flota de un jugador y la máquina
    PRE: """
    reintento= True
    while reintento:
        tPuntoUsuario= namedtuple('x','Ataque,Defensa')
        tPuntoCPU= namedtuple('CPU','Ataque,Defensa')
        puntoUsu=tPuntoUsuario( validarEntero(0,10,'Introduzca una posicion de ataque','Introduzca una posición válida',), validarEntero(0,10,'Introduzca una posicion de defensa','Introduzca una posición válida',))
        puntoCPU=tPuntoCPU(randint(0,10),randint(0,10))
        if puntoUsu[0]  ==  puntoCPU[1]:
            print('Ha ganado, enhorabuena')
            reintento=False
        elif puntoCPU[0] == puntoUsu[1]:
            print('Perdiste')
            reintento=False
        else:
            reintento=True
#Probador
Bili=1
juegoHundirFlota(Bili)

        
    
    
    
