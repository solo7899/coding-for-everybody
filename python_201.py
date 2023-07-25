#! /usr/bin/python3

import requests
import json

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
    print("Name :")
    for form in response.get("forms"): # character's name/s
        print(f'\t> {form.get("name")}')
    print()
    print(f"Height > {response.get('height')}")  # character's height
    print(f"Weight > {response.get('weight')}")  # character weight
    print()
    print("Abilities :")  # list of abilities
    for ability in response.get("abilities"):
        print(f"\t> {ability.get('ability').get('name')}")
    print()
    print("Items :")  # list of held items
    for item in response.get("held_items"):
        print(f"\t> {item.get('item').get('name')}")

    print("\n")
