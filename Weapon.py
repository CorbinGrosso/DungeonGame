class Weapon:
    """
    Weapon class. Every weapon has a name, a chance of being encountered, an attack stat, 
    and possibly a special effect with its own unique properties.
    """

    def __init__(self, name, base_probability, attack, effect=None):
        """
        Initializes an object of the Weapon class.

        :param name: Name of the weapon
        :param base_probability: Probability of being encountered at player level 1
        :param attack: Attack stat
        :param effect: Special effect of the weapon
        :type name: str
        :type base_probability: float
        :type attack: int
        :type effect: Effect
        """

        self.name = name
        self.attack = attack
