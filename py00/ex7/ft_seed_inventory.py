def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        unit = print(f"{seed_type.capitalize()} seeds: \
{quantity} packets available")
    elif unit == "grams":
        unit = print(f"{seed_type.capitalize()} seeds: \
{quantity} grams total")
    elif unit == "area":
        unit = print(f"{seed_type.capitalize()} seeds: covers \
{quantity} square meters")
    else:
        print("Unknown unit type")
