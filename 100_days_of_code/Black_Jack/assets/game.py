from typing import Iterable, List

from .constants import Game as Constants
from .errors import MethodNotImplemented
from .player import Player


class Game:
    """The black jack game engine."""

    _players: List[Player] = []

    def __init__(self, *args):
        """Things to initialize when making a game class"""
        for item in args:
            if isinstance(item, Player):
                self.add_player(item)
                

    def add_player(self, player: Player) -> bool:
        """Add a player to the game. """
        assert isinstance(player, Player)

    def add_players(self, players: Iterable[Player]) -> bool:
        """Add multiple players to a game at once."""
        success = False
        
        assert isinstance(players, Iterable)

        for player in players:
            assert isinstance(player, Player)
            self._players.append(player)

        success = True

        return success

    def get_players(self) -> None:
        """Prints the players in the game."""
        for player in self._players:
            print(player)

    def deal_cards(self) -> None:
        """Deal cards to each player in the game."""
        raise MethodNotImplemented()

    def deal_card(self, player: Player) -> None:
        """Deal a card to a single player."""
        raise MethodNotImplemented()

    def print_game_state(self) -> None:
        """Prints the current game state of each player."""
        raise MethodNotImplemented()

    @staticmethod
    def introduction():
        """Print information about the Black Jack game"""
        print(Constants.LOGO)

    def play(self):
        """Play a game of Black Jack"""
        play = True
        while play:
            raise MethodNotImplemented()

    def restart(self):
        """Reset the game of Black Jack"""
        raise MethodNotImplemented()

    def _determine_winner(self) -> Player:
        """
        Internal method to determine who won the game.
        
        Returns the winning player.
        """
        raise MethodNotImplemented()

    def print_game_end_information(self) -> None:
        """
        Prints the winner of the game to the console.
        Might also print the sate of the game to the console.
        """
        raise MethodNotImplemented()
