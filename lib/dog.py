#!/usr/bin/env python3
import ipdb 

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self,name="loki", breed="Mastiff"):
        # if (type(name) == str) and (1 <= len(name) <= 25):
        self.name = name
        self.breed = breed
        # else: print("Name must be string between 1 and 25 characters.")   
        # if breed in APPROVED_BREEDS:
        #     self.breed == breed
        # else: print("Breed must be in list of approved breeds.")
        # def get_breed(self):
        # return self._breed
   

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
    breed = property(get_breed, set_breed)
