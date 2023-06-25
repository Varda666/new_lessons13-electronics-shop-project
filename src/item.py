import csv



class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []




    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)


        @property
        def name(self):
            return self.__name

        @name.setter
        def name(self, name: str):
            if len(name) <= 10:
                self.__name = name
            else:
                self.__name = name[:10]


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price_for_all_products = self.price * self.quantity
        return total_price_for_all_products

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        discounted_price = self.price * self.pay_rate
        return discounted_price

    @classmethod
    def instantiate_from_csv(cls):
        """класс-метод, инициализирующий экземпляры класса `Item` данными из файла"""
        with open("..\\src\\items.csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item_string = f'{row["name"]} {row["price"]} {row["quantity"]}'
                name, price, quantity = item_string.split(' ')
                return cls(name, price, quantity)

    @staticmethod
    def string_to_number(number_str):
        """статический метод, возвращающий число из числа-строки"""
        if '.' in number_str:
            int_part, fract_part = number_str.split('.')
            return int(int_part)
        else:
            return int(number_str)





