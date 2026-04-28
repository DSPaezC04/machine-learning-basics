# California Housing Price Prediction

## Overview

This project applies multiple regression techniques to predict housing prices using the California Housing dataset.

Three models were evaluated:

- Linear Regression
- Polynomial Regression (Degree 2)
- Polynomial Regression (Degree 3)

## Objective

Identify whether non-linear transformations improve prediction accuracy over a traditional linear model.

## Dataset

California Housing Dataset from Scikit-learn.

## Features Used

- MedInc
- HouseAge
- AveRooms
- Latitude

## Results

| Model | R² | RMSE |
|------|------|------|
| Linear Regression | 0.5043 | 0.8059 |
| Polynomial Degree 2 | **0.5188** | **0.7940** |
| Polynomial Degree 3 | 0.5139 | 0.7980 |

## Key Findings

- Income is the strongest predictor of housing prices.
- Polynomial Degree 2 provided the best balance of complexity and performance.
- Increasing complexity beyond degree 2 did not improve generalization.

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

## Author

David Santiago Paez