from src.cards.cards_model import Card


def test_cards_member_access():
    a_card = Card(description="A todo", owner="someone", id=123)
    assert a_card.description == "A todo"
    assert a_card.owner == "someone"
    assert a_card.status == "todo"
    assert a_card.id == 123


def test_card_defaults():
    a_card = Card()
    assert a_card.description == None
    assert a_card.owner == None
    assert a_card.status == "todo"
    assert a_card.id == None


def test_equality():
    card1 = Card(description="A todo", owner="Roy", id=111)
    card2 = Card(description="A todo", owner="Roy", id=111)
    assert card1 == card2


def test_equality_different_ids():
    card1 = Card(description="A todo", owner="Roy", id=111)
    card2 = Card(description="A todo", owner="Roy", id=222)
    assert card1 == card2
