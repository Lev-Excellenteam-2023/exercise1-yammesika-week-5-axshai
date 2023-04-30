def get_recipe_price(prices, optionals=None, **ingredients):
    """
     Calculates the total price of a recipe based on the prices of the ingredients.
    :param prices: A dictionary that maps ingredient names to their price per 100 grams.
    :param optionals: A list of optional ingredients that will not be included in the total price calculation.
    :param ingredients: A variable-length keyword argument list that maps ingredient names to their weight in grams.
    :return: The total price of the recipe based on the prices of the ingredients, excluding any optional ingredients.
    """
    if optionals is None:
        optionals = []
    total_price = 0
    for item, price_for_100_gram in prices.items():
        if item not in optionals:
            total_price += ingredients[item] / 100 * price_for_100_gram
    return total_price


if __name__ == "__main__":
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
