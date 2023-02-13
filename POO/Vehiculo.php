<?php
class Vehiculo {
    var $marca;
    var $combustible;
    var $tipo;
    var $capacidad_maxima;
    var $nivel_combustible;

    function __construct($marca, $combustible) {
        $this->marca = $marca;
        $this->combustible = $combustible;
    }

    function encender() {
        if (($this->nivel_combustible * 100) / $this->capacidad_maxima < 10) {
        echo "Advertencia, nivel de combustible bajo";
        } else {
        echo "El nivel de combustible es optimo";
        }
    }

    function arrancar($consumo_combustible) {
        $this->nivel_combustible -= $consumo_combustible;
        echo "\n {$this->nivel_combustible} \n";
        if ($this->nivel_combustible <= 0) {
            $this->nivel_combustible = 0s;
            echo "No tienes combustible!";
        }elseif (($this->nivel_combustible * 100) / $this->capacidad_maxima < 10) {
            echo "Advertencia, nivel de combustible bajo";
        }else{
            echo "Acelerando...";
        }
    }

    function __toString() {
        return "El vehiculo tipo {$this->tipo} {$this->marca} necesita gasolina {$this->combustible} para operar";
    }
}

class Moto extends Vehiculo {

  function __construct($marca, $combustible) {
    parent::__construct($marca, $combustible);
      $this->tipo = "Moto";
      $this->capacidad_maxima = 2.3;
      $this->nivel_combustible = 1;
  }
  
}

class Carro extends Vehiculo {

  function __construct($marca, $combustible) {
    parent::__construct($marca, $combustible);
    $this->tipo = "Carro";
    $this->capacidad_maxima = 24;
    $this->nivel_combustible = 20;
  }
}
  
$carro = new Carro("Mazda", "Extra");
echo $carro->encender();
echo "\n";
echo $carro->arrancar(10);
echo $carro->arrancar(8);
echo $carro->arrancar(5);
echo "\n";
$moto = new Moto("Suzuki", "Corriente");
echo $moto->encender();
?>