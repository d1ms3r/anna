from src.product import Product
class Category:
    """
    Класс для категорий товара
    """
    name: str
    description: str
    products: list  # Используем приватный атрибут для хранения списка товаров
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else [] # Инициализируем приватный атрибут
        # Увеличиваем счетчики при создании нового объекта
        Category.category_count += 1 # ?
        Category.product_count += len(self.__products)  # ? Category need?

    @property
    def products(self):
        """
        Геттер для просмотра списка товаров в категории.
        """
        #v vidose через итерацию
        product_str = ""
        for item in self.__products:
            product_str += f"{self.name}, {self.__price} руб., Остаток: {self.quantity} шт.\n"
        return product_str

    @products.setter
    def products(self, new_product):
        """
        Специальный метод для добавления товара в категорию.
        """
        self.__products.append(new_product)  # Используем приватный атрибут для добавления товара
        Category.category_count += 1 # счетчик

    @property
    def product_in_list(self):
        """
        Публичный геттер для доступа к приватному атрибуту _products.
        """
        return self.__products

#проверка через иф нейм