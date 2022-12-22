from cards.cards_model import Card


def test_cards_member_access():
    a_card = Card(description="A todo", owner="someone", id=123)
    assert a_card.description == "A todo"
    assert a_card.owner == "someone"
    assert a_card.status == "todo"
    assert a_card.id == 123
