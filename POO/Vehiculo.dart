/*
Hacer control de encendido de los vehiculos, para esto al momento de usar el método encender, se debe validar el nivel de combustible del vehiculo (medida dada en galones) no este por debejo de un 10%, si este tiene un nivel muy bajo, mostrar la advertencia que necesita ir a la gasolinera. 
*/


class Vehiculo {
  
  String marca;
  String combustible;
  var tipo;
  var capacidad_maxima;
  var nivel_combustible;
  
  Vehiculo(this.marca, this.combustible);
  
  void encender(){
    if ((nivel_combustible * 100) / capacidad_maxima < 10) {
      print("Advertencia, nivel de combustible bajo");
    } else {
      print("El nivel de combustible es optimo");
    }
  }
  
  void arrancar(consumo_combustible){
    nivel_combustible -= consumo_combustible;
      if(nivel_combustible <= 0){
        nivel_combustible = 0;
        print("Se ha quedado sin combustible. Se ha detenido la marcha.");
      }else if ((nivel_combustible * 100) / capacidad_maxima < 10){
        print("Advertencia, nivel de combustible bajo");
      }else{
        print('Acelerando. Nivel de combustible: ${nivel_combustible}');
      }
  }
  
  @override
  String toString() {
    return 'El vehiculo tipo ${tipo} ${marca} necesita gasolina ${combustible} para operar';
  }
}

class Carro extends Vehiculo {
  Carro(marca, combustible): super(marca, combustible) {
    tipo = "Carro"; 
    capacidad_maxima = 24;
    nivel_combustible = 20;
  }
}

class Moto extends Vehiculo {
  Moto(marca, combustible): super(marca, combustible) {
    tipo = "Moto";
    capacidad_maxima = 2.3;
    nivel_combustible = 1;
  }
}

void main() {
  Carro carro = new Carro('Mazda', 'Extra');
  carro.encender();
  carro.arrancar(10);
  carro.arrancar(9);
  carro.arrancar(1);
  
  Moto moto = new Moto('Suzuki', 'corriente');
  moto.encender();
}