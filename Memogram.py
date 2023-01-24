from collections import OrderedDict
import json as js
import codecs, random

file = codecs.open(filename='dictionary.json', encoding='utf-8', errors='ignore')
data = js.load(file)

longest_word = []
shortest_word = []
possible_word = []
expression = 'CSS'

def LongShort(value):
    if " " not in value and "-" not in value:
        if len(shortest_word) <= 0 and len(longest_word) <= 0:
            shortest_word.append(value)
            longest_word.append(value)

        if len(value) >= len(longest_word[0]):
            if len(value) < len(longest_word[0]):
                longest_word.clear()
            longest_word.append(value)

        if len(value) <= len(shortest_word[0]) and len(value) > 1:
            if len(value) < len(shortest_word[0]):
                shortest_word.clear()
            shortest_word.append(value)


for index in range(0, len(expression)):
    possible_word.append([])

    for each in range(0,len(data)):
        value = data[each]["word"]

        if " " not in value and "-" not in value:
            if value[0] == expression[index] and value[len(value)-1] == expression[0]:
                possible_word[index].append(value)
            
        #LongShort(value)
        #print(f'{each}:{shortest_word}')
        #print(f'{each}:{value}')

#print(f'H:\n{possible_word[0]}\nT:\n{possible_word[1]}')
#print(f'H:\n{possible_word[2]}\nT:\n{possible_word[3]}')

print(f'{LongShort(data)}')
for i in range(len(expression)): print(f'{random.choice(possible_word[i])} ', end='')