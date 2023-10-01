var prova1 = 9;
var prova2 = 1.5;

var media = (prova1 + prova2)/2
console.log(`Sua média foi ${media}.`);

if (media >= 6){
    console.log('Parabéns, você foi aprovado.')
}
else{
    console.log('Desculpe, sua nota não foi suficiente.')
}

var rendimento;

if (media >= 8){
    rendimento = 1
}
else if (media >=6 && media < 8){
    rendimento = 2
}
else{
    rendimento = 3
}

switch(rendimento){
    case 1:
        console.log('Parabéns, seu rendimento foi ótimo! Continue assim.')
        break
    case 2:
        console.log('Parabéns, seu rendimento foi bom. Não esqueça de revisar os assuntos.')
        break
    case 3:
        console.log('Seu rendimento não contemplou os requisitos mínimos. Você foi indicado a retenção. Estude mais.')
        break
    default:
        console.log('Houve algum erro.')
        break
}