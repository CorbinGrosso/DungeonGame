class Character:
    """
    Character class objects will record data on characters, including the player and enemies
    """

    # def __init__(self, name, level, hp, attack, defense, magic_attack, magic_dafense, movement_speed):
    def __init__(self, name, speed):
        """
        Initializes an object of the Player class.
        """

        self.name = name
        self.speed = speed


