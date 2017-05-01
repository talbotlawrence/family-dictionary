my_family = {
    'father': {
        'name': 'Jim',
        'age': 103
    },
    'mother': {
        'name': 'Kathleen',
        'age': 102
    },
    'spouse': {
        'name': 'Jen',
        'age': 28
    },
    'daughter': {
        'name': 'Madelyn',
        'age': 5
    }
}

# Krista is my sister and is 42 years old
for family_member,value_of in my_family.items():
    print("{} is my {} and is {} years old".format(value_of['name'], family_member, str(value_of['age'])))