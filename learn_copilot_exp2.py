#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass
"""
This module defines a `Person` class using the `dataclass` decorator.
Classes:
    Person: A class representing a person with a first name, last name, and birthdate.
Methods:
    age(self) -> int:
        Calculates the age of the person in years based on the current date.
    full_name(self) -> str:
        Returns the full name of the person by combining the first name and last name.
Example:
    print(p.full_name)  # Output: John Doe
    print(p.age())      # Output: Age in years
"""
from datetime import date

@dataclass
class Person:
    first_name: str
    last_name: str
    birthdate: date
    
    def age(self):
        today = date.today()
        return (today.year - self.birthdate.year - 
                ((today.month, today.day) < (self.birthdate.month, self.birthdate.day)))
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

 
p = Person("John", "Doe", date(2000, 1, 1))

employees = [
    Person("John", "Doe", date(2000, 1, 1)),
    Person("Jane", "Smith", date(1995, 5, 15)),
    Person("Alice", "Jones", date(1980, 11, 30)),
]

