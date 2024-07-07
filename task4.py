"""
homework 22
"""
class Wheels:
    """_summary_
    """
    def __init__(self, size, material):
        """_summary_

        Args:
            size (_type_): _description_
            material (_type_): _description_
        """
        self.size = size
        self.material = material
    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return f"Колеса: размер {self.size}, материал {self.material}"
class Engine:
    """_summary_
    """
    def __init__(self, horsepower, fuel_type):
        """_summary_

        Args:
            horsepower (_type_): _description_
            fuel_type (_type_): _description_
        """
        self.horsepower = horsepower
        self.fuel_type = fuel_type
    def __str__(self):
        """
        """
        return f"Двигатель: мощность {self.horsepower} л.с., тип топлива {self.fuel_type}"
class Doors:
    """_summary_
    """
    def __init__(self, number, opening):
        """_summary_

        Args:
            number (_type_): _description_
            opening (_type_): _description_
        """
        self.number = number
        self.opening = opening
    def __str__(self):
        """

        Returns:
            _type_: _description_
        """
        return f"Двери: количество {self.number}, тип открытия {self.opening}"

class Car(Wheels, Engine, Doors):
    """_summary_

    Args:
        Wheels (_type_): _description_
        Engine (_type_): _description_
        Doors (_type_): _description_
    """
    def __init__(self, make, model, year, wheel_size, wheel_material, horsepower, fuel_type, door_number, door_opening):
        """_summary_

        Args:
            make (_type_): _description_
            model (_type_): _description_
            year (_type_): _description_
            wheel_size (_type_): _description_
            wheel_material (_type_): _description_
            horsepower (_type_): _description_
            fuel_type (_type_): _description_
            door_number (_type_): _description_
            door_opening (_type_): _description_
        """
        Wheels.__init__(self, wheel_size, wheel_material)
        Engine.__init__(self, horsepower, fuel_type)
        Doors.__init__(self, door_number, door_opening)
        self.make = make
        self.model = model
        self.year = year
    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return f"Автомобиль: {self.year} {self.make} {self.model}, {self.horsepower} л.с., {self.fuel_type}, {self.size}\" {self.material}, {self.number} двери, {self.opening} открывание"

if __name__ == "__main__":
    my_car = Car("Toyota", "Camry", 2023, 18, "алюминий", 203, "бензин", 4, "обычное")
    print(my_car)
