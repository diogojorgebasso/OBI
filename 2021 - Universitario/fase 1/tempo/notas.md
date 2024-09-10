Alguns dados importantes do Exercício:

ENTRADA
- 1 segundo se passa entre dois eventos.
- Os estados E, R referem-se ao envio e recebimento da mensagem; T ao tempo decorrido entre o último evento e o próximo.

SAÍDA
- em ordem *crescente* dos números dos amigos.

Com isso mente, primeiro tentei rodar uma função assintótica para identificar os dois valores de estado (R e E), mas isso se provou não ser tão fácil. A abordagem mais simples provou ser criar um dicionário com todos os amigos em primeiro análise e em seguida rodar um loop dos amigos com todos os valores, aliado a booleano e checar em qual indíce está a saída e o começo. Isso, somando-se a uma variável independente para cada letra, nos dá a resposta.