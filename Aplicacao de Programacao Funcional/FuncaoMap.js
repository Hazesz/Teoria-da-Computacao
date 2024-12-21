//Função map
//declarando função que dobra o valor de um numero
function dobro(number){
    return number * 2;
};

//Uma lista de numeros
var numeros = [33, 4, 5, 9, 22, 44];

//utilizando o comando map para mandar os numeros da lista para a função
var resultado = numeros.map(dobro);

console.log(resultado);
