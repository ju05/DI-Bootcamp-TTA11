class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
    
    def add_animals(self, *new_animal):
        if new_animal not in self.animals:
            self.animals.extend(new_animal)
        print(self.animals)

    def sort_animals(self):
        '''sorts the animals alphabetically and groups them together based on their first letter.'''
        self.animals.sort()
        groups = {}
        for animal in self.animals:
            first_letter = animal[0]
            if first_letter not in groups:
                groups[first_letter] = [animal]
            else:
                groups[first_letter].append(animal)
                   
        return groups
    
    def get_groups(self):
        groups = self.sort_animals()
        # groups_dict = {i+1 : groups[group] for i, group in enumerate(groups)}

        groups_dict = {}
        for i, group in enumerate(groups):
            if len(group) > 1:
                new_group = {i+1 : groups[group]}
                groups_dict.update(new_group)
            else:
                single_animal = ''.join(group)
                {i+1 : single_animal}
        print(f' groups: {groups_dict}')


        # return groups_dict

            

ramat_gan_safari = Zoo('Safari Ramat Gan')
ramat_gan_safari.add_animals('Turtle', 'Elephant', 'Emma', 'Appe', 'Avestruz')
print(ramat_gan_safari.sort_animals())
ramat_gan_safari.get_groups()