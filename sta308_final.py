#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:18:30 2022

STA 308 - Final

Writing a program to do calculate the coefficient of variation in the 
change in unemployment rates by regions within the US

@author: joshuaroach
"""

import pandas as pd

## Loading in the base datasets
regions = pd.read_csv("https://tjfisher19.github.io/data/censusRegions.csv")
states = pd.read_csv("https://tjfisher19.github.io/data/state_abb_codes.csv")
unemployment = pd.read_csv("https://tjfisher19.github.io/data/marchStateUnemployment.csv")

## Merging the state and region datasets
statesWithRegions = states.merge(regions, left_on='Code', right_on='State')
## Merging the new dataset with the unemployment dataset
unemploymentStates = statesWithRegions.merge(unemployment, left_on = 'State_x', right_on = 'State')

## Creating a new variable 'unemploymentChange' that calculate the 
##   change in unemployment rates by state
unemploymentStates['unemploymentChange'] = unemploymentStates['March_21'] - unemploymentStates['March_22']

## Filters out DC to keep only states in the dataframe
unemploymentStates = unemploymentStates[unemploymentStates['Code'] != 'DC']

## Creating the final dataframe that caclulates mean, standard deviation
##  and coefficient of variation on unemploymentChange by region
unemploymentRegion = pd.DataFrame(
    {
     "MeanUnemploymentChange": unemploymentStates.groupby('Region')['unemploymentChange'].mean(),
     "StandardDeviation": unemploymentStates.groupby('Region')['unemploymentChange'].std(),
     "CoefficientOfVariance": unemploymentStates.groupby('Region')['unemploymentChange'].std()/unemploymentStates.groupby('Region')['unemploymentChange'].mean()
     }
    )
unemploymentRegion
