# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_first_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/09 19:57:45 by lbordana        #+#    #+#               #
#  Updated: 2026/02/10 12:49:10 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def check_temperature(temp_str: str) -> str:
    try:
        if 0 <= int(temp_str) <= 40:
            return f"{temp_str}°C is perfect for plants"
        elif int(temp_str) > 40:
            return f"Error : {temp_str}°C is too hot for plants (max 40°C)"
        else:
            return f"Error : {temp_str}°C is too cold for plants (min 0°C)"
    except ValueError:
        return f"Error : '{temp_str}' is not a valid number."


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    print("\nTesting temperature: 25")
    print(check_temperature("25"))
    print("\nTesting temperature: abc")
    print(check_temperature("abc"))
    print("\nTesting temperature: 100")
    print(check_temperature("100"))
    print("\nTesting temperature: -50")
    print(check_temperature("-50"))
    print("\nAll tests completed - program didn't crash !")


if __name__ == "__main__":
    test_temperature_input()
