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

    determined_ings = {}
    while algs_to_ings:
        allergen, candidates = min(algs_to_ings.items(), key=lambda x: len(x[1]))
        ing = next(iter(candidates))
        determined_ings[allergen] = ing
        del algs_to_ings[allergen]
        for s in algs_to_ings.values():
            s.discard(ing)

    print(','.join(ing for _, ing in sorted(determined_ings.items())))


if __name__ == '__main__':
    main()
