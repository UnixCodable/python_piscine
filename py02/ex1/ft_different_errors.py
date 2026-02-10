# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_different_errors.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/09 22:02:57 by lbordana        #+#    #+#               #
#  Updated: 2026/02/10 17:50:53 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def garden_operations(error: str) -> None:
    if error == 'ValueError':
        raise ValueError('ValueError: invalid literal for int()')
    elif error == 'ZeroDivisionError':
        raise ZeroDivisionError('ZeroDivisionError: division by zero')
    elif error == 'FileNotFoundError':
        raise FileNotFoundError("FileNotFoundError: No such file\
 'missing.txt'")
    elif error == 'KeyError':
        raise KeyError("KeyError: 'missing plant'")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    error_to_test = ['ValueError', 'ZeroDivisionError', 'FileNotFoundError',
                     'KeyError']
    for error in error_to_test:
        print(f"\nTesting {error}...")
        try:
            garden_operations(error)
        except Exception as err:
            print(f'Caught {err.args[0]}')


test_error_types()
