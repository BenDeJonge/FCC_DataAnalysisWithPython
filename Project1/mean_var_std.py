import numpy as np

def calculate(lst):
    #Check correct length of 9 numbers.
    if len(lst) != 9:
        raise ValueError('List must contain nine numbers.')
    else:
        #Convert 9-element list to (3,3) np array.
        arr = np.reshape(lst, (3,3))
        axes = [0, 1, None]
        calculations = {
            'mean'               : [],
            'variance'           : [],
            'standard deviation' : [],
            'min'                : [],
            'max'                : [],
            'sum'                : []
            }
    
    #Setup required functions (first-class functions)
    funs = [np.mean, np.var, np.std, np.min, np.max, np.sum]
    
    #Loop over all axes.
    #Append function result to appropriate dictionary value.
    #Convert result to list.
    for axis in axes:
        for i, key in enumerate(calculations.keys()):
            calculations[key].append(funs[i](arr, axis).tolist())
    
    return calculations