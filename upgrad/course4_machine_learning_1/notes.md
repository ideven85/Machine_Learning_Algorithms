Suppose you have a dataset for which the scatter plot looks like the following:
     
￼
 
Now, if you run a linear regression on this dataset in Python, it will fit a line on the data which, say, looks like the following:
     
￼
 
Now, you can clearly see that the data is randomly scattered and doesn't seem to follow a linear trend or any trend, in general. But Python will anyway fit a line through the data using the least squared method. But you can see that the fitted line is of no use in this case. 
 
Hence, every time you perform a linear regression, you need to test whether the fitted line is a significant one or not or to simply put it, you need to test whether β1 is significant or not. And in comes the idea of Hypothesis Testing on β1. Please note that the following text will assume the knowledge of hypothesis testing, which was covered in one of the earlier modules. Please revisit the module on hypothesis testing in case you need to brush up.
 
You start by saying that β1 is not significant, i.e. there is no relationship between X and y.
So in order to perform the hypothesis test, we first propose the null hypothesis that β1 is 0. And the alternative hypothesis thus becomes β1 is not zero.
* Null Hypothesis (H0): β1=0
* Alternate Hypothesis (HA): β1≠0 
Let's first discuss the implications of this hypothesis test. If you fail to reject the null hypothesis that would mean that β1 is zero which would simply mean that β1 is insignificant and of no use in the model. Similarly, if you reject the null hypothesis, it would mean that β1 is not zero and the line fitted is a significant one.
 
Now, how do you perform the hypothesis test? Recall from your hypothesis testing module that you first used to compute the t-score (which is very similar to the Z-score) which is given by X-μ/s*sqrt(n) where μ is the population mean and s is the sample standard deviation which when divided by n is also known as standard error.
Using this, the t-score for β^1 comes out to be (since the null hypothesis is that β1 is equal to zero):

β^1-0/SE(β^1)

Now, in order to perform the hypothesis test, you need to derive the p-value for the given beta. If you're hazy on what p-value is and how it is calculated, it is recommended that you revisit the segment on p-value. Please note that the formula of SE(β1) provided in the t-score above is out of scope of this course.
 

Let's do a quick recap of how do you calculate p-value anyway:
* Calculate the value of t-score for the mean point (in this case, zero, according to the Null hypothesis that we have stated) on the distribution
* Calculate the p-value from the cumulative probability for the given t-score using the t-table
* Make the decision on the basis of the p-value with respect to the given value of β (significance level)
Now, if the p-value turns out to be less than 0.05, you can reject the null hypothesis and state that β1 is indeed significant.
 
Please note that all of the above steps will be performed automatically by the libraries we use Python which you'll learn in the very next segment.

Coming up
Now that you know how to determine whether your beta is significant or not, you'll start building the model in the next segment
 
Additional Reading
Why does the test statistic for β1 follow a t-distribution instead of a normal distribution? (here)


# Summary Statistics:
Now, let's take a look at the summary statistics that was outputted by the model again.

1. F-statistic
You were introduced to a new term named F-statistic and Prob(F-statistic). Now, recall that in the last segment, you did a hypothesis test for beta to determine whether or not the coefficient β1 outputted by the model was significant or not. Now, F-statistic is similar in the sense that now instead of testing the significance of each of the betas, it tells you whether the overall model fit is significant or not. This parameter is examined because many a time it happens that even though all of your betas are significant, but your overall model fit might happen just by chance.
 

2. The heuristic is similar to what you learnt in the normal p-value calculation as well. If the 'Prob (F-statistic)' is less than 0.05, you can conclude that the overall model fit is significant. If it is greater than 0.05, you might need to review your model as the fit might be by chance, i.e. the line may have just luckily fit the data. In the image above, you can see that the p-value of the F-statistic is 1.52e-52  which is practically a zero value. This means that the model for which this was calculated is definitely significant since it is less than 0.05.
 
This will be more appreciable when you study multiple linear regression since there you have a lot of betas for the different predictor variables and thus it is very helpful in determining if all the predictor variables together as a whole are significant or not or simply put, it tells you whether the model fit as a whole is significant or not. 
 

3. R-squared
Like you studied earlier as well, R-squared value tells you exactly how much variance in the data has been explained by the model. In our case, the R-squared is about 0.816 which means that the model is able to explain 81.6% of the variance which is pretty good.
 

4. Coefficients and p-values:
The p-values of the coefficients (in this case just one coefficient for TV) tell you whether the coefficient is significant or not. In this case, the coefficient of TV came out to be 0.0545 with a standard error of about 0.002. Thus, you got a t-value of 24.722 which lead to a practically zero p-value. Hence, you can say that your coefficient is indeed significant. 
 
Apart from this, the summary statistics outputs a few more metrics which are not of any use as of now. But you'll learn about some more of them in multiple linear regression.

5. F-statistic
You were introduced to a new term named F-statistic and Prob(F-statistic). Now, recall that in the last segment, you did a hypothesis test for beta to determine whether or not the coefficient β1 outputted by the model was significant or not. Now, F-statistic is similar in the sense that now instead of testing the significance of each of the betas, it tells you whether the overall model fit is significant or not. This parameter is examined because many a time it happens that even though all of your betas are significant, but your overall model fit might happen just by chance. The heuristic is similar to what you learnt in the normal p-value calculation as well. If the 'Prob (F-statistic)' is less than 0.05, you can conclude that the overall model fit is significant. If it is greater than 0.05, you might need to review your model as the fit might be by chance, i.e. the line may have just luckily fit the data. In the image above, you can see that the p-value of the F-statistic is 1.52e-52  which is practically a zero value. This means that the model for which this was calculated is definitely significant since it is less than 0.05.
 
This will be more appreciable when you study multiple linear regression since there you have a lot of betas for the different predictor variables and thus it is very helpful in determining if all the predictor variables together as a whole are significant or not or simply put, it tells you whether the model fit as a whole is significant or not. 
 

6. R-squared
Like you studied earlier as well, R-squared value tells you exactly how much variance in the data has been explained by the model. In our case, the R-squared is about 0.816 which means that the model is able to explain 81.6% of the variance which is pretty good.
 

7. Coefficients and p-values:
The p-values of the coefficients (in this case just one coefficient for TV) tell you whether the coefficient is significant or not. In this case, the coefficient of TV came out to be 0.0545 with a standard error of about 0.002. Thus, you got a t-value of 24.722 which lead to a practically zero p-value. Hence, you can say that your coefficient is indeed significant. 
 
Apart from this, the summary statistics outputs a few more metrics which are not of any use as of now. But you'll learn about some more of them in multiple linear regression.


Formulae:



Summary

Summary  In this session, you built a simple linear regression model in Python using the advertising dataset. You also saw some more theoretical aspects in between. Here's a brief of what you learnt in this session.
1. A quick recap of simple linear regression
2. Assumptions of simple linear regression
* Linear relationship between X and y.
* Normal distribution of error terms.
* Independence of error terms.
* Constant variance of error terms.
3. Hypothesis testing in linear regression
* To determine the significance of beta coefficients.
* H0:β1=0;HA:β1≠0. 
* T-test on the beta coefficient.
* t score=^βiSE(^βi).
4. Building a linear model
* OLS (Ordinary Least Squares) method in statsmodels to fit a line.
* Summary statistics
* F-statistic, R-squared, coefficients and their p-values.
5. Residual Analysis
* Histogram of the error terms to check normality.
* Plot of the error terms with X or y to check independence.
6. Predictions
* Making predictions on the test set using the 'predict()' function.
7. Linear Regression using SKLearn
* A second package apart from statsmodels for linear regression.
    * A more hassle-free package to just fit a line without any inferences.
Rahim has also answered some common doubts surrounding linear regression. This part has also been included in the notebook provided to you at the beginning of the session.



The statement
𝑥¯−𝜇→𝑁(0,𝜎2𝑛)
is somewhat nonsensical. The right hand side still depends on 𝑛, so what is the convergence here?

What you should be writing here is
𝑛√(𝑥¯−𝜇)→𝑁(0,𝜎2).
The point is that after taking the limit 𝑛→∞, the right hand side should no longer be a function of 𝑛.

Secondly, we know that from the law of large numbers
𝑠2→𝑝𝜎2

By the continuous mapping theorem, this implies that
1/𝑠→𝑑1/𝜎.

Now use Slutsky's to combine the above statements to obtain:
(𝑥¯−𝜇)𝑠/𝑛√=𝑛√(𝑥¯−𝜇)𝑠→𝑑𝑁(0,1).

2) What would be a situation where we would not assume that Slutsky's theorem rescues us from the issue of having a random variable in the denominator?

Slutsky's theorem works so long as the assumptions hold, which can be found here.

3) If we lack normality but then appeal to the central limit theorem to say that our large sample size means that we're "close enough", why do a t-test instead of a z-test?

𝑡-tests are normally used when the sample size is not large. i.e., when that appeal to the central limit theorem is not valid.

**Multi-linear Regression and Multi-collinearity**

### 1. **Introduction to Multi-linear Regression**
Multi-linear regression is a statistical technique used to model the
relationship between one continuous dependent variable (outcome) and two
or more independent variables (predictors). It extends simple linear
regression, which involves only one predictor, by allowing for multiple
predictors in the model.

The general form of a multi-linear regression equation is:
\[ Y = \beta_0 + \beta_1X_1 + \beta_2X_2 + \dots + \beta_nX_n + \epsilon
\]
where:
- \( Y \) is the dependent variable.
- \( X_1, X_2, \dots, X_n \) are independent variables.
- \( \beta_0 \) is the intercept.
- \( \beta_1, \beta_2, \dots, \beta_n \) are the regression coefficients.
- \( \epsilon \) is the error term.

### 2. **What is Multi-collinearity?**
Multi-collinearity refers to a situation where two or more independent
variables in a multiple regression model are highly correlated with each
other. This means that one can be linearly predicted from the others with
a non-trivial degree of accuracy.

### 3. **Consequences of Multi-collinearity**
- **Inflated Standard Errors**: The standard errors of the coefficients
(\( \beta \)) become larger, making it harder to reject null hypotheses
(i.e., detecting insignificant predictors).
- **Unstable Coefficients**: The regression coefficients are unstable and
sensitive to minor changes in model specification or data.
- **Reduced Interpretability**: It becomes difficult to interpret the
individual effects of each predictor on the dependent variable because
they are highly correlated.

### 4. **Causes of Multi-collinearity**
- **Data Collection Issues**: Variables may be collected in a way that
inherently leads to correlation (e.g., measuring similar constructs).
- **Measurement Error**: Errors in data collection or measurement can
create artificial correlations between variables.
- **Model Specification**: Including irrelevant variables or interaction
terms without careful consideration can lead to multi-collinearity.
- **Small Sample Size**: With limited data, it is harder to estimate
relationships accurately, increasing the chance of multi-collinearity.

### 5. **How to Detect Multi-collinearity**
- **Correlation Matrix**: Examine pairwise correlations between
independent variables. High correlations (e.g., >0.7) suggest potential
multi-collinearity.
- **Variance Inflation Factor (VIF)**: VIF measures how much the variance
of a coefficient is inflated due to multi-collinearity. A VIF value
greater than 1 indicates the presence of multi-collinearity, with higher
values (typically >5 or 10) signaling severe issues.
- **Eigenvalues and Condition Indexes**: These are part of variance
decomposition proportions (VDP) analysis and can detect multi-collinearity
when combined with high VIFs.

### 6. **Remedies for Multi-collinearity**
- **Remove Redundant Variables**: Eliminate one or more highly correlated
predictors from the model.
- **Combine Variables**: Create a new variable that is a combination
(e.g., sum, average, or ratio) of the correlated variables.
- **Use Regularization Techniques**: Methods like Ridge Regression or
Lasso can help shrink coefficients and reduce multi-collinearity's impact.
- **Principal Component Analysis (PCA)**: Transforms original variables
into a smaller set of uncorrelated components that capture most of the
variance in the data.

### 7. **Conclusion**
Multi-collinearity is a common issue in regression analysis that can lead
to unreliable and unstable estimates of regression coefficients. By
understanding its causes, detecting it through various methods, and
applying appropriate remedies, researchers can build more robust and
interpretable models.


Alright, I'm trying to wrap my head around multi-linear regression and
multi-collinearity. From the previous explanation, I know that
multi-linear regression is an extension of simple linear regression where
there are multiple independent variables predicting a dependent variable.
The formula given was:

\[ Y = \beta_0 + \beta_1X_1 + \beta_2X_2 + \dots + \beta_nX_n + \epsilon
\]

Okay, so this makes sense—each \( X_i \) is an independent variable with
its own coefficient \( \beta_i \), and we have an intercept term \(
\beta_0 \). The dependent variable is \( Y \), and \( \epsilon \) is the
error term.

Now, multi-collinearity seems to be a problem that arises when there are
high correlations among these independent variables. This can make it hard
to estimate the coefficients accurately because the variables aren't
providing unique information. I'm not entirely sure how exactly this
affects the regression model mathematically, though.

I think what happens is that if two variables are highly correlated, their
individual effects on \( Y \) become unclear. For example, suppose we have
variables like square footage and number of rooms in a house predicting
its price. These might be somewhat related because larger houses tend to
have more rooms. This relationship could make it difficult to determine
whether the effect on price is due to having more rooms or just being
bigger.

Mathematically, I believe this has something to do with the
variance-covariance matrix of the coefficients. When variables are highly
correlated, the matrix becomes ill-conditioned, meaning small changes in
the data can lead to large changes in the coefficient estimates. This
instability makes it hard to trust the significance tests and confidence
intervals around these coefficients.

I also remember that one way to detect multi-collinearity is by using
something called the Variance Inflation Factor (VIF). A high VIF for a
variable indicates that it's highly correlated with other variables in the
model. The formula for VIF might look something like:

\[ \text{VIF}_i = \frac{1}{1 - R_i^2} \]

Where \( R_i^2 \) is the coefficient of determination from a regression of
the \( i^{th} \) variable on all other variables. If VIF is greater than 5
or 10, it's considered high and suggests severe multi-collinearity.

Another thing mentioned was using the correlation matrix to look at
pairwise correlations between variables. High correlations (like above
0.7) can be indicative of multi-collinearity.

Remedies for multi-collinearity include removing redundant variables,
combining variables into a single composite variable, or using techniques
like ridge regression or lasso that can handle multicollinear data by
penalizing large coefficients. Principal Component Analysis (PCA) is
another method where you transform the original correlated variables into
a smaller set of uncorrelated components.

I'm still not entirely clear on how to implement these remedies
mathematically, though. For instance, how exactly do you combine variables
or apply ridge regression? I think ridge regression adds a penalty term to
the sum of squared coefficients to shrink them towards zero, which helps
reduce their variance at the cost of introducing some bias.

Also, what's the proper way to interpret the results when
multi-collinearity is present? Do we just report the coefficients as
usual, or do we need to adjust for it somehow?

Overall, I have a basic understanding of what multi-linear regression and
multi-collinearity are, but diving deeper into their mathematical
underpinnings and practical implications has made me realize there's more
to learn. Maybe going through some example problems would help solidify
these concepts.


**Step-by-Step Explanation:**

**1. Understanding Multi-linear Regression:**

Multi-linear regression is a statistical technique used to model the
relationship between one continuous dependent variable (outcome) and two
or more independent variables (predictors). The general form of the
multi-linear regression equation is:

\[ Y = \beta_0 + \beta_1X_1 + \beta_2X_2 + \dots + \beta_nX_n + \epsilon
\]

Where:
- \( Y \) is the dependent variable.
- \( X_1, X_2, \dots, X_n \) are independent variables.
- \( \beta_0 \) is the intercept.
- \( \beta_1, \beta_2, \dots, \beta_n \) are the regression coefficients.
- \( \epsilon \) is the error term.

**2. What is Multi-collinearity?:**

Multi-collinearity refers to a situation where two or more independent
variables in a multiple regression model are highly correlated with each
other. This means that one can be linearly predicted from the others with
a non-trivial degree of accuracy.

**3. Consequences of Multi-collinearity:**

- **Inflated Standard Errors:** The standard errors of the coefficients
(\( \beta \)) become larger, making it harder to reject null hypotheses
(i.e., detecting insignificant predictors).

- **Unstable Coefficients:** The regression coefficients are unstable and
sensitive to minor changes in model specification or data.

- **Reduced Interpretability:** It becomes difficult to interpret the
individual effects of each predictor on the dependent variable because
they are highly correlated.

**4. Causes of Multi-collinearity:**

- **Data Collection Issues:** Variables may be collected in a way that
inherently leads to correlation (e.g., measuring similar constructs).

- **Measurement Error:** Errors in data collection or measurement can
create artificial correlations between variables.

- **Model Specification:** Including irrelevant variables or interaction
terms without careful consideration can lead to multi-collinearity.

- **Small Sample Size:** With limited data, it is harder to estimate
relationships accurately, increasing the chance of multi-collinearity.

**5. Detecting Multi-collinearity:**

- **Correlation Matrix:** Examine pairwise correlations between
independent variables. High correlations (e.g., >0.7) suggest potential
multi-collinearity.

- **Variance Inflation Factor (VIF):** VIF measures how much the variance
of a coefficient is inflated due to multi-collinearity. A VIF value
greater than 1 indicates the presence of multi-collinearity, with higher
values (>5 or 10) signaling severe issues.

- **Eigenvalues and Condition Indexes:** These are part of variance
decomposition proportions (VDP) analysis and can detect multi-collinearity
when combined with high VIFs.

**6. Remedies for Multi-collinearity:**

- **Remove Redundant Variables:** Eliminate one or more highly correlated
predictors from the model.

- **Combine Variables:** Create a new variable that is a combination
(e.g., sum, average, or ratio) of the correlated variables.

- **Use Regularization Techniques:** Methods like Ridge Regression or
Lasso can help shrink coefficients and reduce multi-collinearity's impact.

- **Principal Component Analysis (PCA):** Transforms original variables
into a smaller set of uncorrelated components that capture most of the
variance in the data.

**7. Conclusion:**

Multi-collinearity is a common issue in regression analysis that can lead
to unreliable and unstable estimates of regression coefficients. By
understanding its causes, detecting it through various methods, and
applying appropriate remedies, researchers can build more robust and
interpretable models.

**Mathematical Considerations:**

- **Variance Inflation Factor (VIF):**

  The VIF for a predictor variable \( X_i \) is given by:

  \[ \text{VIF}_i = \frac{1}{1 - R_i^2} \]

  Where \( R_i^2 \) is the coefficient of determination from a regression
of \( X_i \) on all other variables. A high VIF indicates that \( X_i \)
is highly correlated with other variables in the model.

- **Correlation Matrix:**

  Compute the correlation coefficients between each pair of independent
variables to identify those with high correlations (e.g., >0.7).

- **Eigenvalues and Condition Indexes:**

  These are derived from the eigenvalue decomposition of the
variance-covariance matrix of the predictors. High condition indexes,
especially when associated with high proportions of variance, indicate
multi-collinearity.

**Implementation Steps:**

1. **Model Building:** Start by fitting a multi-linear regression model
with all potential independent variables.
2. **Check Correlations:** Examine the correlation matrix to identify
highly correlated variables.
3. **Calculate VIFs:** For each predictor, compute the VIF to quantify the
severity of multi-collinearity.
4. **Remedial Actions:** Based on the findings from the above steps,
implement appropriate remedies such as removing redundant variables or
applying regularization techniques.

By systematically addressing multi-collinearity through these steps, you
can improve the reliability and interpretability of your regression models.


When you have a categorical variable with say 'n' levels, the idea of dummy variable creation is to build 'n-1' variables, indicating the levels. For a variable say, 'Relationship' with three levels namely, 'Single', 'In a relationship', and 'Married', you would create a dummy table like the following:

Relationship Status	Single	In a relationship	Married
Single	1	0	0
In a relationship	0	1	0
Married	0	0	1
But you can clearly see that there is no need of defining three different levels. If you drop a level, say 'Single', you would still be able to explain the three levels.

Let's drop the dummy variable 'Single' from the columns and see what the table looks like: 
Relationship Status	In a relationship	Married
Single	0	0
In a relationship	1	0
Married	0	1
If both the dummy variables namely 'In a relationship' and 'Married' are equal to zero, that means that the person is single. If 'In a relationship' is one and 'Married' is zero, that means that the person is in a relationship and finally, if 'In a relationship' is zero and 'Married' is 1, that means that the person is married.


It is important to note that scaling just affects the coefficients and none of the other parameters like t-statistic, F-statistic, p-values, R-squared, etc.



There are two major methods to scale the variables, i.e. standardisation and MinMax scaling. Standardisation basically brings all of the data into a standard normal distribution with mean zero and standard deviation one. MinMax scaling, on the other hand, brings all of the data in the range of 0 and 1. The formulae in the background used for each of these methods are as given below:

    Standardisation: x=x-mean(x)/sd(x)
    MinMax Scaling: x=x-min(x)/max(x)-min(x)


Coming up

In the next segment, you will learn to assess and compare models. The concept of comparing models is a very important part as for a data set we can use many models but to use a correct mapped model to the problem statement is a core part of machine learning.



Additional Reading

To know more about dummy variables (here)
Why it's necessary to create dummy variables (here)
When to Normalise data and when to standardise? (here)
Various scaling techniques (here)

Now, for the assessment, you have a lot of new considerations to make. Besides, selecting the best model to obtain decent predictions becomes quite subjective. You need to maintain a balance between keeping the model simple and explaining the highest variance (which means that you would want to keep as many variables as possible). This can be done using the key idea that a model can be penalised for keeping a large number of predictor variables.



Hence, there are two new parameters that come into picture:



                                                              Adjusted R2=1-(1-R2)(N-1)N-p-1


Aℂ=n×logRSSn+2p



Here, n is the sample size meaning the number of rows you'd have in the dataset and p is the number of predictor variables.


Coming up

Adjusted R2 adjusts the value of R2 such that a model with a larger number of variables is penalized. In the next segment, Rahim will talk about feature selection.



Additional Reading :

The following links provide a detail study on AIC and other parameters used in automatic feature selection :

    AIC
    BIC
    Mallows' CP

Before you proceed further, spend some time answering the question next.

					RFE

Functional Benefits of Automating Features using Recursive Feature Elimination (RFE), and L1 Regularization





Introduction to Feature Selection and Automation
All Data Scientist and Machine Learning Engineers knows that “Feature Engineering”, specifically feature selection, is a crucial step in the machine learning and data science workflow that involves selecting the most relevant features from a derived dataset to train a model and take it further the model to the production environment. We have to do the proper exercise and carefully choose these features along with SEM’s involvement and guidance; the end results would be enhanced model performance, improved interpretability, reduced overfitting, and highly optimised computational resources.
The goal is to use automated feature selection techniques to identify how it retains features that contribute the most to the model’s outcome while removing irrelevant, redundant, or noisy data that could negatively impact performance.
Understanding the Automated Feature Selection
Automating feature selection techniques furthers this process by using algorithms and tools to streamline and accelerate it. This approach reduces manual effort, mitigates human biases, and ensures that the most informative features are chosen consistently across large or complex datasets. Automated methods can handle high-dimensional data, making the process more scalable and efficient.
Automated feature selection can be categorized into three main types: Filter, Wrapper, and Embedded Methods. This article will explore Wrapper and Embedded Methods, their statistical metrics, and their understanding and implementation. We will also explore how they help machine learning models build worthy algorithms capable of identifying relevant and required features based on the processed dataset for the problem statement given.
Automated techniques help data scientists and engineers build better-performing models while saving time and effort, making them indispensable in modern machine-learning projects.
As we know, automatic feature selection uses algorithms to choose the best subset of features from the earlier article.
The following methods are designed to handle significant datasets with high-dimensional data and often provide faster, more objective results than manual selection. They are classified into Filter, Wrapper, and Embedded Methods.
￼
Figure 1: Feature Selection Techniques
Among these methods, start with “Filter Methods” to reduce dimensionality if the dataset is large. We can use “Embedded Methods” if model-based selection is preferred to balance performance and efficiency factors. Then, we can apply “Wrapper Methods” if feature interactions are crucial and computational resources allow it, particularly for smaller datasets. That’s the suggestion for a strategy for data scientists and ML engineers.
Comparative Study of Automated Feature Selection Methods
Automated Description and Techniques: Each method is unique. Let’s understand each process and the techniques available.
￼
Table 1: Comparative Study of Automated Feature Selection Methods
Automated Methods — Advantages and Disadvantages: Each method has its own advantages and disadvantages. Let’s explore each one quickly.
￼
Table 2: Automated Methods — Advantages and Disadvantages
Automated Techniques: Although the three methods have unique advantages and various techniques, each method’s fitment differs based on the scenarios it is best for.
￼
Table 3: Automated Methods — Best fit

Auto Feature Selection
Let’s discuss “Auto Feature Selection Tools” in Python. Libraries like scikit-learn in Python offer automated feature selection tools such as SelectKBest, Recursive Feature Elimination (RFE) and LassoCV.
* 		SelectKBest: Select the top k features based on a scoring function (e.g., Chi-square, ANOVA).
* 		Recursive Feature Elimination (RFE): Iteratively fits the model and removes less essential features.
* 		LassoCV: Performs feature selection while optimizing the regularization strength in Lasso Regression.
As I promised initially, let’s implement the Wrapper Methods in this article.
Wrapper Methods
It uses a set of techniques to evaluate different subsets of features by training a model and assessing performance; because of this, methods require more computation effort.
Of course, we can get better capture feature interactions than filter methods. It has three techniques to demonstrate its capabilities: Forward Selection, Backward Elimination, and RFE.
* 		Forward Selection starts with an empty model and keeps adding the features one by one, evaluates the performance, observes the outcome, and, based on the results, decides which feature improves the model the most at each step.
* 		Backward Elimination starts with all features in the initial evaluation and eliminates them one by one. It then evaluates the performance, observes the outcome, and removes the least significant feature based on the results at each step.
* 		Recursive Feature Elimination (RFE) method trains the model with all features from the given dataset and iteratively removes the least essential features based on model performance. It is often used with algorithms that provide feature importance, like decision trees.
￼
Figure 2: Feature Selection Techniques — Wrapper method process
```python
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings('ignore')

# Load a winequality dataset
X = df_winequality.drop("quality", axis=1)
y = df_winequality["quality"]

def forward_selection(X, y, model, scoring='accuracy', cv=5):

    selected_features = []
    remaining_features = list(X.columns)
    best_score = 0

    while remaining_features:
        scores_with_candidates = []
        for feature in remaining_features:
            # Test the current set of selected features plus the candidate feature
            candidate_features = selected_features + [feature]
            X_subset = X[candidate_features]
            score = cross_val_score(model, X_subset, y, scoring=scoring, cv=cv).mean()
            scores_with_candidates.append((score, feature))

        # Select the feature with the highest score
        scores_with_candidates.sort(reverse=True)
        best_new_score, best_candidate = scores_with_candidates[0]

        # Stop if no improvement
        if best_new_score <= best_score:
            break

        # Update the best score and add the best candidate to selected features
        best_score = best_new_score
        selected_features.append(best_candidate)
        remaining_features.remove(best_candidate)
        print(f"Selected feature: {best_candidate} with score: {best_new_score}")

    return selected_features

# Instantiate the model
model = LogisticRegression(max_iter=10,solver='liblinear')

# Perform forward selection
selected_features = forward_selection(X, y, model)
print("Final selected features:", selected_features)
```

Output
Selected feature: alcohol with score: 0.5516202978056427
Selected feature: volatile acidity with score: 0.5584835423197492
Selected feature: citric acid with score: 0.5666261755485893
Selected feature: sulphates with score: 0.572884012539185
Selected feature: chlorides with score: 0.575384012539185
Selected feature: residual sugar with score: 0.5766261755485893
Final selected features: ['alcohol', 'volatile acidity', 'citric acid', 'sulphates', 'chlorides', 'residual sugar']
Observation
Key Insights from the Output
Feature Selection Process:
* 		We have implemented forward selection to iteratively choose features based on their contribution to the model’s performance.
* 		Each iteration adds the feature from the given dataset (winequality), increasing the cross-validated accuracy score.
Feature Scores:
* 		Based on the code implementation, the selection process begins with alcohol, which achieved the highest initial score of 0.5516.
* 		Subsequent features
* 		Volatile Acidity
* 		Citric Acid
* 		Sulphates
* 		Chlorides
* 		Residual Sugar
Were added one at a time, each providing an incremental improvement in model performance. Each chosen feature leads to a higher score than previous combinations, indicating that these features contribute significantly to model accuracy.
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE

# Load a sample dataset (you can replace this with your own dataset)
data = load_wine()
X = data.data
y = data.target



# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Instantiate a Logistic Regression model
model = LogisticRegression(max_iter=1000, solver='liblinear')

# Set up RFE to select the top 5 features
n_features_to_select = 5
rfe = RFE(estimator=model, n_features_to_select=n_features_to_select)

# Fit RFE
rfe.fit(X_train, y_train)

# Get the selected features
selected_features = rfe.support_
feature_ranking = rfe.ranking_

# Print the selected features and their rankings
print("Selected Features (True means selected):", selected_features)
print("Feature Ranking:", feature_ranking)

# Get names of selected features if using a dataframe
selected_feature_names = [data.feature_names[i] for i in range(len(selected_features)) if selected_features[i]]
print("Selected Feature Names:", selected_feature_names)

# Evaluate model performance on the test set using only selected features
X_train_selected = rfe.transform(X_train)
X_test_selected = rfe.transform(X_test)
model.fit(X_train_selected, y_train)
score = model.score(X_test_selected, y_test)
print(f"Model accuracy with selected features: {score:.4f}")
Output
Selected Features (True means selected):
[False False  True False False False  True False False  True  True  True  False]
Feature Ranking: [7 5 1 3 8 4 1 6 2 1 1 1 9]
Selected Feature Names: ['ash', 'flavanoids', 'color_intensity', 'hue', 'od280/od315_of_diluted_wines']
Model accuracy with selected features: 0.8704
Observation
Selected Features (True means selected):
* 		This array shows a True or False for each feature in the dataset, indicating whether RFE selected each feature.
* 		True means the feature was selected as one of the top 5 essential features, while False means it was not.
* 		For example, [False, False, True, False, False, False, True, False, False, True, True, True, False] indicates that the 3rd, 7th, 10th, 11th, and 12th features were selected.
Feature Ranking:
* 		Each feature’s ranking shows how important RFE considered it, with 1 indicating selected features and higher numbers indicating lower importance.
* 		For example:
* 		Features ranked 1 are selected: ash, flavanoids, color_intensity, hue, and od280/od315_of_diluted_wines.
* 		The feature ranking 9 (the highest) was deemed the least important.
Selected Feature Names:
* 		The selected features (ash, flavanoids, color_intensity, hue, and od280/od315_of_diluted_wines) are printed here by name.
* 		The top 5 features that RFE identified as most significant for the logistic regression model in predicting the target.
Model Accuracy with Selected Features:
    * 		The model’s accuracy using only the selected features is 0.8704.
* 		This accuracy score indicates how well the model performs on the test data when using just the selected subset of features rather than the entire set.
* 		A relatively high score here (0.8704) suggests that the selected features are well-suited to the model and can make accurate predictions, simplifying the model without sacrificing much accuracy.
Conclusion
Automating feature selection through Recursive Feature Elimination (RFE) and L1 Regularization offers substantial functional benefits in developing machine learning models.
These techniques efficiently streamline selecting the most relevant features, reducing manual effort, computational cost, and model complexity.
By focusing on the features that significantly influence the model’s predictions, these automated methods improve the model’s accuracy, interpretability, and generalization capability.
In our implementations:
* 		Forward Selection in wrapper methods selected features based on their incremental contribution to accuracy, resulting in a robust feature subset that improves model performance in stages.
* 		Recursive Feature Elimination (RFE) effectively reduced the dataset to the most impactful features, preserving only those essential for predicting outcomes while achieving a high model accuracy of 0.8704.
Both methods confirm that automated feature selection simplifies model training and produces models optimized for high-dimensional data. By automating feature selection, data scientists can focus on refining model accuracy and robustness while minimizing the risk of overfitting and enhancing the model’s deployment readiness. Thus, automated selection is an indispensable part of a scalable and efficient data science workflow.
Thanks for reading this article.


```python

```
