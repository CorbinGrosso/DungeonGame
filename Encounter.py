from itertools import permutations
from Character import Character
import math
import random
from bullet import Bullet


# encounter_types = {
#     'battle': battle
# }

def get_move_order(players, enemies):
    """
    Calculates the order in which combatants move and returns a list in order of movement speed

    :param players: list of characters in the player's party
    :param enemies: list of enemies in the battle
    :type players: list[Character]
    :type enemies: list[Character]
    :return: list of list of combatants in order of greateset to least speed. 
            There will be multiple lists in the outer list if there are any speed ties between combatants
    :rtype: list[list[Character]]
    """

    combatants = players + enemies
    move_order = []
    while len(combatants) > 0:
        move_order.append(get_fastest_character(combatants))
        combatants.remove(move_order[-1])
    return move_order


def get_fastest_character(characters):
    """
    Returns the fastest character out of the characters provided.
    In the case of a  speed tie, it returns one at random.

    :param characters: list of characters to compare the speeds of
    :type characters: list[Characters]
    :return: character with the highest speed
    :rtype: Character
    """

    best = {
        'speed': 0,
        'Character': []
    }
    for character in characters:
        if character.speed > best['speed']:
            best['speed'] = character.speed
            best['Character'] = [character]
        elif character.speed == best['speed']:
            best['Character'].append(character)
    return random.choice(best['Character'])


def battle(players, enemies):
    while len(enemies) > 0:
        move_order = get_move_order(players, enemies)

        for character in move_order:
            if character.name == "Player":
                options = Bullet(prompt="What will you do?", choices=['Attack', 'Defend', 'Cast Spell', 'Talk', 'Inspect'])
                result = options.launch()
                if result == 'Attack':
                    print('You attack!')
                elif result == 'Talk':
                    options = Bullet(prompt="What will you talk about?", choices=['Weather', 'Compliment', 'Bully'])
                    result = options.launch()


battle([Character('Player', 10)], [Character('Skeleton', 2)])