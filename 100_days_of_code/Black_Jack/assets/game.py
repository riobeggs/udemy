from typing import Dict, Iterable, List

from .player import Player
from .errors import MethodNotImplemented


class Game:
    """The black jack game engine."""

    _players = {}       

    def __init__(self, *args):
        """Things to initialize when making a game class"""

        for item in args:
            if isinstance(item, Player):
                self.add_player(item)

    def add_player(self, player: Player) -> bool:
        """Add a player to the game."""
        assert isinstance(player, Player)

    def add_players(self, players: Iterable[Player]) -> bool:
        """Add multiple players to a game at once."""
        success = False
        for player in players:
            self._players[player._name] = player
        assert isinstance(players, Iterable)

        # add_player call this

        return success

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
    def introduction() -> None:
        """Print information about the Black Jack game"""

        logo = """
        .------.            _     _            _    _            _    
        |A_  _ |.          | |   | |          | |  (_)          | |   
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
        `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
              |  \/ K|                            _/ |                
              `------'                           |__/           
        """

        print(logo)

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
        winner = self._determine_winner()
        print(f"{winner} wins.")

    def play(self):
        """Play a game of Black Jack"""
        play = True
        while play:
            new_card = Player().draw_card()
            Player._hand.append(new_card)
            self.print_game_state
            if Player.is_bust():
                play = False


        self.print_game_end_information()
