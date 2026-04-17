# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   loading.py                                          :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: lbordana <lbordana@student.42mulhouse.fr>   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/19 01:00:31 by lbordana           #+#    #+#             #
#   Updated: 2026/04/17 22:53:13 by lbordana          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import sys

print("LOADING STATUS: Loading programs\n")

print("Checking dependencies:")
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


def analysis() -> None:

    from matplotlib import pyplot as plt

    print('\nAnalyzing Matrix data...')
    data = np.round(np.random.random(1000), 2)

    print('Processing 1000 data points...')
    data_plot = pd.Series(data)
    data_plot.plot()

    print('Generating visualization...')
    plt.savefig('matrix_analysis.png')

    print('\nAnalysis complete!')
    print('Results saved to: matrix_analysis.png')


if __name__ == '__main__':
    analysis()
