from time import sleep

from data import data_loading
from game.game import run


def main():
    actions = data_loading.load_action_sequence('check_door_key_interaction')
    action_delay = .05
    input_delay = .5

    def get_action_from_sequence():
        sleep(action_delay)
        a = actions.get()
        return a

    def empty_input(prompt):
        print(prompt)
        sleep(input_delay)
        return

    run(get_action_from_sequence, empty_input)


if __name__ == '__main__':
    main()
