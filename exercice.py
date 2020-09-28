#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> bool:
    if values is None:
        # TODO: Demander les valeurs ici
        ma_liste = []
        while len(ma_liste) < 10:
            ma_liste.append(int(input('Entrez un entier : ')))

        resultat = True
        index = 0
        while index < len(ma_liste) - 1:
            if ma_liste[index] > ma_liste[index + 1]:
                resultat = False
                break
            index += 1
        print(resultat)

        # print(ma_liste == sorted(ma_liste)) - mieux pour des listes courtes, sinon non (ex : 1mil termes)

def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: Demander les mots ici
        pass

        mot1 = 'ALEVIN'
        mot2 = 'NIVELA'

        mot1 = list(mot1)
        mot2 = list(mot2)
        """
        if len(mot1) == len(mot2):
            for lettre in mot1:
                if lettre in mot2:
                    mot2.revome(lettre)
            if len(mot2) == 0:
                print('Anagramme')
            else:
                print('raté'
return False
        """

        print(sorted(mot1) == sorted(mot2))


def contains_doubles(items: list) -> bool:
    return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    return {}


def histogram(sentence: str) -> tuple:
    # TODO: Créer l'histogramme a l'aide d'un dictionnaire
    #       Afficher l'histogramme et les lettres les plus fréquentes
    #       Retourner l'histogramme et le tableau de lettres

    return {}, []


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingrédients et enregistrer dans une structure de données 
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    name, result = best_grades(grades)
    print(f"{name} a la meilleure moyenne: {result}")
    
    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
