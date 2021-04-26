class Weapon:
    """
    Weapon class. Every weapon has a name, a chance of being encountered, an attack stat, 
    and possibly a special effect with its own unique properties.
    """

    def __init__(self, name, attack, magic, effect, description):
        """
        Initializes an object of the Weapon class.

        :param name: Name of the weapon
        :param base_probability: Probability of being encountered at player level 1
        :param attack: Attack stat
        :param magic: Magic stat
        :param effect: Special effect of the weapon
        :param description: Description of the weapon
        :type name: str
        :type base_probability: float
        :type attack: int
        :type magic: int
        :type effect: Effect
        :type description: str
        """

        self.__name = name
        self.__attack = attack
        self.__magic = magic
        self.__effect = effect
        self.__description = description


    def get_name(self):
        """
        Gets the name of the Weapon

        :return: Weapon's name
        :rtype: str
        """

        return self.__name


    def get_attack(self):
        """
        Gets the Weapon's attack stat

        :return: attack stat
        :rtype: int
        """

        return self.__attack


    def get_magic(self):
        """
        Gets the Weapon's magic stat

        :return: magic stat
        :rtype: int
        """

        return self.__magic


    def get_effect(self):
        """
        Gets the special effect of the Weapon

        :return: Weapon's special effect
        :rtype: Effect
        """

        return self.__effect


    def get_description(self):
        """
        Gets the description of the Weapon

        :return: Weapon's description
        :rtype: str
        """

        return self.__description

