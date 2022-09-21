import json
from random import randint
import sqlite3


def get_birth():
    return randint(1960, 2005)


persons = {
    "persons": [
        {
            "firstname": "pelle",
            "lastname": "svensson",
            "birth": get_birth(),
            "address": "stockholm 1",
        },
        {
            "firstname": "olle",
            "lastname": "svensson",
            "birth": get_birth(),
            "address": "goteborg 2",
        },
        {
            "firstname": "nisse",
            "lastname": "svensson",
            "birth": get_birth(),
            "address": "mamlo 3",
        },
        {
            "firstname": "hakan",
            "lastname": "mild",
            "birth": get_birth(),
            "address": "uppsala 4",
        },
        {
            "firstname": "thomas",
            "lastname": "brolin",
            "birth": get_birth(),
            "address": "linkoping 5",
        },
    ]
}
