def ft_count_harvest_recursive(days=int(input("Days until harvest: "))):
    if days > 1:
        ft_count_harvest_recursive(days - 1)
        print("Days", days)
    else:
        print("Time to harvest!")
