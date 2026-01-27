def ft_water_reminder():
    days_without_watering = int(input("Days since last watering: "))
    if days_without_watering > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
