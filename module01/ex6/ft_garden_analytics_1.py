#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_analytics.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: airandri <airandri@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/01 12:39:20 by airandri            #+#    #+#            #
#   Updated: 2026/04/01 16:25:30 by airandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    class Statistical:
        def __init__(self) -> None:
            self._grow_call = 0
            self._age_call = 0
            self._show_call = 0

        def display(self) -> None:
            print(f"Stats: {self.get_grow_call()} grow, "
                  f"{self.get_age_call()} age, "
                  f"{self.get_show_call()} show")

        def get_grow_call(self) -> int:
            return self._grow_call

        def get_age_call(self) -> int:
            return self._age_call

        def get_show_call(self) -> int:
            return self._show_call

        def set_age_call(self) -> None:
            self._age_call += 1

        def set_grow_call(self) -> None:
            self._grow_call += 1

        def set_show_call(self) -> None:
            self._show_call += 1

    def __init__(self,
                 name: str,
                 Height: float,
                 Age: int) -> None:
        self.name = name
        self.Height = round(Height, 1)
        self.Age = Age
        self._statistical = Plant.Statistical()

    def show(self) -> None:
        self._statistical.set_show_call()
        print(f"{self.name}: {self.Height:.1f}cm, {self.Age} days old")

    def grow(self, growth: float = 0) -> None:
        self._statistical.set_grow_call()
        self.growth = growth
        self.Height = round((self.Height + growth), 1)

    def age(self, day: int = 0) -> None:
        self._statistical.set_age_call()
        self.day = day
        self.Age += day

    @staticmethod
    def Check_year_old(age: int) -> None:
        if (age > 365):
            result_bool = True
        else:
            result_bool = False
        print(f"Is {age} days more than a year? -> {result_bool}")

    @classmethod
    def created_anonymous(cls,
                          name: str = "Unknown plant",
                          Heigth: float = 0,
                          Age: int = 0) -> "Plant":
        plant = cls(name, Heigth, Age)
        return plant


class Flower(Plant):
    def __init__(self,
                 name: str,
                 Height: float,
                 Age: int,
                 color: str) -> None:
        super().__init__(name, Height, Age)
        self.color = color

    def bloom(self, blooming: bool = False) -> None:
        if blooming is False:
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!")

    def show_flower(self) -> None:
        super().show()
        print(f" Color: {self.color}")


class Tree(Plant):
    class Statistical_Tree(Plant.Statistical):
        def __init__(self) -> None:
            super().__init__()
            self._produce_shade_call = 0

        def display(self) -> None:
            super().display()
            print(f" {self.get_produce_shade_call()} shade")

        def get_produce_shade_call(self) -> int:
            return self._produce_shade_call

        def set_produce_shade_call(self) -> None:
            self._produce_shade_call += 1

    def __init__(self,
                 name: str,
                 Height: float,
                 Age: int,
                 trunk_diameter: int) -> None:
        super(). __init__(name, Height, Age)
        self.trunk_diameter = trunk_diameter
        self._statistical: Tree.Statistical_Tree = self.Statistical_Tree()

    def produce_shade(self) -> None:
        self._statistical.set_produce_shade_call()
        print(f"Tree {self.name} now produces a shade of "
              f"{self.Height:.1f}cm long and "
              f"{self.trunk_diameter:.1f}cm wide.")

    def show_tree(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self,
                 name: str,
                 Height: float,
                 Age: int,
                 harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, Height, Age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show_vegetable(self) -> None:
        self.show()
        print(f" Harvest season: {self.harvest_season}"
              f" Nutritional value: {self.nutritional_value}")

    def grow_and_age(self) -> None:
        print(f"[make {self.name} grow and age for 20 days]")
        for i in range(0, 20):
            super().grow()
            super().age()
            self.nutritional_value += 1


class Seed(Flower):
    def __init__(self,
                 name: str,
                 Height: float,
                 Age: int,
                 color: str):
        super().__init__(name, Height, Age, color)
        self.seed = 0

    def show_seed(self, blooming: bool = False) -> None:
        super().show()
        print(f" Color: {self.color}")
        super().bloom(blooming)
        print(f" Seeds: {self.seed}")

    def make(self) -> None:
        print(f"[make {self.name} grow, age and bloom]")
        self.seed += 42
        self.grow(30)
        self.age(20)


def displays_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant._statistical.display()


def ft_plant_types() -> None:
    print("=== Check year-old")
    Plant.Check_year_old(30)
    Plant.Check_year_old(400)
    print()
    print("=== Flower")
    flower = Flower("Rose", 15, 10, "red")
    flower.show_flower()
    flower.bloom()
    displays_statistics(flower)
    print("[asking the rose to grow and bloom]")
    flower.grow(8)
    flower.show_flower()
    flower.bloom(True)
    displays_statistics(flower)
    print()
    print("=== Tree")
    tree = Tree("Oak", 200, 365, 5)
    tree.show_tree()
    displays_statistics(tree)
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    displays_statistics(tree)
    print()
    print("=== Seed")
    seed_flower = Seed("Sunflower", 80, 45, "yellow")
    seed_flower.show_seed()
    seed_flower.make()
    seed_flower.show_seed(True)
    displays_statistics(seed_flower)
    print()
    print("=== Anonymous")
    anonymous = Plant.created_anonymous()
    anonymous.show()
    displays_statistics(anonymous)


if __name__ == "__main__":
    print("=== Garden statistics ===")
    ft_plant_types()
