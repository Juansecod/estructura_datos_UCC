"""
Hacer control de encendido de los vehiculos, para esto al momento de usar el método encender, se debe validar el nivel de combustible del vehiculo (medida dada en galones) no este por debejo de un 10%, si este tiene un nivel muy bajo, mostrar la advertencia que necesita ir a la gasolinera. 
"""
class Vehiculo:

  marca: str
  combustible: str
  tipo: str
  capacidad_maxima: float
  nivel_combustible: float
  encendido: bool

  def __init__(self, marca, combustible):
    self.marca = marca 
    self.combustible = combustible
    self.encendido = False

  def encender(self, llave = False):
    if llave:
      self.encendido = True
      if (self.nivel_combustible * 100) / self.capacidad_maxima < 10:
        print("Advertencia, nivel de combustible bajo")
      else:
        print("El nivel de combustible es optimo")
    else:
      print("Necesitas una llave.")
    
  def arrancar(self, consumo_combustible):
    if self.encendido:
      self.nivel_combustible -= consumo_combustible
      if(self.nivel_combustible <= 0):
        self.nivel_combustible = 0
        print("Se ha quedado sin combustible. Se ha detenido la marcha.")
      elif (self.nivel_combustible * 100) / self.capacidad_maxima < 10:
        print("Advertencia, nivel de combustible bajo")
      else:
          print(f"Acelerando. Nivel de combustible: {self.nivel_combustible}")
    else:
      print("Primero debes encender tu {}".format(self.tipo))

  def __str__(self):
    return "El vehiculo tipo {} {} necesita gasolina {} para operar".format(self.tipo, self.marca, self.combustible)


class Moto(Vehiculo):
  
  def __init__(self, marca, combustible):
      super().__init__(marca, combustible)
      self.tipo = 'Moto'
      self.capacidad_maxima = 2.3
      self.nivel_combustible = 1

class Carro(Vehiculo):
  
  def __init__(self, marca, combustible):
      super().__init__(marca, combustible)
      self.tipo = 'Carro'
      self.capacidad_maxima = 24
      self.nivel_combustible = 20


carro = Carro('Mazda', 'Extra')
carro.encender(True)
carro.arrancar(3)
carro.arrancar(10)
carro.arrancar(20)

moto = Moto('Suzuki', 'Corriente')
moto.encender()
moto.arrancar(3)
