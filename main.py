#                           Home Task 4

# Task 1
# Модифицируйте первое домашнее задание (О заказе),
# добавив проверки в методы классов и обработку исключительных ситуаций. При попытке установить отрицательную или
# нулевую стоимость товара следует вызвать исключительную ситуацию, тип которой реализовать самостоятельно.


# Task 2
# Модифицируйте второе домашнее задание (Дисконт) добавив проверки в методы классов и обработку исключительных ситуаций.
# При попытке установить скидку не в пределах 0-100% - следует вызвать исключительную ситуацию,
# тип которой реализовать самостоятельно.


class Product:
    """
    Product class
    :param name: product name
    :param price: product price
    :param quantity: product quantity
    """
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

        if self.price <= 0:
            raise ValueError('Price must be greater than 0')

        if self.quantity <= 0:
            raise ValueError('Quantity must be greater than 0')

    def __str__(self):
        """
        Returns product info
        """
        return f"{self.name}: {self.price * self.quantity}"

    def apply_discount(self, discount_percentage):
        """
        Applies discount to the product
        :param discount_percentage:
        """
        try:
            if discount_percentage > 0 or discount_percentage <= 100:
                discount_factor = 1 - discount_percentage / 100
                self.price *= discount_factor
        except ValueError as err:
            print(err)


class Order:
    """
    Order class
    :param products: list of products
    """
    def __init__(self, products):
        self.products = products

    def get_total_sum(self):
        """
        Returns total sum of the order
        """
        self.total_sum = 0
        for product in self.products:
            self.total_sum += product.price * product.quantity
        return self.total_sum


try:
    products = [Product('apple', 10, 2),
                Product('banana', 20, 5),
                Product('orange', 30, 4)]

    order = Order(products)

    for product in products:
        product.apply_discount(15)

    print("Products in the order:")
    for product in products:
        print(product)

    print("\nTotal Order Cost (after discount):", order.get_total_sum())

    invalid_discount_product = Product('invalid_discount_product', 50, 3)
    invalid_discount_product.apply_discount(120)

except ValueError as err:
    print(err)

