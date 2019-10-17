def price(product):

    price_of_products = {
        "shoe": 400,
        "brush": 30,
        "shirt": 1000,
        "t-shirt": 450,
        "pant": 900
    }

    return price_of_products.get(product)
