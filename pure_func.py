import random

pies = ["apple", "cherry", "blueberry",
        "strawberry", "raspberry", "peach", "creame"]

def get_pies():
    return pies

def add_pie(pie):
    pies.append(pie)

def remove_pie(pie):
    pies.remove(pie)

def get_pie(index):
    return pies[index]

def get_pie_count():
    return len(pies)

def get_pie_names():
    return pies

def get_pie_names_sorted():
    return sorted(pies)

def get_pie_names_reversed():
    return reversed(pies)

def get_pie_names_random():
    return random.shuffle(pies)

print(get_pie_names())
print(get_pie_names_sorted())
print(get_pie_names_reversed())
print(get_pie_names_random())

add_pie("chocolate")

print(get_pie_names())
print(get_pie_count())

remove_pie("chocolate")

print(get_pie_names())
print(get_pie(0))
print(get_pie(1))
print(get_pie_count())