
from electronics_shop.src.item import Item


class MixinLanguage:

    def __init__(self):
        self.language = "EN"


    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
            return self.language
        else:
            return self.language


class Keyboard(Item, MixinLanguage):
    pass
