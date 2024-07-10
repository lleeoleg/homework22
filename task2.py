"""
homework 22
"""
class Ship:
    """_summary_
    """
    def __init__(self, name, length, displacement):
        """_summary_

        Args:
            name (_type_): _description_
            length (_type_): _description_
            displacement (_type_): _description_
        """
        self.name = name
        self.length = length
        self.displacement = displacement
    def display_info(self):
        """_summary_
        """
        print(f"Ship: {self.name}")
        print(f"Length: {self.length} meters")
        print(f"Displacement: {self.displacement} tons")
class Frigate(Ship):
    """_summary_

    Args:
        Ship (_type_): _description_
    """
    def __init__(self, name, length, displacement, num_missiles):
        """_summary_

        Args:
            name (_type_): _description_
            length (_type_): _description_
            displacement (_type_): _description_
            num_missiles (_type_): _description_
        """
        super().__init__(name, length, displacement)
        self.num_missiles = num_missiles
    def display_info(self):
        """_summary_
        """
        super().display_info()
        print(f"Type: Frigate")
        print(f"Missiles: {self.num_missiles}")
class Destroyer(Ship):
    """_summary_

    Args:
        Ship (_type_): _description_
    """
    def __init__(self, name, length, displacement, num_guns):
        """_summary_

        Args:
            name (_type_): _description_
            length (_type_): _description_
            displacement (_type_): _description_
            num_guns (_type_): _description_
        """
        super().__init__(name, length, displacement)
        self.num_guns = num_guns
    def display_info(self):
        """_summary_
        """
        super().display_info()
        print(f"Type: Destroyer")
        print(f"Guns: {self.num_guns}")
class Cruiser(Ship):
    """_summary_

    Args:
        Ship (_type_): _description_
    """
    def __init__(self, name, length, displacement, num_missiles, num_guns):
        """_summary_

        Args:
            name (_type_): _description_
            length (_type_): _description_
            displacement (_type_): _description_
            num_missiles (_type_): _description_
            num_guns (_type_): _description_
        """
        super().__init__(name, length, displacement)
        self.num_missiles = num_missiles
        self.num_guns = num_guns
    def display_info(self):
        """_summary_
        """
        super().display_info()
        print(f"Type: Cruiser")
        print(f"Missiles: {self.num_missiles}")
        print(f"Guns: {self.num_guns}")

if __name__ == "__main__":
    frigate = Frigate("Frigate Alpha", 120, 3500, 48)
    destroyer = Destroyer("Destroyer Delta", 150, 5000, 64)
    cruiser = Cruiser("Cruiser Charlie", 180, 8000, 96, 88)
    frigate.display_info()
    print("--------------------")
    destroyer.display_info()
    print("--------------------")
    cruiser.display_info()
