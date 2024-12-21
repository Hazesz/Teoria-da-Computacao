// Função Filter
// Declarando uma lista de elementos
var numbers = [2, 3, 4, 5, 6, 7, 8];

// Filtrar apenas os números pares
var filtro = numbers.filter(function par(number) {
    return number % 2 === 0;
});

console.log(filtro);