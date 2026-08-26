from typing import TypedDict

class Person(TypedDict):
    # defining the keys of our dictionary
    name: str
    age: int
    
new_person: Person = {'name':'Abdul Rehman Gulshan', 'age':35}

print(new_person)