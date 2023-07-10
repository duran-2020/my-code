def main():
    farms = [
        {"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
        {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
        {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}
    ]

    # Print the animals in the NE Farm
    print("Animals in NE Farm:")
    for animal in farms[0]["agriculture"]:
        print("-", animal)

    print("\nAvailable Farms:")

    # Print the names of available farms
    for farm in farms:
        print("-", farm["name"])
    choice = input("Pick a farm!\n")

    # Iterate over farms and print animals/plants for the chosen farm
    for farm in farms:
        if farm["name"].lower() == choice.lower():
            print(f"\nAnimals/Plants in {farm['name']}:")
            for item in farm["agriculture"]:
                print("-", item)

    # Modified farms list
    farms = [
        {"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
        {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
        {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
        {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}
    ]

    print("\nAvailable Farms:")

    # Print the names of available farms from the modified list
    for farm in farms:
        print("-", farm["name"])
    choice = input("Pick a farm!\n")

    # Iterate over farms and print only the animals for the chosen farm, excluding "carrots" and "celery"
    for farm in farms:
        if farm["name"].lower() == choice.lower():
            print(f"\nAnimals in {farm['name']}:")
            for item in farm["agriculture"]:
                if item not in ["carrots", "celery"]:
                    print("-", item)


if __name__ == "__main__":
    main()

