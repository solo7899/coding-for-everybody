#! /usr/bin/python3

import requests

while True:
    # TODO: ask for user input => which pokemon
    user_input = input("Which pokemon do you like? ").lower()
    # user_input = "ditto"

    # TODO: create a dynamic url
    url = f"https://pokeapi.co/api/v2/pokemon/{user_input}"

    # TODO: fetch data
    response = requests.get(url)

    # TODO: check if response is valid
    if response.status_code != 200:
        print("Character not found\n\n")
        continue

    # TODO: convert json data
    response = response.json()
    # print(type(response))

    # TODO: print out json data
    print(f"Name   > {response.get('name')}")  # character's name
    print(f"Height > {response.get('height')}")  # character's height
    print(f"Weight > {response.get('weight')}")  # character weight
    print()
    print("forms :")
    forms = response.get("forms")
    if len(forms) > 0:
        for form in forms:  # character's form/s
            print(f'\t> {form.get("name")}')
    else:
        print("\t> None")
    print()
    print("Abilities :")  # list of abilities'
    abilities = response.get("abilities")
    if len(abilities) > 0:
        for ability in abilities:
            print(f"\t> {ability.get('ability').get('name')}")
    else:
        print("\t> None")
    print()
    print("Items :")  # list of held items
    items = response.get("held_items")
    if len(items) > 0:
        for item in items:
            print(f"\t> {item.get('item').get('name')}")
    else:
        print("\t> None")

    print("-" * 100, "\n")
