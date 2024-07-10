"""
homework 22
"""
class Device:
    """_summary_
    """
    def __init__(self, year, manufacturer):
        """_summary_

        Args:
            year (_type_): _description_
            manufacturer (_type_): _description_
        """
        self.year = year
        self.manufacturer = manufacturer
    def set_year(self, year):
        """_summary_

        Args:
            year (_type_): _description_
        """
        self.year = year
    def get_year(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.year
    def set_manufacturer(self, manufacturer):
        """_summary_

        Args:
            manufacturer (_type_): _description_
        """
        self.manufacturer = manufacturer
    def get_manufacturer(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.manufacturer
class CoffeeMachine(Device):
    """_summary_

    Args:
        Device (_type_): _description_
    """
    def __init__(self, year, manufacturer, color, energy):
        """_summary_

        Args:
            year (_type_): _description_
            manufacturer (_type_): _description_
            color (_type_): _description_
            energy (_type_): _description_
        """
        super().__init__(year, manufacturer)
        self.color = color
        self.energy = energy
    def set_color(self, color):
        """_summary_

        Args:
            color (_type_): _description_
        """
        self.color = color
    def get_color(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.color
    def set_energy(self, energy):
        """_summary_

        Args:
            energy (_type_): _description_
        """
        self.energy = energy
    def get_energy(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.energy
class Blender(Device):
    """_summary_

    Args:
        Device (_type_): _description_
    """
    def __init__(self, year, manufacturer, color, energy):
        """_summary_

        Args:
            year (_type_): _description_
            manufacturer (_type_): _description_
            color (_type_): _description_
            energy (_type_): _description_
        """
        super().__init__(year, manufacturer)
        self.color = color
        self.energy = energy
    def set_color(self, color):
        """_summary_

        Args:
            color (_type_): _description_
        """
        self.color = color
    def get_color(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.color
    def set_energy(self, energy):
        """_summary_

        Args:
            energy (_type_): _description_
        """
        self.energy = energy
    def get_energy(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.energy
class MeatGrinder(Device):
    """_summary_

    Args:
        Device (_type_): _description_
    """
    def __init__(self, year, manufacturer, color, energy):
        """_summary_

        Args:
            year (_type_): _description_
            manufacturer (_type_): _description_
            color (_type_): _description_
            energy (_type_): _description_
        """
        super().__init__(year, manufacturer)
        self.color = color
        self.energy = energy
    def set_color(self, color):
        """_summary_

        Args:
            color (_type_): _description_
        """
        self.color = color
    def get_color(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.color
    def set_energy(self, energy):
        """_summary_

        Args:
            energy (_type_): _description_
        """
        self.energy = energy
    def get_energy(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.energy

if __name__ == "__main__":
    print("Main class")
    main_device = Device("2016", "Samsung")
    main_device.set_year("2016")
    print(main_device.get_year())
    main_device.set_manufacturer("Samsung")
    print(main_device.get_manufacturer())
    print("-------------")
    print("Coffee Machine class")
    child_cm = CoffeeMachine("2020", "Xiaomi", "Black", "190w")
    print(child_cm.get_year())
    print(child_cm.get_manufacturer())
    print(child_cm.get_color())
    print(child_cm.get_energy())
    print("-------------")
    print("Meat Grinder class")
    child_mg = MeatGrinder("2022", "Bosch", "White", "220w")
    print(child_mg.get_year())
    print(child_mg.get_manufacturer())
    print(child_mg.get_color())
    print(child_mg.get_energy())
    print("-------------")
    print("Blender class")
    child_mg = MeatGrinder("2021", "LG", "Blue", "220w")
    print(child_mg.get_year())
    print(child_mg.get_manufacturer())
    print(child_mg.get_color())
    print(child_mg.get_energy())
