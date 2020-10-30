import random 


animal_attributes = {
    'cat': ['popular pet', 'says "Meow"'],
    'dog': [],   # empty list is a valid list 
    'bird': ['has feathers', 'usually can fly']
}


def get_animals():
    return list(animal_attributes.keys())


def get_attributes(animal):

    """ Returns a list of attributes for an animal.
    Return list of attributes for animal
    Returns empty list if no attributes 
    Returns None if animal not found
    Raises Exception if connection fails (pretend this is calling to an API)
     """

    # randomly fail one-third of the time to mimic connection loss. 
    # obviously you would not do this in your code.
    if random.randint(1, 3) == 1:
        raise Exception('Pretend no connection error')

    if animal not in animal_attributes:
        return None 
    return animal_attributes[animal]
    

def like(animal):
    # pretend this is a method that saves/updates a database 
    # obviously you would not do this in your code.
    if random.randint(1, 3) == 1:
        raise Exception('Pretend database error')

    # return True if animal is one of the options, False otherwise 
    return animal in animal_attributes
        

    