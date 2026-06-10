Conj1 = {'Carlos', 'Josiel', 'Jandira', 'Aline'}
Conj2 = {'Aline', 'Carlos', 'Jaqueline', 'Altair'}

print(f'Pessoas presentes nos dois grupos: {Conj1.intersection(Conj2)}')
print(f'Pessoas que estão em apenas um grupo: {Conj1.difference(Conj2), Conj2.difference(Conj1)}')
print(f'Todas as pessoas sem repetir nomes: {Conj1.union(Conj2)}')