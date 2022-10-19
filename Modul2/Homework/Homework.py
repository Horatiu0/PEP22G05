# exercitiul 1

print('Astazi ma duc la "facultate".')           # punctul a
print("Astazi ma duc la \"facultate\".")         # punctul a
print('/*\/*\*/*\/*\\\nPython\n\./\./\./\./')    # punctul b

#punctul b
print(
"""
/*\/*\*/*\/*\\
Python
\./\./\./\./
""")

#punctul c
print("P","y","t","o","n", sep="   ")

#exercitiul 2
nume = input("Cum te numesti ?")
varsta = int(input("Ce varsta ai ?"))
print("Ceau",nume, "deci te-ai nascut in ", int(2022) - varsta)

#exercitiu 3
a = input("introduceti un sir:")
print("lungimea sirului este:", len(a))
print(f"lungimea sirului este: {len(a)}")
print("lungimea sirului este:" + str(len(a)))
print("lungimea sirului este:", float(len(a)))

#exercitiul 4
#punctul a
print('/-\\'.center(7))
print('//-\\\\'.center(7))
print('_______'.center(7))
print('\\\\-//'.center(7))
print('\\-/'.center(7))

#punctul b
print('----'.center(8))
print('/    \\'.center(8))
print('/______\\'.center(8))

#punctul c
print('*'.center(8))
print('***'.center(8))
print('*****'.center(8))
print('*******')

# exercitiul 5
a = input("introduceti un cuvant:")
print('Este palindrom', a[::-1] == a)
print('Este polidrom:', a.lower() == a.lower()[::-1])

# exercitiul 6
a = 'Hello Python'
b = 'Ana are mere'
c = 'Pizza Party'
c1 = 'Pizza{}Party'

result = a.split()
print(result[0],result[1], sep='_')

print(a.split()[0],a.split()[1], b.replace(" ","_"),c1.format('_') , sep='_')
print(a.split()[0],a.split()[1], b.replace(" ","_"),c1.format('_'), "." , sep='_')
print(a.split()[0]*4, a.split()[1] , b.split()[0]*4, b.split()[1], b.split()[2], c.split()[0]*4, c.split()[1])

#exercitiul 7
a = 5.
b = 5
c = 'ana'

print('locatia lui a este:',hex(id(a)))
print('locatia lui b este:',hex(id(b)))
print('locatia lui c este:',hex(id(c)))

print('tipul variabilei a este', type(a))
print('tipul variabilei b este', type(b))
print('tipul variabilei c este', type(c))



