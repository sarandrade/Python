# Continue -> interrompe a repetição e vai para a próxima
for x in range(1, 11):
    if x % 2 == 0:
        continue
    print(x)
print()

# Break -> interrompe a repetição e sai do laço
for x in range(1, 11):
    if x == 5:
        break
    print(x)

print('FIM!')
