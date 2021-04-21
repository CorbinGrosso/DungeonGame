from itertools import permutations
from Character import Character


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
    possible_orders = [[]]
    iterations = len(combatants)
    for i in range(iterations):
        best = {
            'speed': 0,
            'Character': []
        }
        for combatant in combatants:
            if combatant.speed > best['speed']:
                best['speed'] = combatant.speed
                best['Character'] = [combatant]
            elif combatant.speed == best['speed']:
                best['Character'].append(combatant)
        possible_orders *= len(best['Character'])
        list_of_permutations = list(permutations(best['Character']))
        for i in range(len(possible_orders)):
            for character in list_of_permutations[i]:
                possible_orders[i].append(character.name)
        for character in best['Character']:
            combatants.remove(character)
    for possible_order in possible_orders:
        print(possible_order)


def battle(players, enemies):
    move_order = get_move_order(players, enemies)



players = [Character('fastest', 10), Character('slow', 1)]
enemies = [Character('Speedy', 10), Character('zoomer', 5)]
get_move_order(players, enemies)