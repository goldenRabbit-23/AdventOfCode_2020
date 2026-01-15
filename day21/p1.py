import sys


def main():
    data = open(sys.argv[1]).read().split('\n')

    algs_to_ings = {}
    all_ings_list = []

    for line in data:
        ings_str, als_str = line.split(' (contains ')
        ingredients = set(ings_str.split())
        allergens = als_str[:-1].split(', ')

        all_ings_list.extend(list(ingredients))

        for allergen in allergens:
            if allergen not in algs_to_ings:
                algs_to_ings[allergen] = ingredients.copy()
            else:
                algs_to_ings[allergen] &= ingredients

    possible_allergenic_ings = set()
    for ingredients in algs_to_ings.values():
        possible_allergenic_ings.update(ingredients)

    print(sum(1 for ing in all_ings_list if ing not in possible_allergenic_ings))


if __name__ == '__main__':
    main()
