class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list:
    person_list = [Person(each["name"], each["age"]) for each in people]
    for each in people:
        person_instance = Person.people[each["name"]]
        if "wife" in each and each["wife"] is not None:
            person_instance.wife = Person.people[each["wife"]]
        if "husband" in each and each["husband"] is not None:
            person_instance.husband = Person.people[each["husband"]]

    return person_list
