# ======== Based on: https://realpython.com/python-f-strings/ =======


print("%(language)s has %(number)02d quote types."%
      {"language": "Python", "number":15})
print("\n")

name = "Eric"
print("Hello, %s."% name)
print("\n")

name = "Eric"
age = 74
print("Hello, %s. You are %s."% (name, age))
print("\n")

first_name = "Eric"
last_name = "Idle"
age = 74
profession = "comedian"
affiliation = "Monty Python"
print("Hello, %s %s. You are %s. You are a %s. You were a member of %s." % (first_name, last_name, age, profession, affiliation))
print("\n")

# ============= str.format() ===================

print("Hello, {}. You are {}.".format(name, age))
print("\n")

print("Hello, {1}. You are {0}.".format(age, name))
print("\n")

person = {'name': 'Eric', 'age': 74}
print("Pass an object. Hello, {name}. You are {age}.".format(name=person['name'], age=person["age"]))
print("\n")

person = {"name":"Eric", "age":74}
print("**trick. Hello {name}. You are {age}.".format(**person))
print("\n")

# ============== f-strings ================
name = "Eric"
age = 74
print(f"f-string: Hello, {name}. you are {age}.")
print("\n")

print(f"{2 * 37}")
print("\n")

def to_lowercase(input):
    return input.lower()

name = "Eric Idle"
print(f"Call a function: {to_lowercase(name)} is funny.")
print("\n")

print(f"Call a method directly: {name.lower()} is funny.")
print("\n")

class Comedian:
    def __init__(self, first_name, Last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"

new_comedian = Comedian("Eric", "Idle", "74")
print(f"Objects created from classes: {new_comedian}")
print("\n")
print(f"Objects created from classes with __repr__: {new_comedian!r}")
print("\n")
