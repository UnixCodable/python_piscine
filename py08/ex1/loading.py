# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   loading.py                                          :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: lbordana <lbordana@student.42mulhouse.fr>   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/19 01:00:31 by lbordana           #+#    #+#             #
#   Updated: 2026/04/05 01:10:28 by lbordana          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

print("LOADING STATUS: Loading programs\n")

print("Checking dependencies:")
try:
    import pandas
    print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
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
