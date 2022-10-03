import json

from chardet import detect


def write_order_to_json(item, quantity, price, buyer, date, encoding_file='utf-8'):
    order = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }
    with open('orders.json', 'r', encoding=encoding_file) as orders_file:
        content = orders_file.read()
        orders = json.loads(content)
    orders['orders'].append(order)
    with open('orders.json', 'w', encoding='utf-8') as orders_file:
        orders_string = json.dumps(orders, indent=4, ensure_ascii=False)
        # print(type(orders_string))
        orders_file.write(orders_string)


with open('orders.json', 'rb') as order_file:
    content = order_file.read()
    encoding = detect(content)['encoding']
write_order_to_json("Телефон", 2, 200, "Сан Саныч", "20.09.2022", encoding)
