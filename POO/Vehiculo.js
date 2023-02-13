class Vehiculo {

  constructor(marca, combustible) {
    this.marca = marca;
    this.combustible = combustible;
    this.encendido = false;
  }

  encender(llave = false) {
    if(llave){
      this.encendido = true;
      if ((this.nivel_combustible * 100) / this.capacidad_maxima < 10) {
        console.log("Advertencia, nivel de combustible bajo");
      }
      else {
        console.log("El nivel de combustible es optimo");
      }
    }else{
      console.error("Necesitas de una llave para encederlo");
    }
  }

  arrancar(consumo_combustible) {
    if(this.encendido){
      this.nivel_combustible -= consumo_combustible;
      if(this.nivel_combustible <= 0){
        this.nivel_combustible = 0;
        console.error("Se ha quedado sin combustible. Se ha detenido la marcha.");
      }else if ((this.nivel_combustible * 100) / this.capacidad_maxima < 10){
        console.warn("Advertencia, nivel de combustible bajo");
      }else{
        console.info(`Acelerando. Nivel de combustible: ${this.nivel_combustible}`);
      }
    }else{
      console.error(`Primero debes encender tu ${this.tipo}`);
    }
  }

  toString() {
    return `El vehiculo tipo ${this.tipo} ${this.marca} necesita gasolina ${this.combustible} para operar`;
  }
}

class Moto extends Vehiculo {
  constructor(marca, combustible) {
    super(marca, combustible);
    this.tipo = "Moto";
    this.capacidad_maxima = 2.3;
    this.nivel_combustible = 1;
  }
}

class Carro extends Vehiculo {
  constructor(marca, combustible) {
    super(marca, combustible);
    this.tipo = "Carro";
    this.capacidad_maxima = 24;
    this.nivel_combustible = 20;
  }
}


let carro = new Carro("Mazda", "Extra");
carro.encender(true);
carro.arrancar(3);
carro.arrancar(15);
carro.arrancar(20);

let moto = new Moto("Suzuki", "Corriente");
moto.encender();
moto.arrancar();
