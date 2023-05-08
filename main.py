from itertools import product  

gramatica = {'S': [('a', 'A'), ('d', 'E')], 
             'A': [('a', 'B'), ('a', 'S')], 
             'B': [('b', 'C')],
             'C': [('b', 'D'), ('b', 'B')], 
             'D': [('c', 'D'), '*'], 
             'E': ['*']}

def verifCuv(gramatica, s, cuv):
    if len(cuv) == 0 and '*' in gramatica[s]: #cuv vin in starea de final
        return True 

    for stare in gramatica[s]:
        if cuv and cuv[0] == stare[0] and stare[0].islower():
            if verifCuv(gramatica, stare[1], cuv[1:]): #trec la urmatoarea litera mica
                return True
    return False
#        elif aux[0].isupper():
#               verifCuv(gramatica, aux[0], aux[1] + cuv) #intru pe literele mari

s = 'S'
ok = 0
string = input("Dati literele ")
n = int(input("Dati lungimea maxima "))
if '*' in gramatica[s]:
    print("E acceptat cuvantul vid!")
    ok = 1
for i in range(1,n+1):
    for cuv in (product(list(string), repeat = i)):
        if(verifCuv(gramatica, 'S', ''.join(list(cuv)))):
            print(''.join(list(cuv)))
            ok = 1
if ok == 0:
    print("Nu exista cuvant")
    pass
    
#print(verifCuv(gramatica, s, 'eee'))
    