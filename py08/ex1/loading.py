# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  loading.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: lbordana <lbordana@student.42mulhouse.f   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/19 01:00:31 by lbordana        #+#    #+#               #
#  Updated: 2026/04/15 15:13:53 by lbordana        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys

print("LOADING STATUS: Loading programs\n")

try:
    import pandas as pd
    print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
    import numpy as np
    print(f"[OK] numpy ({np.__version__}) - Numerical computation ready")
    import requests
    print(f"[OK] requests ({requests.__version__}) - Network access ready")
    import matplotlib
    print(f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready")
except ModuleNotFoundError as err:
    print(f"Error while loading the module : {err}")
    print("Please check dependencies in requirements.txt")
    print("Use 'pip install -r requirements.txt'")
    print("Or 'poetry install' then 'poetry run python loading.py'")
    sys.exit(1)


def transform():

    from matplotlib import pyplot as plt

    data = np.round(np.random.random(1000), 2)
    plt.plot(xpoints, ypoints)
    plt.show()


if __name__ == '__main__':
    transform()
