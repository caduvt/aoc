# O funcionamento de findall é bastante particular.
# Quando usamos com um regex simples, vai retornar
# uma tupla apenas com os valores variáveis (nesse caso
# os dois valores numéricos). Caso seja um regex condicional,
# vai retornar:
  
#   1. regex completa
#   2. primeiro valor condicional
#   2.1 valores variáveis (os números nesse caso)
#   3. segundo valor condicional