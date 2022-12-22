"""Data Model for Cards App"""
from dataclasses import dataclass, field, asdict


@dataclass
class Card:
    """Represents a todo cards"""

    description: str = None
    owner: str = None
    status: str = "todo"
    id: int = field(default=None, compare=False)

    @classmethod
    def from_dict(cls, a_dict: dict) -> Card:
        """Creates a card by reading fields from a dictionary

        Args:
            a_dict (dict): Dictionary with all the fields

        Returns:
            Card: Card filled with the fields
        """
        return Card(**a_dict)

    def to_dict(self) -> dict:
        """Returns dictionary representation of card

        Returns:
            dict: dictionary filled from the Card
        """
        return asdict(self)
