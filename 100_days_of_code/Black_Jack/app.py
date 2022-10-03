# The main game file we will use.

from assets.game import Game
from assets.player import Player


def main():
    """Run the game engine."""
    computer = Player(is_dealer=True, is_computer=True)
    player = Player(name="Rio")
    players = [computer, player]
    game = Game()
    game.add_players(players)
    game.introduction()
    game.play()

if __name__ == "__main__":
    main()