import numpy as np
import time

def calc_inflation(weights, vpi_now, vpi_one_year_ago):
    percentage_weights = weights/np.sum(weights)
    #print(percentage_weights)
    return (np.round(np.sum(percentage_weights*vpi_now),decimals=1))/np.round((np.sum(percentage_weights*vpi_one_year_ago)),1) - 1
'''
off_vpi_june21 = np.load('official_vpi_june21.npy')
off_vpi_june20 = np.load('official_vpi_june20.npy')
weights = np.load('official_weights.npy')
print(weights/1000)
print(off_vpi_june21)
print(calc_inflation(weights, off_vpi_june21, off_vpi_june20))
'''