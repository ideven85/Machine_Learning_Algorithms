# Regularization-Based Regression Model for Prediction of the Actual Value of Prospective Real-Estate Properties and Decision Making for Investment
> House price modelling based on regression with regularization to reveal significant predictors of house prices and enable decision making for investment.
> Determination of the suitability and effectiveness of the predictors in describing house price 
> Determination of the optimal value of lambda for ridge and lasso regression


## Table of Contents
* [General Info](#general-information)
* [Conclusions](#conclusions)
* [Technologies Used](#technologies-used)

<!-- You can include any other section that is pertinent to your problem -->

## General Information
- A US-based housing company named Surprise Housing has decided to enter the Australian market. The company uses data analytics to purchase houses at a price below their actual values and sell at a higher price. For the same purpose, the company has collected a data set from the sale of houses in Australia. 

- The model built using this data set will be used by the management to understand how the prices vary with the variables. This will not only enable management to accordingly manipulate the strategy of the firm and concentrate on areas that will yield high returns but also to understand the pricing dynamics of a new market.




## Conclusions
- The optimal regularization strength for Ridge regression, determined through hyperparameter tuning, is 10.0.

- The optimal regularization strength for Lasso regression, determined through hyperparameter tuning, is approximately 316.23.

-                               Performance Table
|Regression|Dataset|RSS         |R2      |Adj. R2 |MSE         |NRMSE        | 
|----------|-------|------------|--------|--------|------------|-------------|
|Linear    |Train  |2.852138e+12|0.553005|0.549026|2.793475e+09|-52853.331582|  
|Linear    |Test   |1.542873e+12|0.452632|0.441122|3.522541e+09|-59350.995782|  
|Ridge     |Train  |1.750575e+12|0.725645|0.723203|1.714569e+09|-41407.356141| 
|Ridge     |Test   |7.596290e+11|0.730505|0.724838|1.734313e+09|-41645.081050|  
|Lasso     |Train  |1.289688e+12|0.797877|0.796077|1.263161e+09|-35540.979030| 
|Lasso     |Test   |5.527885e+11|0.803886|0.799762|1.262074e+09|-35525.682431|

- Overall, lower values of RSS, MSE, and NRMSE and higher values of R2 and Adj. R2 indicate better model performance.

- The substantial difference in the R2 values of the linear regression model on the train and test datasets indicates overfitting and the model's inability to generalize.

- Regularization is an approach to prevent overfitting by adding a penalty term to the loss function that the model seeks to minimize. The alpha parameter in Ridge and Lasso regressions is a regularization term that controls the magnitude of the coefficients in the model. For Ridge regression (L2 regularization), the regularization term is the sum of the squares of the coefficients, multiplied by alpha. For Lasso regression (L1 regularization), the regularization term is the sum of the absolute values of the coefficients, multiplied by alpha. The selection of optimal values of alpha is important, as it manifests the tradeoff between bias and variance and hence determines the model complexity. The difference between Ridge and Lasso lie in the fact that in the process of penalization, Lasso reduces the coefficients to zero, thereby eliminating those features from the model, whereas Ridge can only minimize the coefficients to approximately zero but not completely eliminate them.

- Considering the above performance table obtained as output, we note the following:
1. The Ridge and Lasso models show better performance (higher R2, lower RMSE) on both the training and test datasets relative to the Linear Regression model.

2. The Ridge and Lasso models also show comparable performance on the training and test datasets (R2 and RMSE are close in value), suggesting that they are well-generalized.

3. The Lasso model performs slightly better than the Ridge model in this case, on both training and test data, and would be the preferred model based on these results for this problem statement.
Equation for the lasso regression model: y = 85725.947736 + 30512.222719 * YearRemodAdd + 216326.777645 * GrLivArea + 50927.778547 * Fireplaces + 59249.790586 * GarageCars - 56528.061292 * PropertyAge + 39303.245706 * Neighborhood_NoRidge + 43767.665578 * OverallQual_8 + 102387.775077 * OverallQual_9 + 120041.591278 * OverallQual_10

- The following are the five best predictors of the target SalePrice:
• Above grade (ground) living area square feet (GrLivArea: 216,326.78)
• "Very excellent" and "excellent" rates of the overall material and finish of the house (OverallQual_10: 120,041.59; OverallQual_9: 102,387.77)
• Size of garage in car capacity (GarageCars: 59,249.79)
• Number of fireplaces (Fireplaces: 50,927.78)


## Technologies Used
- NumPy - version 1.23.5
- Pandas - version 1.5.3
- Matplotlib - version 3.7.0
- Seaborn - version 0.12.2
- sklearn - version 1.2.1
- statsmodels - version 0.13.5


## Contact
Created by [@Sangbeda] - feel free to contact me!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->