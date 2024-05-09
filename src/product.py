class Product:
    """
    Класс для описания товара в магазине
    """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."
    @classmethod
    def new_product(cls, product : dict):
        """
        Класс-метод для создания нового продукта.
        """
        return cls(**product)

    @property
    def price(self):
        """
        Геттер для цены.
        """
        return self.__price

    @price.setter
    def price(self, new_price):
        """
        Сеттер для цены с проверкой.
        """
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
            return
        self.__price = new_price



if __name__ == "__main__":
    product_1 = Product("sambuka", "alko", 120.0, 12)
    print(product_1)
    print(product_1.name)
    print(product_1.description)
    print(product_1.price)
    print(product_1.quantity)

    product_data = {
        "name" : "vodka",
        "description" : "beer-vodka",
        "price" : 124.0,
        "quantity" : 13
    }
    product_2 = Product.new_product(product_data)
    print(product_2.name)
    print(product_2.price)
    print(product_2.quantity)
    product_2.price = -1
    print(product_2.price)

    print(product_1)
    print(product_2)

