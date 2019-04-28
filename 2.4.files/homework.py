
file = r'D:\Python\Netology\py-homework-basic-files\2.4.files\recipes.txt'


cook_book = dict()

def get_dish_qty(file):

    dish_qty = 1
    with open(file, encoding='utf-8') as f:
        for line in f:
            stripe = line.strip()
            if stripe == '':
                dish_qty += 1

    return dish_qty


def push_to_cook_book(file, dish_qty):

    with open(file, encoding='utf-8') as f:
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

cook_book = push_to_cook_book(file, get_dish_qty(file))


dish_list = ['Запеченный картофель', 'Омлет']
persons = 2

def get_shop_list_by_dishes(dishes, persons):

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