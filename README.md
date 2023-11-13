# Investment Simulation Script

## Overview
This script simulates an investment scenario with initial money subject to random fluctuations over numerous iterations. It's designed to model a stochastic process similar to some financial investments, where outcomes are influenced by randomness.

## Functionality
- **Initial Investment**: Starts with 1000 units.
- **Iterations**: Runs for 10000 iterations. Each iteration, the investment increases by 20% or decreases by 18%, based on random selection.
- **Key Statistics**: Calculates and prints statistics after iterations, including:
  - Percentage of simulations with final amount > initial
  - Mean, median, standard deviation of final amounts
  - Risk-reward ratio
- **Value Modification**: Final values >2000 are modified to 2100.
- **Visualization**: Generates a scatter plot showing final values of each simulation. 
  - Points above the initial value (1000) are green.
  - Points below are blue.
  - A horizontal red line represents the initial value.
  - Y-axis ticks at 0, 500, 1000, 1500, 2000, and >2000 (capped at 2100).

## Output Example
- Percentage of Profitable Simulations: 8.51%
- Mean Final Value: 1,096,819.17
- Median Final Value: 0.31
- Standard Deviation: 82,856,832.86
- Risk-Reward Ratio: 75,611.78

Following is graph generated from simulation:
![Simulation Result](figure.png).

## Usage
Requires Python with numpy and matplotlib libraries. Run the script in a Python environment to see console output and the graphical plot.
