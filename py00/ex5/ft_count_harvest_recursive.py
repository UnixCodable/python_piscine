def ft_count_harvest_recursive(days=None):
    if days is None:
        days = int(input("Days until harvest: "))
        ft_count_harvest_recursive(days)
        print("Harvest time!")
    elif days > 0:
        ft_count_harvest_recursive(days - 1)
        print("Day", days)
