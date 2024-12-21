//Função Reduce
const numeros = [5,5,5,5];

//usando reduce para somar os numeros
const soma = numeros.reduce(function(acumulador, valoratual){

    return acumulador + valoratual;

}, 0);

//dividindo a soma pela quantidade de numeros
var media = soma / numeros.length;

console.log(media);