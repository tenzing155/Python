    print(category['name'])
    for product in products:
        if category['id'] == product['category_id']:
            print(" \t",product['name'])
