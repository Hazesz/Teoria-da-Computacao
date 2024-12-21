function dobro(number){
    return number * 2;
};

var numeros = [33, 4, 5, 9, 22, 44];

var resultado = numeros.map(dobro);

console.log(resultado);