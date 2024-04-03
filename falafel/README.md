# Groupe de schobe_c 1026222

Je déclare un tableau pour stocker les char rencontrés
    un tableau pour stocker le nombre d'occurence des char
    un int pour check les char avec un nombre d'occurence impaire (il ne peut y en avoir qu'un (si la string est impaire), tous les autres char doivent avoir un nombre d'occurence pair)

Je parcours l'input dans les deux sens pour réduire le nombre d'itérations
Je stock les nouveaux char et j'incrémente le compteur de ceux connus

Je parcours mon tableau count pour verifier que les char soient tous pair (sauf 1 si la string d'input est impaire)

Le programme parcours l'ensemble de la chaîne d'entrée s ainsi que le tableau count dont la taille dépend de s donc on a bien une complexité linéaire O(n)