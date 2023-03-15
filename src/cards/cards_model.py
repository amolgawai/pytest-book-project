"""Data Model for Cards App"""
from __future__ import annotations
from dataclasses import dataclass, field, asdict


@dataclass
class Card:
    """Represents a todo cards"""

    description: str = ""
    owner: str = ""
    status: str = "todo"
    id: int = field(default=0, compare=False)

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
