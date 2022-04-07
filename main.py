import numpy as np
from geneticalgorithm import geneticalgorithm as ga
import matplotlib.pyplot as plt

import ExcelInterface

algorithm_param = {'max_num_iteration': 3000,\
                   'population_size':100,\
                   'mutation_probability':0.1,\
                   'elit_ratio': 0.01,\
                   'crossover_probability': 0.5,\
                   'parents_portion': 0.3,\
                   'crossover_type':'uniform',\
                   'max_iteration_without_improv':None}


def f(x):
    return ExcelInterface.get_satisfaction(x)


var_bound = np.array([[160, 620],  # consumption
                      [0, 2],  # roof_catchment, NOTE: needs conversion
                      [0, 201],  # additional_catchment,
                      [0, 5],  # collection_tank, NOTE: needs conversion
                      [0, 50],  # storage_tank_volume,
                      [10, 100],  # x,
                      [-25, 20],  # y,
                      [0, 10],  # tower_height,
                      [1, 4],  # pump, NOTE: needs conversion
                      [0, 2],  # filter_location, NOTE: needs conversion
                      [0, 2],  # five_um_filter,
                      [0, 2],  # twenty_um_filter,
                      [0, 2],  # UV, NOTE: needs conversion
                      [0, 2],  # chemical_type, NOTE: needs conversion
                      [0, 2],  # power_system_choice, NOTE: needs conversion
                      [1, 10],  # num_batteries,
                      [0, 4],  # solar_panel_type, NOTE: needs conversion
                      [0, 20]  # num_solar_panels,
                      ])

model = ga(function=f, dimension=18, variable_type='int', variable_boundaries=var_bound)

model.run()
