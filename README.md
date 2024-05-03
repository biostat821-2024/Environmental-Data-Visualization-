# Environmental Data Visualization Application

**Team members**: Anastasiia Saenko, Antara Bhide, Keon Nartey

![Be a part of the solution, not pollution](https://github.com/biostat821-2024/Environmental-Data-Visualization-/assets/125210401/61319e61-968c-4981-aaa8-6102daaee9e2)

## Introduction:
This Githhub repository aims to visualise environmental, specifically pollution related data in [India](https://www.nytimes.com/2017/02/14/world/asia/indias-air-pollution-rivals-china-as-worlds-deadliest.html?_r=0).  

In 2019, as part of a worldwide survey, it was discovered that 21 out of the 30 most polluted cities were in India. And this pushed India’s ranking as a country to 5th place. The US AQI number averaged out at 152 and the PM2.5 figure recorded was 58.08µg/m³. This concentration was 5 times higher than that recommended by the World Health Organisation (WHO). This is an overall improvement on the 2018 figure of 72.54µg/m³. The levels of the pollutant PM 2.5 are often well above the World Health Organisation’s recommended level of exposure (often over 5 times higher) and this leads to serious respiratory problems for those exposed to it. 

Records show that in 2019 over 1.6 million deaths were attributed to poor air quality. the State of Global Air 2020 noted that air pollution is now the largest risk factor for death amongst all other forms.

In this repository, we focus primarily on the pollutants - Sulphur Dioxide and Nitrogen Oxide by analysing their state wise levels. 

## Approach
We divided this project into 3 key phases:
1. Data Cleaning accompanied with the creation of classes to calcuate the pollutant levels
2. Data Vizualization : We vizualised the data as a Heatmap and a Piechart
3. Testing all components

## Installation:
To replicate the resuts on your computer, please fork this guthub repository or clone it using https://github.com/biostat821-2024/Environmental-Data-Visualization-.git.

Please ensure that you install all libraries outlined within the requirements.txt file. You will also need to ensure that you have Python installed on your computer. 


## Data 

We wanted to understand more about India’s air quality using quantitative means.

To load the data which is a `csv` and have an what attributes the data has in our module,

First load a python script

> -  From cleaning_data import Environment
> - env = Environment("../data/data.csv") where you specify the path to the data in the object class.

The two of the 4 dangerous gas over the years in India has been Sulphur Dioxide (SO2) and Nitrogen oxide (NO2) we wanted to get the average levels these gases in india over the period.

Some basic python methods were created to get the 
- mean SO2 levels 
> - `env.average_sulphur_dioxide() = 10.829414322672587`

- mean NO2 levels 
> - `env.average_nitrogen_oxide() = 25.80962289781126`

- get the max SO2 levels by states in India.
> - `environment.state_max_so2()`

## Visualisations

We have included two visualisations our data:

# 1)  Heatmap : 

We created a heatmap  displaying the average levels of a particular pollutant across different states and years. It visually represents how pollution varies geographically and over time, helping us understand environmental trends and potential health implications more
intuitively. The function allows to choose different metrics to plot. 

![image](https://github.com/biostat821-2024/Environmental-Data-Visualization-/assets/54864655/5139155d-dd0f-4867-b5b7-537083f47ffe)


  # 2)  Pie Chart :

The pie chart visually represents the distribution of maximum Sulfur Dioxide (SO2) production across different states. Each slice of the pie corresponds to a state, with the size of the slice indicating the proportion of SO2 production from that state relative to the total production. This provides insights into which states contribute the most to overall SO2 emissions.

The function that was used to generate this pie chart was the `state_max_so2` which we had included in our codebase. The data frame that emeged a s result of this function was visualised as this pie chart. 

![image](https://github.com/biostat821-2024/Environmental-Data-Visualization-/assets/54864655/79d78e65-574a-4936-9444-54dbf861d57f)


A full **demonstration** of the visualization functions usage is provided in the [end_to_end.ipynb](src/end_to_end.ipynb). 

## Tests 

The testing class was developed for the data reading and basic functions and it is provided in the [test/test_cleaning.py](tests/test_cleaning.py); \

## Future Work
In order to build on this project, we would like to expand the the number of the types of pollutants such as Carbon Monoxide(CO) and Particulate Matter(PM10) who's levels we are analysing in India. We would then like to integrate health related data, preferably from official sources hosted by the Government Of India  to analyze the health disorders caused by each of these pollutants and the rate of growth of these diseases in India. 

## References

https://www.iqair.com/india

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9189448/




