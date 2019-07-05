# Seed disperser

### General Specs
4 seed layers : 
1. Canopy
1. Tree Stratum
1. Understorey
1. Shrub Layer

Best scenario : Must place 3 seed of different layers in each square meter. Sometimes it is not possible to have 3 different seeds in one square meter due to the number of seeds given at the beginning, so 2 of the same layer are ok but this scenario must be avoided as much as possible. 

Seeds must be randomly distributed across the whole area. We don't want to see patterns e.g: all canopy seeds in the first half of the area.


### V1 Specs
#### Inputs
1. area length
1. area width
1. nb canopy seeds
1. nb Tree Stratum seeds
1. nb Understorey seeds
1. nb Shrub Layer seeds

#### Output
1. Rectangular plot mapping the area dimensions.
1. Grid on the whole area dividing it in square meters.
1. Seeds to be planted in each square meter. 
1. Legend showing what color correspond to what seed layer (e.g: Canopy => blue)
1. Count of the number of each layer of seed in the final area and their percentage (ony for verifiaction purposes)


#### Improvements wanted in future releases
1. Being able to download and print the plot
1. Being able to feed not only seed layers but also the different seed type per layer to be placed (e.g: 27 seeds of "Apple tree" from "Tree Stratum" layer). Expecting around ~40 different seed type
1. Use non-rectangular area. User should be able to feed a totally custom area.


### V2 Specs
#### Inputs
1. area length
1. area width
1. CSV file which will contains layer|type|seed_count columns

#### Output
1. Rectangular plot mapping the area dimensions.
1. Grid on the whole area dividing it in square meters.
1. Seeds to be planted in each square meter. 
1. Legend : TBD. Markers or something to differentiate seed types (~40). Colors won't be used, because it is hard to differentiate between so many.
1. Count of the number of each seed type in the final area and their percentage (ony for verifiaction purposes)




