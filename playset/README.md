# Groupe de schobe_c 1026222

Dans un premier temps je déclare un tableau pour stocker les caractères que je n'ai pas rencontré

Je parcours tous les char de la string, si le char est déjà présent dans stock alors je renvoi True sinon je le stock

A la fin de la boucle si on n'a pas trouvé de doublon on renvoi False

La complexité maximale du programme dépend de la taille de la chaîne d'entrée s, ce qui donne une complexité linéaire O(n)
Dès que le programme détecte un doublon dans la chaîne d'entrée s il return True, la complexité minimale dépend donc de l'emplacement de doublon dans la chaîne s