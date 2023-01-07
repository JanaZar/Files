print('What do you want to write?')
answer = input('Enter your answer: ')
print(f'How many time do you want to print?')
i = int(input('Enter your answer: '))

file = open('p.txt', 'w')

for n in range(i):
    file.write(f'{answer}\n')
file.close
