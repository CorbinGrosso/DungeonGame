import math
import random


class Character:
    """
    Character class objects will record data on characters, including the player and enemies
    """

    # def __init__(self, name, level, hp, attack, defense, magic_attack, magic_dafense, movement_speed):
    def __init__(self, name, level, base_hp, base_attack, base_defense, base_magic, base_speed, weapon, armor, shield):
        """
        Initializes an object of the Player class.

        :param name: Name of the Character. Acts to identify the object
        :param level: Character's level. Player's increases throughout gameplay
        :param base_hp: Base HP stat
        :param base_attack: Base attack stat
        :param base_defense: Base defense stat
        :param base_magic: Base magic stat
        :param base_speed: Base speed stat
        :param weapon: Weapon that the Character is equipt with
        :param armor: Armor that the Character is equipt with
        :param shield: Shield that the Character is equipt with
        :type name: str
        :type level: int
        :type base_hp: int
        :type base_attack: int
        :type base_defense: int
        :type base_magic: int
        :type base_speed: int
        :type weapon: Weapon
        :type armor: Armor
        :type shield: Shield
        """

        self.__name = name
        self.__level = level
        self.__base_hp = base_hp
        self.__base_attack = base_attack
        self.__base_defense = base_defense
        self.__base_magic = base_magic
        self.__base_speed = base_speed
        self.__weapon = weapon
        self.__armor = armor
        self.__shield = shield

        self.__update_hp()
        self.__update_attack()
        self.__update_defense()
        self.__update_magic()
        self.__update_speed()


    def get_name(self):
        """
        Gets the name of the Character

        :return: Character's name
        :rtype: str
        """

        return self.__name


    def get_level(self):
        """
        Gets the Character's level

        :return: Character's level
        :rtype: int
        """

        return self.__level
        

    def get_max_hp(self):
        """
        Gets the current HP stat of the Character

        :return: current HP stat
        :rtype: int
        """

        return self.__max_hp
        

    def get_current_hp(self):
        """
        Gets the current HP stat of the Character

        :return: current HP stat
        :rtype: int
        """

        return self.__current_hp


    def get_attack(self):
        """
        Gets the attack stat of the Character

        :return: attack stat
        :rtype: int
        """

        return self.__attack


    def get_defense(self):
        """
        Gets the defense stat of the Character

        :return: defense stat
        :rtype: int
        """

        return self.__defense


    def get_magic(self):
        """
        Gets the magic stat of the Character

        :return: defense stat
        :rtype: int
        """

        return self.__magic


    def get_speed(self):
        """
        Gets the speed stat of the Character

        :return: speed stat
        :rtype: int
        """

        return self.__speed


    def get_weapon(self):
        """
        Gets the weapon equipt by the Character

        :return: Character's weapon
        :rtype: Weapon
        """

        return self.__weapon


    def get_armor(self):
        """
        Gets the armor equipt by the Character

        :return: Character's armor
        :rtype: Armor
        """

        return self.__armor


    def get_shield(self):
        """
        Gets the armor equipt by the Character

        :return: Character's shield
        :rtype: Shield
        """
        
        return self.__shield


    def __increase_level(self):
        """
        Increases Character's level by 1
        """

        self.__level += 1

    
    def __update_hp(self):
        """
        Recalculates the Character's HP stat
        """

        prev_max_hp = self.__max_hp

        self.__max_hp = math.ceil(self.__base_hp + self.__base_hp * self.__level / 25)
        if self.__current_hp == None:
            self.__current_hp = self.__max_hp
        else:
            self.__current_hp += self.__max_hp - prev_max_hp

    
    def __update_attack(self):
        """
        Recalculates the Character's attack stat
        """

        self.__attack = math.ceil(self.__base_attack * self.__level / 25)
        if self.__weapon is not None:
            self.__attack += self.__weapon.get_attack()


    def __update_defense(self):
        """
        Recalculates the Character's defense stat
        """

        self.__defense = math.ceil(self.__base_defense * self.__level / 25)
        if self.__armor is not None:
            self.__defense += self.__armor.get_defense()


    def __update_magic(self):
        """
        Recalculates the Character's magic stat
        """

        self.__magic = math.ceil(self.__base_magic * self.__level / 25)
        if self.__weapon is not None:
            self.__magic += self.__weapon.get_magic()


    def __update_speed(self):
        """
        Recalculates the Character's speed stat
        """

        self.__speed = math.ceil(self.__base_speed * self.__level / 25)
        if self.__armor is not None:
            self.__speed += self.__armor.get_speed()


    def level_up(self):
        """
        Levels up the Character by increasing its level and updating all its stats
        """
    
        self.__increase_level()
        self.__update_hp()
        self.__update_attack()
        self.__update_defense()
        self.__update_magic()
        self.__update_speed()


    def print_stats(self):
        """
        Prints out the Character's stats
        """

        print(f"Name: {self.__name}")
        print(f"Level: {self.__level}")
        print(f"HP: {self.__current_hp} / {self.__max_hp}")
        print(f"Attack: {self.__attack}")
        print(f"Defense: {self.__defense}")
        print(f"Magic: {self.__magic}")
        print(f"Speed: {self.__speed}")


    def attack(self, opponent):
        """
        The Character attacks their opponent, dealing damage based on the attacker's attack stat and
        the opponent's defense stat, reducing the opponent's current HP by the calculated amount.

        :param opponent: Target being attacked
        :type opponent: Character
        """

        damage = math.ceil(self._attack / opponent.get_defense() * 10)
        opponent.take_damage(damage)


    def take_damage(self, damage):
        """
        Damages the Character by reducing their current HP by the damage they have received.
        Does not allow for negative current HP.

        :param damage: Amount of damage that has been dealt to the Character
        :type damage: int
        """

        if self.__current_hp < damage:
            self.__current_hp = 0
        else:
            self.__current_hp -= damage

    
    def block_attack(self):
        """
        If the Character is holding a shield, allows for the chance to block an incoming attack.

        :return: If the Character successfully blocked the attack
        :rtype: bool
        """

        if self.__shield is not None:
            block_chance = self.__shield.get_block_chance()
            if random.random() <= block_chance:
                return True
        return False


# person = Character('player', 1, 1, 1, 1, 1, 1, 1)
# print(person.get_name())