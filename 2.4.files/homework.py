
file = 'recipes.txt'


def add_to_recipes(file):

    file = file

    def get_dish_qty(file):

        dish_qty = 1
        with open(file) as f:
            for line in f:
                stripe = line.strip()
                if stripe == '':
                    dish_qty += 1
        
        return dish_qty


    def push_to_cook_book(file):

        cook_book = dict()
        dish_qty = get_dish_qty(file)

        with open(file) as f:
            for i in range(0, dish_qty):
                dish_name = f.readline().strip()
                qty = int(f.readline())
                cook_book[dish_name] = list()

                for i in range(0, qty):
                    products = f.readline().strip().split(' | ')
                    ingridient_name = products[0]
                    quantity = products[1]
                    measure = products[2]

                    cook_book[dish_name].append({
                        'ingridient_name' : ingridient_name,
                        'quantity' : quantity,
                        'measure' : measure
                    })
        
                f.readline()

        return cook_book

    return (push_to_cook_book(file))

print(add_to_recipes(file))


def get_shop_list_by_dishes(dish_list, persons, file_recipes):

    cook_book = add_to_recipes(file_recipes)

    shop_list = dict()

    for dish in dish_list:
        product_list = cook_book[dish]

        for product in product_list:
            product_name = product['ingridient_name']
            product_qty = int(product['quantity']) * persons
            product_measure = product['measure']

            shop_list[product_name] = ({
                'measure' : product_measure, 
                'qty' : product_qty
                })

    return shop_list
