function combinacao(numSapatos, numCalcas, numCamisetas) {
  // Verifica se os valores são números inteiros positivos
  if (
    !Number.isInteger(numSapatos) ||
    !Number.isInteger(numCalcas) ||
    !Number.isInteger(numCamisetas) ||
    numSapatos < 0 ||
    numCalcas < 0 ||
    numCamisetas < 0
  ) {
    console.log(`As variáveis devem conter números inteiros e positivos.`);
    return "null";
  }

  // Calcula o número de combinações usando a fórmula da combinação simples e retorna o resultado
  let numCombinacoes = numSapatos * numCalcas * numCamisetas;
  return numCombinacoes;
}

// Exemplo de uso da função
const numCombinacoes = combinacao(3, 2, 5);
console.log(`O número de combinações possíveis é ${numCombinacoes}.`);
