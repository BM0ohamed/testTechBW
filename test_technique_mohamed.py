#Question 1:
def test_chain(parentheses):
    if type(parentheses)!=str : 
        return False #choix arbitraire, le plus judicieux serait de raise une typeError
        # par ex : raise TypeError("input must be str")
    memory=[]
    for parenthese in parentheses :
        if parenthese =="(":
            memory.append(parenthese)
        if parenthese ==")":
            if len(memory)==0: 
                return False
            memory.pop()
    return len(memory)==0
#La complexité temporelle de cette fonction est en O(n) où n=len(input) car on n'itère
#qu'une seule fois sur tous les élements de la liste en entrée. 

#Au pire des cas, la compelxité spatiale = O(n) car celà reviendrait au cas où toutes les parenthèses sont ouvrantes
#donc on les stock tous dans memory.


#Question 2:
def find_wellformed_subchain(parentheses):
    if type(parentheses)!=str : 
        return 0 #choix arbitraire, le plus judicieux serait de renvoyer une typeError
    memory_pos=[-1]#On commence par 0 pour le cas où il n'y aurait aucune parenthèse ouvrante
    max_long=0
    for i, parenthese in enumerate(parentheses):
        if parenthese =="(":
            memory_pos.append(i)
        if parenthese==")":
            if len(memory_pos)>1:
                memory_pos.pop() 
                max_long = max(max_long, i-memory_pos[-1]) #on 
            else:
                memory_pos[0] = i
    return max_long


#Question 3 :
"""
A priori, il est possible de parallèliser cette tache en sur plusieurs machines, pour ça il faudrait couper la chaine principale en plusieurs sous chaines,
étudier les sous chaines sur chaque machine, centraliser les résultats partiels et les combiner à la fin pour avoir le résultat final. A mon avis la difficulté
réside dans les noeuds de la chaine. 
En ce qui concerne les performances et la complexité, a priori je n'ai pas trop d'estimations. Ces facteurs dépenderont fortement de la longueur de la chaine initial
ainsi que de chaque sous chaine, il faudrait aussi prendre en compte le temps de réception des données (les sous chaines) et le temps d'envoie des résultats intémédiaires,
mais aussi la centralisation et la concaténation de ces résultats pour donner le résultat final.
"""
if __name__ == '__main__':
    test_cases1 = [
        ('()', True),
        ('()()()()()', True),
        ('((((()()()))))', True),
        ('((())) ', True),
        ('', True),
        (' ',True),
        (213,False),
        (')(', False),
        ('()())(()()', False),
        ('(((()()()()()()))))', False),
        ('(((()))))', False),
        ('(', False),
    ]
    print("=====================================================================")
    print("=======================- Test Case for Q1 -==========================")
    for i, test_case in enumerate(test_cases1):
        parentheses, expected_output = test_case
        output = test_chain(parentheses)
        if output == expected_output:
            print(f'Test {i} CORRECT')
        else:
            print(f'Test {i} FAILED: expected {expected_output}, but got {output}')
    print("===================================================================== \n")

    test_cases2 = [
        (213,0),
        ('()', 2),
        ('()()()()()', 10),
        ('((())) ', 6),
        ('', 0),
        (' ',0),
        (')(', 0),
    ]
    print("=====================================================================")
    print("=======================- Test Case for Q2 -==========================")
    for i, test_case in enumerate(test_cases2):
        parentheses, expected_output = test_case
        output = find_wellformed_subchain(parentheses)
        if output == expected_output:
            print(f'Test {i} CORRECT')
        else:
            print(f'Test {i} FAILED: expected {expected_output}, but got {output}')
    print("===================================================================== \n")