Additional Support - Linear Regression


Additional Support
This page provides guidance on common challenges, best practices, and additional resources for selected steps in the assignment.

Data Preprocessing and Feature Engineering

Fixing Datatypes
Why separate categorical features from numerical ones?
* Machine learning models treat categorical and numerical features differently. Categorical variables often require encoding (one-hot or label encoding), while numerical features can be used directly in computations.
* Keeping them separate initially ensures correct transformations without unintended numerical operations on categorical data.

Train-Validation Split
Common questions:
* Why split the data before feature engineering? Prevents data leakage, ensuring that the validation set remains unseen during preprocessing.
* What’s a good split ratio? 80-20 or 70-30 is common. Ensure that the distribution of target and key features remains consistent across both sets.


Exploratory Data Analysis (EDA)

Why perform EDA separately on training and testing data sets?
* Data Leakage: If EDA is performed on the entire dataset (both training and testing), information from the test set may influence decisions made during model building. This leads to overfitting, where the model performs well on the training data but poorly on new, unseen data.
* Accurate Performance Evaluation: By performing EDA separately on the test set, we can ensure that the test data is distributed well enough to represent the real-world patterns the model might encounter. Well-distributed test data also helps to get an accurate evaluation of the model’s generalisation abilities.

Feature Distribution
Understanding skewness and transformations:
* Skewness indicates asymmetry in data distribution. High skewness can impact model assumptions.
* Transformations like log or square root normalisation can help make data more normally distributed.
  Resources:
* Understanding Skewness in Data
* Transformation in Python

Correlation Analysis
Why drop weakly correlated features?
Linear regression assigns coefficients based on relationships, so why do we want to drop any of the features when the model can simply assign small coefficients to less useful features?
* Weakly correlated features introduce noise and reduce model interpretability.
* Removing them reduces dimensionality and prevents overfitting.
* Feature selection ensures a more stable model by focusing on impactful predictors.
  Resources:
* Correlation Heatmap Tutorial


Model Building

Feature Scaling
Why scale when linear regression is scale-agnostic?
* While linear regression does not require feature scaling for estimating coefficients, applying scaling can improve numerical stability and make the results easier to interpret. 
* Scaling also helps gradient-based optimisation methods converge more quickly and enables a better comparison of feature importance, as standardised coefficients reflect their relative impact more clearly.
* For linear regression models, however, most libraries prefer the Ordinary Least Squares (OLS) method.
  Effect on the final model:
* Unscaled features with large values might dominate model interpretation.
* When you read about advanced regression techniques, you will see that scaling ensures better convergence in gradient-based methods like Ridge and Lasso.
  Resources:
* When and Why to Scale Data
* Effect of Scaling on Linear Regression

Libraries for Linear Regression
* statsmodels: Provides detailed statistical summaries, including confidence intervals and p-values. Good for interpretability.
* sklearn: Optimised for predictive performance but lacks statistical insights.

Recursive Feature Elimination (RFE)
How to select features using RFE?
* RFE ranks features by recursively removing least important ones and refitting the model.
* Iterate over different feature subsets and compare performance metrics (R-squared, adjusted R-squared). This helps in deciding an optimal number of features that justify the model performance.
  Manual vs RFE-based feature selection:
* Manual: Based on domain knowledge and exploratory analysis.
* RFE: Algorithmic, identifies features that contribute the most to prediction accuracy.
  Resources:
* Feature Selection with RFE


Results and Inference

Residual Analysis
Interpreting residual plots:
* Homoscedasticity: Residuals should have constant variance; patterns indicate heteroscedasticity.
* Normality: Use QQ-plots to check if residuals are normally distributed.
* Independence: Ensure residuals are uncorrelated.
  Resources:
* How to Interpret Residual Plots
* Assumptions of Linear Regression
* QQ-Plots in Python

Coefficient Analysis
How scaling affects coefficients?
* In standard-scaled models, coefficients represent the change in output per unit standard deviation of the feature. In other kinds of scaling, the scale of change varies as per the scaling function used.
* Convert back to the original scale by multiplying with the feature scaling factor.
* Use standardised coefficients to compare feature importance.
  Calculating the effect of unit change in scaled features:
  An example to understand how standard scaling affects the predicted output: If scaled_coeff = β and original feature std = σ, the real-world impact is β * σ per unit change in original scale.



Next, you will find the final submission field for this assignment.
