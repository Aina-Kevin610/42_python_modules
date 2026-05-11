#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_factory.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: airandri <airandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/31 08:07:54 by airandri            #+#    #+#            #
#   Updated: 2026/03/31 09:48:42 by airandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._age = age
        self._height = height
        self.stat = self.Statistic()

    def show(self) -> str:
        self.stat.set_show()
        print (f"{self._name.capitalize()}: "
                f"{round(self._height, 1)}cm, {self._age} days old")

    def grow(self, h: float = 2.1) -> None:
        self.stat.set_grow()
        self._height += h

    def age_(self, day: int = 1) -> None:
        self.stat.set_age()
        self._age += day


    @staticmethod
    def check(age_: int) -> None:
        if age_ > 365:
            res = True
        else:
            res = False
        print(f"Is {age_} days more than a year? -> {res}")
    
    @classmethod
    def anonymous(cls) -> None:
        return cls("Unknown plant", 0.0, 0)
    
    class Statistic:
        def __init__(self, grow: int = 0, age: int = 0, show: int = 0) -> None:
            self._age = age
            self._show = show
            self._grow = grow

        def display(self) -> None:
            print(f"Stat: {self.get_grow()} grow,"
                f" {self.get_age()} age,"
                f" {self.get_show()} show")

        def set_grow(self) -> None:
            self._grow += 1

        def set_show(self) -> None:
            self._show += 1

        def set_age(self) -> None:
            self._age += 1

        def get_grow(self) -> int:
            return self._grow

        def get_age(self) -> int:
            return self._age

        def get_show(self) -> int:
            return self._show


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 age: int, color: str, blooming: bool):
        super().__init__(name, height, age)
        self._color = color
        self._blooming = blooming

    def show(self) -> None:
        super().show()
        print (f" Color: {self._color}") 
    
    def bloom(self) -> None:
        if self._blooming:
            print(f"{self._name.capitalize()} is blooming beautiffully!")
        else:
            print(f"{self._name.capitalize()} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str, blooming: bool, number_seed: int):
        super().__init__(name, height, age, color, blooming)
        self._number_seed = number_seed

    def show(self):
        self.stat.get_show()
        super().show()
        print(" Seeds: ", self._number_seed)
    
    def set_seed(self, seed) -> None:
        self._number_seed = seed


class Tree(Plant):
    class TreeStat:
        def __init__(self, grow: int = 0, age: int = 0, show: int = 0, shade: int = 0) -> None:
            self._age = age
            self._show = show
            self._grow = grow
            self._shade = shade

        def display(self) -> None:
            print(f"Stat: {self.get_grow()} grow,"
                f" {self.get_age()} age,"
                f" {self.get_show()} show"
                f"\n {self.get_shade()} shade")

        def set_grow(self) -> None:
            self._grow += 1

        def set_show(self) -> None:
            self._show += 1

        def set_age(self) -> None:
            self._age += 1

        def set_shade(self) -> int:
            self._shade += 1

        def get_grow(self) -> int:
            return self._grow

        def get_age(self) -> int:
            return self._age

        def get_show(self) -> int:
            return self._show
        
        def get_shade(self) -> int:
            return self._shade

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self.stat = self.TreeStat()

    def show(self):
        self.stat.get_show()
        super().show()
        print(" Trunk diameter: ", self._trunk_diameter, "cm")

    def produce_shade(self) -> None:
        self.stat.set_shade()
        if self._height >= 0:
            print(f"Tree {self._name.capitalize()} now produces a shade of "
                  f"{self._height}cm long and {self._trunk_diameter}cm wide.")
        else:
            print("Can't produce shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 nutri_val: int, harvest_season: str) -> None:
        super().__init__(name, height, age)
        self._nutri_val = nutri_val
        self._harvest_season = harvest_season

    def show(self) -> None:
        print (f"{self._name.capitalize()}: "
                f"{round(self._height, 1)}cm, "
                f"{self._age} days old \n"
                f" Harvest season: {self._harvest_season}\n"
                f" Nutritional Value: {self._nutri_val}")

    def grow_and_age(self, evo: int) -> None:
        i = 0
        while i < evo:
            super().grow()
            super().age_()
            self._nutri_val += 1
            i += 1


def display_stat(plant: Plant) -> None:
    print(f"[statistics for {plant._name.capitalize()}]")
    plant.stat.display()


if __name__ == "__main__":
    print ("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check(30)
    Plant.check(400)
    print("\n=== Flower")
    rose = Flower("rose", 15.0, 10, "red", False)
    rose.show()
    rose.bloom()
    display_stat(rose)
    print("[asking the rose to bloom]")
    rose._blooming = True
    rose.grow(8.0)
    rose.show()
    rose.bloom()
    display_stat(rose)
    print("\n=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    display_stat(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stat(oak)



    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", False, 0)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.age_(20)
    sunflower.grow(30)
    sunflower.set_seed(42)
    sunflower.bloom()
    sunflower.show()
    display_stat(sunflower)


    print("\n=== Anonymous")
    annonym = Plant.anonymous()
    annonym.show()
    display_stat(annonym)
    