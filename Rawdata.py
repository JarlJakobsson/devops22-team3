# Importing randint from random
from random import randint

# Method to randomize birth for our rawdata
def get_birth():
    return randint(1960, 2005)

# Our rawdata saved as a dict in persons, with 1 key, persons, that has a value of a list with dicts.
persons = {
    "persons": [
        {
            "firstname": "thomas",
            "lastname": "ravelli",
            "birthyear": get_birth(),
            "address": "stockholm 12",
        },
        {
            "firstname": "mats",
            "lastname": "sundin",
            "birthyear": get_birth(),
            "address": "kiruna 26",
        },
        {
            "firstname": "martin",
            "lastname": "dahlin",
            "birthyear": get_birth(),
            "address": "visby 31",
        },
        {
            "firstname": "hakan",
            "lastname": "mild",
            "birthyear": get_birth(),
            "address": "uppsala 43",
        },
        {
            "firstname": "thomas",
            "lastname": "brolin",
            "birthyear": get_birth(),
            "address": "huddinge 57",
        },
    ]
}
