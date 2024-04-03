# Groupe de schobe_c 1026222

Dans un premier temps je vérifie qu'il n'y est pas d'erreur dans les arguments:
    si la liste compte au moins 1 élément
    si l'index k est bien dans la liste

Si la liste ne compte qu'un élément on renvoi True

On parcours tous les éléments de la liste,
    on vérifie que les élément avant numbers[k] sont bien strictement inférieurs à numbers[k] sinon on renvoi False
    et que les éléments après numbers[k] sont bien supérieurs ou égaux à numbers[k] sinon on renvoi False

Si la liste à passé les tests sans soucis on renvoi True

La complexité maximale du programme dépend de la taille du tableau d'entrée 'numbers' ce qui donne une complexité algorithmique linéaire O(n)
La compléxité minimale dépend de l'index de la case du tableau d'entrée où le programme détecte une erreur