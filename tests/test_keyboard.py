from src.keyboard import KeyBoard

kb = KeyBoard('Клавиатура', 10000, 10)

def test_str():

    assert str(kb.language) == "EN"

def test_change_lang():

    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"


