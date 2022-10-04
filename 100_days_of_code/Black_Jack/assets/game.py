import random
from typing import Dict, Iterable, List
from urllib import response

from assets.player import Player
from assets.errors import MethodNotImplemented


class Game:
    """The black jack game engine."""
    
    VALID_RESPONSES = ("hit", "stand")
    _players = {}       

    def __init__(self, *args):
        """Things to initialize when making a game class"""

        for item in args:
            if isinstance(item, Player):
                self.add_player(item)

    def add_player(self, player: Player) -> bool:
        """Add a player to the game."""
        # TODO: account for 2 players with same name
        self._players[player._name] = player

    def add_players(self, players: Iterable[Player]) -> bool:
        """Add multiple players to a game at once."""
        success = False
        assert isinstance(players, Iterable)
        for player in players:
            self.add_player(player)

        return success

    def deal_cards(self) -> None:
        """Deal cards to each player in the game."""
        for name in self._players:
            for _ in range(2):
                self.deal_card(name)

        pass

    def deal_card(self, name: str):
        """deals a card to a player"""
        player = self._players[name]
        card = self.draw_card()
        player.deal_card(card)
            
    @staticmethod
    def draw_card() -> int:
        """Draws a card"""
        available_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        distributed_card = random.choice(available_cards)
        return distributed_card

    def print_game_state(self) -> None:
        """Prints the current game state of each player."""
        for name in self._players:
            player = self._players[name]
            player.show_hand()

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

    def ask_if_hit(self) -> str:
        """ask if player wants to hit"""
        response = input("Would you like to stand or hit?: ").lower()
        while response not in self.VALID_RESPONSES:
            response = input("Would you like to stand or hit?: ").lower()

        return response

    def play(self):
        """Play a game of Black Jack"""
        play = True
        while play:
            self.deal_cards()
            self.print_game_state()
            players = [player for _, player in self._players.items() if not player._is_dealer]
            for player in players:
                while not player.is_bust and self.ask_if_hit() == "hit":
                    self.deal_card(player.name)
                    self.print_game_state()
                play = False

        self.print_game_end_information()
