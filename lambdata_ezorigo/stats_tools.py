"""
stats functions for mean, median, mode,
variance, standard deviation, and coefficient of variation
"""
import numpy as np


def mean(data):
    """
    function to calculate mean of data
    """
    size = len(data)
    mean = sum(data)/size
    return mean

def median(data):
    """
    function to calculate median of data
    """
    data.sort()
    size = len(data)

    if len(data) % 2 == 1:
        median = data[int(size/2)]
    else:
        median = (data[int(size/2 - 1)] +
                    data[int(size/2)]) / 2
    return median

def mode(data):
    """
    function to get mode of data, only returns the first it encounters if
    there are more than 1 mode
    """
    mode = max(data, key=data.count)
    return mode

def variance(data, sample=True):
    """
    function to calculate variance of data

    by default, it calculates sample variance, change sample=False if you
    want to calculate population.
    """
    size = len(data)
    distance_squared = list(map(lambda x: (x - sum(data)/size) **
                                2, data))

    if sample is True:
        variance = sum(distance_squared)/(size - 1)
    if sample is False:
        variance = sum(distance_squared)/(size)
    return variance

def stddev(data, sample=True):
    """
    function to calculate standard deviation of data

    by default, it calculates sample standard deviation, change
    sample=False if you want to calculate population.
    """
    size = len(data)
    distance_squared = list(map(lambda x: (x - sum(data)/size) **
                                2, data))

    if sample is True:
        variance = sum(distance_squared)/(size - 1)
        stddev = variance**(1/2)
    if sample is False:
        variance = sum(distance_squared)/(size)
        stddev = variance**(1/2)
    return stddev

def coeffvar(data, sample=True):
    """
    function to calculate the coefficient of variance of data

    by default, it calculates sample coefficient of variance, change
    sample=False if you want to calculate population.
    """
    size = len(data)
    mean = sum(data)/size
    distance_squared = list(map(lambda x: (x - sum(data)/size) **
                                2, data))

    if sample is True:
        variance = sum(distance_squared)/(size - 1)
        stddev = variance**(1/2)
        coeffvar = stddev/mean
    if sample is False:
        variance = sum(distance_squared)/(size)
        stddev = variance**(1/2)
        coeffvar = stddev/mean
    return coeffvar
