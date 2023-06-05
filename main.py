import requests
import json
from tabulate import tabulate

API_ENDPOINT = "https://trackapi.nutritionix.com/v2/search/instant"
HEADERS = {
    'x-app-id': '70358fd5',
    'x-app-key': 'cf7a7ad737dca347015f1ab1e7b9b4a8',
    'x-remote-user-id': '0',
}

def get_nutrient_value(product, nutrient_id):
    for nutrient in product.get('full_nutrients', []):
        if nutrient['attr_id'] == nutrient_id:
            return nutrient['value']
    return 0

def main():
    meals = ['breakfast', 'lunch', 'dinner', 'snacks']
    daily_intake = {meal: {} for meal in meals}

    # Initialize goals
    goals = {}
    nutrients_list = ['Calories', 'Fat', 'Protein', 'Carbohydrates', 'Vitamin C', 'Iron']
    for nutrient in nutrients_list:
        goals[nutrient] = float(input(f"Please enter your daily goal for {nutrient} (in grams): "))

    for meal in meals:
        while True:
            product_name = input(f"Please enter the name of a {meal} item (or 'done' if finished): ")
            if product_name.lower() == 'done':
                break

            params = {
                'query': product_name,
                'branded': True,
                'detailed': True
            }

            response = requests.get(API_ENDPOINT, headers=HEADERS, params=params)
            products = response.json()['branded']

            for i, product in enumerate(products, start=1):
                print(f"{i}. {product['food_name']}")

            product_idx = int(input("Please enter the number of the product you want to add: ")) - 1
            product = products[product_idx]

            portion_size = float(input(f"Please enter the portion size for this item (in grams): "))

            nutrients = {
                'Calories': product.get('nf_calories', 0),
                'Fat': get_nutrient_value(product, 204),      # 204 is the id for Fat
                'Protein': get_nutrient_value(product, 203),  # 203 is the id for Protein
                'Carbohydrates': get_nutrient_value(product, 205),  # 205 is the id for Carbohydrates
                'Vitamin C': get_nutrient_value(product, 401),  # 401 is the id for Vitamin C
                'Iron': get_nutrient_value(product, 303)  # 303 is the id for Iron
            }

            serving_weight = product.get('serving_weight_grams', 100)
            if serving_weight is None:  # If serving_weight is None, set it to 100
                serving_weight = 100

            for nutrient, value in nutrients.items():
                nutrients[nutrient] = round((value / serving_weight) * portion_size, 2)

            daily_intake[meal][product['food_name']] = nutrients

    final_tally = {nutrient: 0 for nutrient in nutrients_list}

    for meal, products in daily_intake.items():
        for product in products.values():
            for nutrient, amount in product.items():
                final_tally[nutrient] += amount

    print("\nFinal Tally:")
    table_data = []
    for nutrient in nutrients_list:
        amount = final_tally.get(nutrient, 0)
        goal = goals.get(nutrient, 0)
        table_data.append([nutrient, f"{amount}g", goal, f"{round((amount / goal) * 100, 2)}%"])

    print(tabulate(table_data, headers=['Nutrient', 'Amount', 'Goal', 'Achieved'], tablefmt='pretty'))

if __name__ == '__main__':
    main()
