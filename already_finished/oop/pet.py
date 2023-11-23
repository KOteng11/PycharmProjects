class Pet:
    allowed = ["cat", "dog", "fish", "rat"]

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet")
        self.name = name
        self.species = species


cat = Pet("blue", "cat")
dog = Pet("Wyatt", "dog")
tony = Pet("Billy", "tiger")
print(tony.species)
