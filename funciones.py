import os
import msvcrt
import numpy
from colorama import Style, Fore, Back

registro = numpy.empty((10,8),object)
def limpiarpantalla():
    print("<<<<<Presione tecla>>>>>")
    msvcrt.getch()
    os.system('cls')



def printr(texto):
    print(f"{Fore.RED}{Style.BRIGHT}{texto}{Fore.RESET}{Style.RESET_ALL}")

def printv(texto):
    print(f"{Fore.GREEN}{Style.BRIGHT}{texto}{Fore.RESET}{Style.RESET_ALL}")


def titulo(texto):
    print("--------------------")
    print(f"{texto.upper}")
    print("--------------------")


def verificarrut(Rut):
    for i in range(10):
        if registro(1,0) ==Rut:
            return
    return -1
    

def registrar(Rut,nombrecompleto,edad,genero,notas,fechamatricula,nombreapoderado):
    if None in registro:
        if verificarrut(Rut)!= -1:
            if len(Rut):
                if nombrecompleto >=2 and nombrecompleto<=30:
                    if edad>=4:
                        for i in range(10):
                            if registro(1,0)==None:
                               registro[1.0]==Rut
                               registro[1.1]==nombrecompleto
                               registro[1.2]==edad
                               registro[1.3]==genero
                               registro[1.4]==notas
                               registro[1.5]==fechamatricula
                               registro[1.6]==nombreapoderado
                               print(f"Datos de Joven {nombrecompleto} se han Registrado de manera exitosa")
                               break
                    else:
                        print("edad invalida es menor a 4 años")
                else:
                    print("Nombre invalido demasiado corto/largo")
        else:
            print("Rut invalido o Rut ya registrado")
    else:
        print("espacios llenos")

def buscar():
    for i in range(10):
        if registro(1,0) == None:
            print(f"{registro(1,0)}\t{registro(1,1)}\t{registro(1,2)}\t{registro(1,3)}\t {registro(1,4)}\t {registro(1,5)}\t{registro(1,6)}")

        
def certificacion(Rut):
    posicion = verificarrut(Rut)




   
    
            
            


                    

