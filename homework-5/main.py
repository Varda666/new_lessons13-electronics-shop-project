from electronics_shop.src.keyboard import Keyboard, MixinLanguage

if __name__ == '__main__':
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"

    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    # Сделали RU -> EN -> RU
    for i in range(2):
        kb.change_lang()
    print(kb.change_lang())
    assert str(kb.language) == "RU"

    kb.language = 'CH'
    # AttributeError: property 'language' of 'Keyboard' object has no setter
