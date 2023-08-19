# Travelling Salesman Problem

> [!WARNING]
> This project is not made for general use, please refer at your own risk.

Travelling Salesman describes a problem where a salesman has to visit a number of cities. The order of the cities does not matter, but the salesman has to visit each city exactly once and return to the starting city. The goal is to find the shortest possible route.

Here, we use genetic algorithm to find the optimal solution.

## Files

- `Lab 2_Genetic Algorithm.ipynb`: Jupyter notebook for the project
- `helperpy/duplicatecheck.py`: Verify answer does not contain duplicate cities
- `helperpy/plot.py`: Plot the jsons
- `helperpy/plot2.py`: Plot the all.csv 
- `helperpy/plot3.py`: Plot the answer.csv into a line graph with scatterplot
- `csv/answer.csv`: The current optimum answer provided by the GA
- `csv/all.csv`: The iteration log of the three parent selection methods