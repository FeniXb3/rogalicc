from game.game import run
from player_interaction.player_input import get_action_by_key


def main():
    run(get_action_by_key, input)


if __name__ == "__main__":
    main()
