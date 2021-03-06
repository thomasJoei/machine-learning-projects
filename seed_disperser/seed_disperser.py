
# coding: utf-8


# Specs:
# 4 seed layers : Canopy, Tree Stratum, Understorey, Shrub Layer.
# Must place 3 seed of different layers in each square meter.
# Seeds must be randomly distributed across the whole area.

import io
from enum import Enum 
import numpy as np
import gzip
import random
np.random.seed(19680801)
import matplotlib.pyplot as plt

def count_seeds(area_list, seed_layers):
    result = dict.fromkeys(seed_layers, 0)
    
    for x in area_list:
        for seed_type in x:
            result[seed_type] += 1
    
    return result

def print_distribution(area_list, seed_layers):
    result = count_seeds(area_list, seed_layers)
    seeds_count = sum(result.values())
    
    for seed_type, seed_nb in result.items():
        print("{} : {} ({}%)".format(seed_type, seed_nb, (seed_nb / seeds_count) * 100))

def decrement_seed_stock(key, seed_layers, seeds_stocks):
    seeds_stocks[key] -= 1
   
    if (seeds_stocks[key] <= 0):  # removing from list if no seeds left
        seed_layers.remove(key)
    
def select_seeds_from_stock(size, seeds_stocks):
    seed_layers = list(seeds_stocks.keys())
    selection = []

    # check size of current selection and if seed_type_array not empty
    while len(selection) < size and seed_layers:
        size_to_complete = size - len(selection)
        size_possible = min(size_to_complete, len(seed_layers))
        my_selection = np.random.choice(seed_layers, size=size_possible, replace=False)
        
        # merge in selection array
        selection = np.concatenate((selection, my_selection), axis=None) 
        
        for seedName in my_selection:
            decrement_seed_stock(seedName, seed_layers, seeds_stocks)
        
    return selection


def plant_seeds(area_size, seeds_stocks):
    area = []
    
    for i in range(area_size) :
        area.append(select_seeds_from_stock(3, seeds_stocks))

    # Shuffle the area to avoid lack of one seed layer at the end of the list.
    # e.g: if there is 20% of one layer the stock will go empty pretty fast 
    # and the distribution won't be uniform accross the area.
    random.shuffle(area)
    return area


def rand_jitter(arr):
    return arr + np.random.uniform(low=0.1, high=0.9, size=len(arr))

def get_coordinates(case_index, length):
    x = float(case_index % length)
    y = float(case_index // length)
    return x, y

def separate_seeds(linear_area, length, seed_layers):
    result = {key: {'x' : [], 'y' : []} for key in seed_layers}
    
    for case_index, square in enumerate(linear_area):
        for seed in square:
            x,y = get_coordinates(case_index, length)
            result[seed]['x'].append(x)
            result[seed]['y'].append(y)
    
    return result


def jitter(ax, x, y, s=30, c='b', marker='.', cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=None, rasterized=False, **kwargs):
    return ax.scatter(rand_jitter(x), rand_jitter(y), s=s, c=c, marker=marker, cmap=cmap, norm=norm, 
                      vmin=vmin, vmax=vmax, alpha=alpha, linewidths=linewidths, rasterized=rasterized, verts=verts, **kwargs)


def get_plot(coordinates_per_seed_type, length, width, lowquality=False, seed_color = {
    'canopy' : 'tab:blue',
    'tree_stratum' : 'tab:orange',
    'understorey' : 'tab:green',
    'shrub_layer' : 'tab:brown'
    }):

    plt.rcParams["figure.figsize"] = [length/5, width/5]
    
    fig, ax = plt.subplots()
    
    for seed_type, coordinates in coordinates_per_seed_type.items():
        marker_letter = seed_type[:1] # first letter
        jitter(ax, coordinates.get('x'), coordinates.get('y'), c=seed_color.get(seed_type), label=seed_type,
                   alpha=0.8, rasterized=lowquality
               #marker="${}$".format(marker_letter)
              )

    # ax.legend()
    # Major ticks every 20, minor ticks every 5
    ax.set_xticks(np.arange(0, length + 1, 5))
    ax.set_xticks(np.arange(0, length + 1 , 1), minor=True)
    ax.set_yticks(np.arange(0, width + 1, 5))
    ax.set_yticks(np.arange(0, width + 1 , 1), minor=True)

    ## And a corresponding grid
    ax.grid(which='both')
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    # ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    # fig.legend(loc="upper right")
    fig.legend(loc="lower left")
    fig.suptitle('Dispersed seeds', fontsize=16)
    #plt.show()
    
    return fig, ax

def disperse_seeds(seeds_stocks, length, width):
    
    area_size = length * width
    seeds_count = area_size * 3
    
    # validation 
    seed_sum = sum(seeds_stocks.values())

    if (seed_sum != seeds_count) :
        print("The seed sum is {} and must be {}".format(seed_sum, seeds_count))
        return 
    
    area = plant_seeds(area_size, seeds_stocks)    

    coordinates_per_seed_type = separate_seeds(area, length, list(seeds_stocks.keys()))
    fig, ax = get_plot(coordinates_per_seed_type, length, width, lowquality=True)

    return fig, ax

def get_svg(fig):
    imgdata = io.StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)  # rewind the data

    svg_data = imgdata.getvalue()  # this is svg data
    imgdata.close()
    return svg_data

def get_svgz(fig):
    svg_data = get_svg(fig)
    return gzip.compress(svg_data.encode())
