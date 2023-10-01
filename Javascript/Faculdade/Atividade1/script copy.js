var combinacao = (numSapatos, numCalcas, numCamisetas) => {
  // Calcula o número de combinações usando a fórmula da combinação simples e retorna o resultado
  let numCombinacoes = numSapatos * numCalcas * numCamisetas;
  return numCombinacoes;
};

// Exemplo de uso da função
const numCombinacoes = combinacao(3, 2, 5);
console.log(`O número de combinações possíveis é ${numCombinacoes}.`);
