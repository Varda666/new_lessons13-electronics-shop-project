from electronics_shop.src.item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, sim_quantity: int):
        """`Phone` содержит все атрибуты класса `Item` и дополнительно атрибут, содержащий количество поддерживаемых сим-карт"""
        super().__init__(name, price, quantity)
        self.sim_quantity = sim_quantity

    def __repr__(self):
        super().__repr__()
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.sim_quantity})"

    def __add__(self, other):
        """Складывает экземпляры класса `Phone` и `Item` по количеству товара в магазине"""
        if isinstance(other, (Phone, Item)):
            return self.quantity + other.quantity
