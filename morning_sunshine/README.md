

Pour ce code, j'ai choisi d'utiliser une approche itérative pour parcourir la liste numbers à l'envers. Nous initialisons une variable max_num à une valeur 0 pour représenter le maximum rencontré jusqu'à présent. Ensuite, nous initialisons une liste result pour stocker les éléments qui sont strictement supérieurs à tous ceux situés après eux. Nous parcourons ensuite la liste numbers de la fin au début. Pour chaque élément, s'il est strictement supérieur au maximum actuel (max_num), nous l'ajoutons à la liste result et mettons à jour max_num. Enfin, nous renvoyons result dans l'ordre inverse, car nous avons parcouru la liste à l'envers.

Cela donne une complexité linéaire par rapport à la longueur de la chaîne d'entrée s, soit O(n), où n est la longueur de s.