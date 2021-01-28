class Coche():

    '''
    Propiedades o caracteristicas
    '''
    color = None
    modelo = None
    freno_mano = None
    llantas = None

    def __init__(self):
        print("Clase coche")

    '''
    Metodos
    '''
    def arrancar(self):
        print("Metodo arrancar")
    
    def apagar(self):
        print("Metodo apagar")

# Creacion de un objeto basado en una clase
vocho = Coche()

# Asiganacion de valores a las propiedades
vocho.color = "rojo"
vocho.modelo = 2000
vocho.freno_mano = "si"
vocho.llantas = 4

# Imprimir valore de las propiedades
print(vocho.color)
print(vocho.modelo)
print(vocho.freno_mano)
print(vocho.llantas)

# Invocar metodos de la clase
vocho.arrancar()
vocho.apagar()
vocho.arrancar()
