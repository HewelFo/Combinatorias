from math import factorial

def Combinacion(n, r):
    ## funcion para resolver combinacion sin repeticiones
    return (factorial(n)/(factorial(r)*(factorial(n-r))))

def CombinacionR(n, r):
    ## resulve combinaciones sin repeticion
    return ((factorial(n+r-1))/(factorial(r)*(factorial(n-1))))

def Variacion(n, r):
    ## resulve variaciones si repeticiones
    return (factorial(n)/(factorial(n-r)))

def VariacionR(n, r):
    ## resielve variaciones con repeticiones
    return (pow(n,r))

def Permutacion(n):
    ## resulve permutacion sin repeticiones
    return factorial(n)

def PermutacionR(n, a):
    ## resulve permutaciones con repeticiones
    divisor = 0
    i = 0
    while i != len(a):
        divisor *= factorial(a[i])
    return (factorial(n)/divisor)

def ArregloPermut():
    ## una funcion que toma la cantidad 
    ## de elementos q sacaran factorial en PermutacionR()
    fini = "ya"
    conjuF = []
    while fini == "ya":
        conjuF.append(int(input("sifras q se repiten: ")))
        fini = input("para terminar escribe -ya-:")
    return conjuF

intro = 1
while intro == 1:

    intro = input("importa el orden: ")
    if intro == "si":
        
        intro = input("se usan todos los elementos: ")
        if intro == "si":

            intro = input("se pueden repetir los elementos: ")
            if intro == "si":
                ##------------------------------------------------------
                print("permutacion con repeticion")
                print("recuerda que n siempre debe ser mayor que r")
                n = int(input("n= "))
                r = ArregloPermut()
                print(PermutacionR(n, r))
            
            else:
                ##------------------------------------------------------
                print("Permutacion sin repeticon")
                n = int(input("n= "))
                print(Permutacion(n))
        
        else:

            intro = input("se pueden repetir los elementos: ")
            if intro == "si":
                ##------------------------------------------------------
                print("variacioncon con repeticion")
                print("recuerda que n siempre debe ser mayor que r")
                n = int(input("n= "))
                r = int(input("r= "))
                print(VariacionR(n,r))
            else:
                ##------------------------------------------------------
                print("variacion sin repeticion")
                print("recuerda que n siempre debe ser mayor que r")
                n = int(input("n= "))
                r = int(input("r= "))
                print(Variacion(n, r))
    else:

        intro = input("se pueden repetir los elementos: ")
        if intro == "si":
            ##---------------------------------------------------------
            print("combinacion con repeticion")
            print("recuerda que n siempre debe ser mayor que r")
            n = int(input("n= "))
            r = int(input("r= "))
            print(CombinacionR(n,r))
        else:
            ##----------------------------------------------------------
            print("variacion sin repeticion")
            print("recuerda que n siempre debe ser mayor que r")
            n = int(input("n= "))
            r = int(input("r= "))
            print(Combinacion(n,r))
    
    intro = int(input("para reitentar preciona 1 para terminar 0: "))
    if intro == 0:
        print("gracias por entrar")