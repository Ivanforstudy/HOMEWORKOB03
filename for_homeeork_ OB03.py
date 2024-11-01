
import json

class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def to_dict(self):
        return {
            'name': self.name,
            'species': self.species,
            'age': self.age
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['species'], data['age'])

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump([animal.to_dict() for animal in self.animals], f)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                animal_data = json.load(f)
                self.animals = [Animal.from_dict(data) for data in animal_data]
        except FileNotFoundError:
            print(f"Файл {filename} не найден. Создан новый зоопарк.")
            self.animals = []

    def show_animals(self):
        for animal in self.animals:
            print(f"{animal.name} - {animal.species}, {animal.age} лет")

if __name__ == "__main__":
    zoo = Zoo()
    zoo.load_from_file('zoo_data.json')


    zoo.add_animal(Animal("Орел", "Птица", 5))
    zoo.add_animal(Animal("Тигр", "Млекопитающее", 3))


    zoo.show_animals()


    zoo.save_to_file('zoo_data.json')



1