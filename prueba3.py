import funciones as fun

while True:
    fun.limpiarpantalla()
    fun.printv("1) Registrar")
    fun.printv("2) Buscar")
    fun.printv("3) Certificado")
    fun.printr("0) Salir")
    opcion = int(input("Seleccion :"))

    if opcion==0:
        fun.printr("Nos vemos")
        break
    elif opcion==1:
        fun.titulo("registrar")
        
        

        

    