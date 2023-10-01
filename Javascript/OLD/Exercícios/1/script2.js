var idade = parseInt(prompt('Qual sua idade?'))

if (idade >= 18) {
    alert('Sim, você pode consumir bebidas alcoolicas.')
    var pedido = prompt('Qual o seu pedido?')
    alert('Certo! Em poucos minutos volto com sua ' + pedido + '.')
}

else
    alert('Você ainda não pode consumir bebidas álcoolicas. Volte futuramente.')



