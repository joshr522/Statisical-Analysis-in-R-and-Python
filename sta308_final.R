################
## STA 308 - Final in R
## Josh Roach

library(tidyverse)

## Reading in the original datasets
regions <- read_csv("censusRegions.csv")
states <- read_csv("state_abb_codes.csv")
unemployment <- read_csv("marchStateUnemployment.csv")

## Merging states and region datasets to assign each state
##    to their specific region
statesWithRegions <- merge(states, regions, by.x = "Code", by.y = "State")
## Merging the new states and region dataset with the unemployment
##    dataset to assign regions to each state in this set
##    to align the unemployment numbers by region.
unemploymentStates <- merge(unemployment, statesWithRegions, by.x = "State", by.y = "State")

## Removing DC and creating a variable to calculate the change
##    in unemployment rates from 2021 to 2022.
unemploymentStates <- unemploymentStates %>%
  filter(State != "District of Columbia") %>%
  mutate(unemploymentChange = March_21 - March_22)

## Calculating the mean, standard deviation, and 
##    coefficient of variation by region on the 
##    unemployment rate change.
unemploymentRegions <- unemploymentStates %>%
  group_by(Region) %>%
  summarize(meanUnemployment = mean(unemploymentChange),
            sdUnemployment = sd(unemploymentChange),
            cvUnemployment = sdUnemployment/meanUnemployment)

