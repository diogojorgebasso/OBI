
# Tempo de Resposta

Sara adora trocar mensagens com amigos. Como ela recebe e envia muitas mensagens, está preocupada com o tempo que seus amigos esperam para receber respostas das mensagens.

## Regras de Etiqueta

As seguintes regras de etiqueta são sempre obedecidas:

1. As únicas mensagens que Sara envia são respostas a mensagens que ela recebeu.
2. Sara envia no máximo uma mensagem como resposta a uma mensagem que recebeu.
3. Um amigo de Sara nunca envia uma nova mensagem para Sara até que tenha recebido resposta da mensagem que enviou anteriormente.

O aplicativo de mensagens que Sara e seus amigos usam recebe e envia mensagens instantaneamente. O envio e o recebimento de mensagens são chamados de eventos. O aplicativo registra cada evento na ordem em que os eventos ocorrem, usando dois tipos de registro:

- `R X` indica que uma mensagem foi recebida do amigo `X`.
- `E X` indica que uma mensagem foi enviada ao amigo `X`.

O aplicativo usa ainda um outro tipo de registro, para indicar o tempo que se passou entre dois eventos consecutivos, na forma:

- `T X` indicando que `X` segundos se passaram entre o evento anterior e o evento posterior a esse registro.

Se não há registro do tipo `T X` entre dois registros de eventos consecutivos, significa que exatamente 1 segundo se passou entre esses dois eventos.

## Definição de Tempo de Resposta

O **Tempo de Resposta** de uma mensagem é o tempo que se passa entre o recebimento da mensagem por Sara e o envio da resposta a essa mensagem por Sara. Se um amigo recebeu respostas para todas as suas mensagens, o **Tempo de Resposta Total** para esse amigo é a soma dos Tempos de Respostas para as mensagens desse amigo; caso contrário, o Tempo de Resposta Total para esse amigo é `-1`.

Dada a lista de registros do aplicativo de Sara, sua tarefa é determinar o Tempo de Resposta Total para cada amigo.

## Entrada

A primeira linha da entrada contém um inteiro `N`, o número de registros. Os amigos de Sara são identificados por números inteiros. Cada uma das `N` linhas seguintes descreve um registro e contém um caractere (`R`, `E` ou `T`) seguido de um número inteiro `X`. No caso de registros dos tipos `R` e `E`, o valor de `X` indica um amigo de Sara; no caso do registro de tipo `T`, o valor de `X` indica o número de segundos que se passaram entre o evento anterior e o posterior.

## Saída

Para cada amigo de Sara, seu programa deve produzir uma linha na saída contendo dois inteiros: o número do amigo e o Tempo de Resposta Total para esse amigo, em ordem crescente dos números dos amigos.

## Restrições

- `1 ≤ N ≤ 20`
- `1 ≤ X ≤ 100`

### Informações sobre a pontuação

Para um conjunto de casos de testes valendo 20 pontos, `1 ≤ N ≤ 10`.
Para um conjunto de casos de testes valendo 80 pontos, nenhuma restrição adicional.

## Exemplos

### Entrada

```
5
R 2
R 3
T 5
E 2
E 3
```

### Saída

```
2 6
3 6
```

### Entrada

```
14
R 12
T 2
R 23
T 3
R 45
E 45
R 45
E 23
R 23
T 2
E 23
R 34
E 12
E 34
```

### Saída

```
12 13
23 8
34 2
45 -1
```
