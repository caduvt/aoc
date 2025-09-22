import re

file = open('input.txt', 'r')

input = file.read()

# O funcionamento de findall é bastante particular.
# Quando usamos com um regex simples, vai retornar
# uma tupla apenas com os valores variáveis (nesse caso
# os dois valores numéricos). Caso seja um regex condicional,
# vai retornar:
  
#   1. regex completa
#   2. primeiro valor condicional
#   2.1 valores variáveis (os números nesse caso)
#   3. segundo valor condicional

regex = r"(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))"
match = re.findall(regex, input)

output = 0
enabled = True

if match:
  for tuple in match:
    if 'do()' in tuple:
      enabled = True
    elif "don't()" in tuple:
      enabled = False
    elif enabled:
      a = int(tuple[1])
      b = int(tuple[2])
      output += a * b

print(output)
