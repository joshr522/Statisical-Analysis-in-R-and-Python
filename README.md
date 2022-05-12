# sta308_final
Final Exam for STA 308 Sp2022
Josh Roach

The material in this repository includes two files that run the same program, one being in R and the other in Python. The csv files are the datasets contained within these programs. Below are my answers to the questions posed in the assignment. 

A. The coefficient of variation is the ratio of the standard deviation to the mean. This gives a figure to reference to compare the relationship between standard deviation and the mean. 

B. The coefficient of variation is highest in the West, meaning that the standard deviation of the unemployment rate change is higher in relation to the mean in the West than the standard deviations in other regions. It is lowest in the South, meaning the standard deviation in the South is lowest in comparison to its mean than any other region. 

C. 
| Functionality                                                      | In R                                 | In Python                    |
|--------------------------------------------------------------------|--------------------------------------|------------------------------|
| Loading a package for data handling                                | library(tidyverse)                   | import pandas as pd          |
| Reading a csv file into a dataframe                                | read.csv() or read_csv() (tidyverse) | pandas.read_csv()            |
| Merge two datasets into one based on a matching column             | merge()                              | df.merge()                   |
| Setting the variables to match while merging                       | by.x='', by.y=''                     | left_on='', right_on=''      |
| Creating new variables                                             | mutate()                             | df['new variable'] =         |
| Organizing data by grouping similar observations within a variable | group_by()                           | df.groupby()                 |
| Removing rows based on a specific criteria                         | filter(variable != 'obs.')           | df[df['variable'] != 'obs.'] |
| Calculate aggregated summaries                                     | summarize()                          | df.agg()                     |

D. I think my favorite topic was running simulations. Using while and for loops to simulate different scenarios was super interesting. There is so much potential within these simulations to predict important things (election results, sports games, etc.). I've always been fascinated by forecasting models that run simulations to predict a result before the event even happens. I would love to continue to learn more complex simulations and how to build these forecasting models. 

