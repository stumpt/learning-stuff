import pandas as pd
import numpy as np
#
# Simple linear interpolation
#
tempKey = 'T [K]' # we're going to need this a couple times so we'll just keep it as a variable
table_cols = [tempKey,'ρ [kg/m3]','Cp (kJ/kg*K)',
    'µe7 [Ns/m2]','νe6 [m2/s]','ke3 [w/mK]',
    'αe6 [m2/s]','Pr']

#
# This function needs to be called once before interpolate will work
#
def load(dataUrl): 
    global dataSet
    dataSet = pd.read_csv(dataUrl, sep=" ", names=table_cols, index_col=tempKey) # tell it to use the temp as index instead of some 
                                                                            # random integer. This also actually calculates an index
                                                                            # for the column so 'lookups' (like the "in" call below)
                                                                            # will be fast even with large amounts of data

#
# takes T (float temperature) and returns value based on match or interpolation
#
def interpolate(T):
    global dataSet
    if dataSet is None:
        return -1
    if T in dataSet.index: # if it's an exact known temperature
        return pd.DataFrame(dataSet.loc[T]) # return the row
    # otherwise, 
    dataSet.loc[T] = np.NaN # insert a blank row at the temperature requested
    dataSet = dataSet.interpolate("values") # tell pandas to interpolate all missing values using a simple 
                                            # linear interpolation based on the index value (the temperature).
                                            # there are many other approaches that can be used here, including
                                            # extrapolation if you wanted to go outside the bounds of the data, 
                                            # polynomial curves, etc.
    return pd.DataFrame(dataSet.loc[T]) # and return the conveniently filled-out row
