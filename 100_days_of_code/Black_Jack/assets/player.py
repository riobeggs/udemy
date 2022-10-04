from assets.constants import Game as GameConstants, Player as PlayerConstants
from assets.errors import MethodNotImplemented
import random


class Player:
    """A black jack player"""

    # Private attributes about a player. Expose them using properties
    _hand = None
    _stand: bool = False
    _is_computer: bool = False
    _is_dealer = False
    _name = None

    def __init__(
        self, name=PlayerConstants.COMPUTER_NAME, is_computer=False, is_dealer=False
    ):
        """Initialize a player."""
        self._name = name
        self._is_dealer = is_dealer
        self._is_computer = is_computer
        self._hand = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def stand(self) -> bool:
        """
        Getter for the stand property.

        This will be used to determine if a player has stood up from the hand.
        They will not be dealt more cards if this is true.

        Use this pattern to expose attributes about the class.

        Example:
            if not Player.stand:
                draw_card()
        """
        return self._stand

    @stand.setter
    def stand(self, state_to_set: bool):
        """Setter for the stand property"""
        assert isinstance(state_to_set, bool)
        self._stand = state_to_set

    @property
    def is_bust(self) -> bool:
        """Used to check if a player has gone bust"""
        return self.get_score() > GameConstants.PERFECT_SCORE

    @property
    def _should_draw(self) -> bool:
        """Logic used by the computer to determine if they should draw."""
        raise MethodNotImplemented()

    def get_score(self) -> int:
        """Returns the score of the players hand."""
        score = sum(self._hand)
        return score

    def deal_card(self, card: int):
        """Draw a card."""
        self._hand.append(card)

    def show_hand(self):
        """prints players name and hand"""
        if not self._is_dealer:
            print(f"{self._name} hand = {self._hand}")
        else:
            print(f"{self._name} hand = [{self._hand[0]}, ?]")