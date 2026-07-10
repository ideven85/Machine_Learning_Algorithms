# Problem Statement

## Objective

This assignment aims to give you a practical understanding of model selection in real-world scenarios. You will learn how to analyse and preprocess data, extract meaningful features, and apply various machine learning models to uncover patterns and insights. Through model evaluation and optimisation techniques, you will gain the ability to compare different approaches and select the most effective one. This process will enhance your skills in building reliable predictive models, improving decisionmaking, and ensuring model accuracy and generalisation in diverse applications.

## Business Value

Developing a predictive model for insurance fraud detection offers significant business value. Fraud investigations currently rely on manual processes like reviewing claims, calling claimants, and conducting background checks, which are time-consuming and inefficient. These delays allow fraud to go undetected while legitimate claims face unnecessary scrutiny. Predictive modelling enables early identification of high-risk claims, streamlining fraud investigations, reducing financial losses, and improving operational efficiency. It also enhances customer experience by expediting legitimate claims. Ultimately, an effective fraud detection model leads to better decision-making, optimised resource allocation, and increased profitability.

The objective is to build a model to classify insurance claims as either fraudulent or legitimate based on historical claim details and customer profiles. By using features like claim amounts, customer profiles, claim types, and approval times, the company aims to predict which claims are likely to be fraudulent before they are approved.

# Dataset Overview

### Context

The data contains records of various claims received by an insurance company and relevant features associated with those claims such as policy number, incident date, incident type, and so on.

## Content

The data is stored as a CSV file and contains information such as customer-related details (age, occupation, hobbies), policy information (coverage limits, premiums), incident specifics (type, severity, location), claim details (amounts, types of damage), vehicle information (make, model, year), and whether the claim was reported as fraud.

### Acknowledgements

This dataset is free and is publicly available on UCI Machine Learning Repository.

### Scoring and Penalty

- Total Marks: 250 (130 for code notebook, 70 for report and 50 for PPT)
- Extension and Penalty: As given in your learner handbooks

![](_page_1_Picture_0.jpeg)

## Instructions

- 1. This is a group assignment.
- 2. The programming language is Python.
- 3. You will be provided with the dataset and a starter notebook. You have to perform all the tasks in the starter notebook only.
- 4. It is very important that you do not change any headings, subheadings, questions or tasks in your notebook as it can cause problems with grading.
- 5. The data will have inconsistencies and outliers; please handle them as you see fit and mention them in your report.
- 6. You are encouraged to search the web and consult AI tools for conceptual understanding. However, using plagiarised or AI-generated code is strictly prohibited and strongly discouraged.
- 7. Submitting plagiarised and AI-generated code or reports will result in significant penalties to your scores.

# Submission Guidelines

- 1. To submit your solution, push your submission to GitHub and submit the GitHub link in the submission box
- 2. You are required to upload your solution as a zip file titled "Fraudulent\_Claim\_Detection\_<your\_name>.zip" in a public GitHub repository
- 3. The repository should be named after the assignment
- 4. The zip file should contain three files:
  - (a) an Interactive Python Notebook (.ipynb) that contains your code
  - (b) a Report Document (.pdf) that presents your visualisations, analysis, results, insights, and outcomes
  - (c) a PPT, which clearly states the summary, recommendations and business implications of your findings and also provides answers to the questions asked
- 5. Please note that these files should only be generated from the starter files provided to you
- 6. The submitted Jupyter notebook, report and PPT should contain your name and the assignment title
- 7. Mention all assumptions, if made, in the report
- 8. The report should include the overall approach of the assignment, covering the problem statement, methodology, techniques used, and key insights
- 9. The PPT should present answers to the questions asked in the assignment, using visualisations to support your responses

# Results Expected from Learners

Briefly outline the problem statement and approach in the report document. Use visualisations in the PPT to support your answers for all questions in the assignment.

In the starter notebook, you will find headings, subheadings, and checkpoints stating the tasks you need to perform. The marks associated with each checkpoint will also be mentioned in the notebook. Keep in mind not to edit the cells with marking schemes and questions. You can find a brief description of the tasks below.

1. Data Preparation: Import necessary libraries and load the data

![](_page_2_Picture_0.jpeg)

- 2. Data Cleaning (10 marks)
  - (a) Handling null values [2 marks]
  - (b) Handling redundant features [5 marks]
  - (c) Fix data types [3 marks]
- 3. Train-Validation Split [5 marks]
  - (a) Define feature and target(s) variables [2 marks]
  - (b) Split data into training and validation sets [3 marks]
- 4. EDA on Training Data [20 marks]
  - (a) Perform univariate analysis [5 marks]
  - (b) Perform correlation analysis [3 marks]
  - (c) Check class balance [2 marks]
  - (d) Perform bivariate analysis [10 marks]
- 5. EDA on Validation Data [optional]
  - (a) Perform univariate analysis
  - (b) Perform correlation analysis
  - (c) Check class balance
  - (d) Perform bivariate analysis
- 6. Feature Engineering [25 marks]
  - (a) Perform resampling [3 marks]
  - (b) New feature creation [4 marks]
  - (c) Handle redundant columns [3 marks]
  - (d) Combine values in categorical columns [6 marks]
  - (e) Dummy variable creation [6 marks]
  - (f) Feature rescaling [3 marks]
- 7. Model Building [50 marks]
  - (a) Feature selection [4 marks]
  - (b) Building logistic regression model [12 marks]
  - (c) Find the optimal cutoff [12 marks]
  - (d) Building random forest model [12 marks]
  - (e) Hyperparameter tuning [10 marks]
- 8. Predictions and model evaluation [20 marks]
  - (a) Make predictions over validation data using logistic regression model [10 marks]
  - (b) Make predictions over validation data using random forest model [10 marks]

# Evaluation Rubrics

The following rubrics will be used while evaluating your solutions to the above tasks.

![](_page_3_Picture_0.jpeg)

#### Table 1: Rubrics

| Criteria                  | Meets expectations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Does not meet expectations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data Cleaning             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                           | 1. Missing values are handled correctly.<br>2. Redundant values within categorical<br>columns are correctly identified and<br>handled (if any).<br>3. Redundant<br>columns<br>are<br>dropped<br>correctly.<br>4. DataTypes have been corrected for<br>columns with incorrect DataTypes.                                                                                                                                                                                                                                                              | 1. Missing<br>values<br>are<br>handled<br>inadequately.<br>2. Redundant values within categorical<br>columns<br>are<br>incorrectly<br>identified<br>and handled (if any).<br>3. Redundant columns are not dropped<br>correctly.<br>4. DataTypes have not been corrected<br>or have been incorrectly assigned for<br>columns with incorrect DataTypes.                                                                                                                                                                                                                                                                 |
| Train-Validation<br>Split | 1. Feature<br>and<br>target<br>variables<br>are<br>defined correctly.<br>2. Data<br>is<br>split<br>into<br>training<br>and<br>validation sets maintaining the ratio<br>of 70:30.                                                                                                                                                                                                                                                                                                                                                                     | 1. Feature and target variables are not<br>defined or defined incorrectly.<br>2. Data<br>splitting<br>is<br>implemented<br>incorrectly or not implemented at<br>all.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| EDA on training<br>data   | 1. Performed<br>univariate<br>analysis<br>by<br>visualising<br>the<br>distribution<br>of<br>all<br>numerical columns.<br>2. Performed<br>correlation<br>analysis<br>by<br>visualising<br>a<br>heatmap<br>of<br>the<br>correlation matrix.<br>3. Visualised class distribution of the<br>target variable.<br>4. Bivariate<br>analysis<br>has<br>been<br>performed<br>by<br>analysing<br>target<br>likelihood<br>for<br>each<br>category<br>level<br>and<br>visualising<br>the<br>relationship<br>between numerical columns and the<br>target variable | 1. Failed<br>to<br>plot<br>the<br>distributions<br>of<br>numerical<br>columns<br>or<br>created<br>incomplete<br>or<br>inaccurate<br>plots<br>without meaningful insights.<br>2. Incorrectly visualised the heatmap<br>or failed to interpret correlations.<br>3. Failed<br>to<br>visualise<br>the<br>class<br>distribution of the target variable.<br>4. Target Likelihood Analysis has not<br>been performed or done incorrectly.<br>The influence of numerical variables<br>on the target variable has not been<br>visualised.<br>Incomplete<br>or<br>unclear<br>visualisations and insights have been<br>provided. |

Continued on next page

#### Table 1: Rubrics (Continued)

| Criteria               | Meets expectations                                                                                                                                                 | Does not meet expectations                                                                                                                                            |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Feature<br>Engineering | 1. Performed<br>resampling<br>to<br>handle<br>class imbalance.                                                                                                     | 1. Failed<br>to<br>perform<br>resampling<br>to<br>handle class imbalance.                                                                                             |
|                        | 2. Created new feature(s) from existing<br>features<br>to<br>enhance<br>the<br>model's<br>ability to capture patterns.                                             | 2. Failed to create new feature(s) from<br>existing<br>features<br>to<br>enhance<br>the<br>model's ability to capture patterns.                                       |
|                        | 3. Handled redundant columns which<br>may<br>be<br>redundant<br>or<br>contribute<br>minimal<br>information<br>toward<br>prediction.                                | 3. Failed to handle redundant columns<br>which<br>may<br>be<br>redundant<br>or<br>contribute<br>minimal<br>information<br>toward prediction.                          |
|                        | 4. Identified<br>and<br>combined<br>low<br>frequency<br>values<br>in<br>categorical<br>columns<br>to<br>reduce<br>sparsity<br>and<br>improve model generalisation. | 4. Failed<br>to<br>identify<br>and<br>combine<br>low frequency values in categorical<br>columns<br>to<br>reduce<br>sparsity<br>and<br>improve model generalisation.   |
|                        | 5. Created<br>dummy<br>variables<br>for<br>independent and dependent columns<br>in both training and validation sets.                                              | 5. Failed<br>to<br>identify<br>or<br>create<br>appropriate<br>dummy<br>variables<br>for<br>independent and dependent columns<br>in both training and validation sets. |
|                        | 6. Applied feature scaling to numerical<br>columns<br>effectively<br>by<br>scaling<br>the<br>features.                                                             | 6. Failed<br>to<br>apply<br>or<br>incorrectly<br>performed<br>feature<br>scaling,<br>leading<br>to inconsistent data ranges.                                          |

Continued on next page

#### Table 1: Rubrics (Continued)

| Criteria                                 | Meets expectations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Does not meet expectations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Model Building                           | 1. Selected the most important features<br>using Recursive Feature Elimination<br>Cross Validation (RFECV).<br>2. Built<br>a<br>logistic<br>regression<br>model<br>using<br>the<br>selected<br>features,<br>evaluated multicollinearity with p<br>values and VIFs, made predictions,<br>and assessed model performance.<br>3. Found the optimal cutoff by plotting<br>the ROC curve, visualising trade-offs<br>between sensitivity and specificity,<br>precision and recall, and evaluated<br>the<br>final<br>prediction<br>with<br>optimal<br>cutoff.<br>4. Built a random forest model, made<br>predictions<br>and<br>asssessed<br>model<br>performance.<br>5. Tuned<br>the<br>random<br>forest<br>model<br>using<br>appropriate<br>technique,<br>optimised<br>hyperparameters,<br>made<br>predictions,<br>and<br>assessed<br>performance with relevant metrics. | 1. Failed to select appropriate features<br>using Recursive Feature Elimination<br>Cross Validation (RFECV).<br>2. Failed<br>to<br>correctly<br>build<br>the<br>logistic<br>regression<br>model<br>using<br>selected features and evaluated or<br>interpreted the performance metrics<br>incorrectly.<br>3. Failed<br>to<br>identify<br>the<br>optimal<br>cutoff<br>or<br>omitted<br>key<br>evaluations<br>like plotting curves and calculated<br>necessary performance metrics.<br>4. Failed<br>to<br>correctly<br>build<br>the<br>random forest model, did not apply<br>appropriate<br>evaluation<br>metrics,<br>or<br>misinterpreted the results.<br>5. Failed<br>to<br>tune<br>the<br>random<br>forest<br>model effectively, did not optimise<br>hyperparameters, or misinterpreted<br>the performance evaluation. |
| Prediction<br>and<br>Model<br>Evaluation | 1. Predictions were made on validation<br>data<br>using<br>the<br>selected<br>relevant<br>features<br>in<br>the<br>logistic<br>regression<br>model.<br>2. Predictions were made on validation<br>data using the random forest model.<br>3. Evaluated the performance of both<br>the logistic regression and random<br>forest<br>models<br>using<br>the<br>given<br>evaluation metrics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 1. Failed<br>to<br>select<br>relevant<br>features<br>or<br>incorrectly<br>made<br>predictions<br>on<br>validation<br>data<br>in<br>the<br>logistic<br>regression model.<br>2. Made<br>incorrect<br>predictions<br>on<br>validation<br>data<br>using<br>the<br>random<br>forest model.<br>3. Failed to evaluate the performance<br>of<br>both<br>the<br>logistic<br>regression<br>and<br>random<br>forest<br>models<br>using<br>the<br>correct<br>evaluation<br>metrics<br>or<br>interpreted the results inaccurately.                                                                                                                                                                                                                                                                                                  |

Continued on next page

#### Table 1: Rubrics (Continued)

| Criteria                                         | Meets expectations                                                                                                                                                                                                                                                                                                                                                                                                                                  | Does not meet expectations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Report<br>and<br>Recommendations                 | 1. The report has a clear structure, is<br>not too long, and explains the most<br>important results concisely in simple<br>language.<br>2. The recommendations to solve the<br>problem are realistic, actionable and<br>coherent with the analysis.<br>3. The<br>report<br>includes<br>visualisations<br>and insights derived from them.<br>4. If any assumptions are made, they<br>are stated clearly.                                             | 1. The report lacks structure,<br>is too<br>long or does not put emphasis on<br>the<br>important<br>observations.<br>The<br>language<br>used<br>is<br>complicated<br>for<br>business people to understand.<br>2. The recommendations to solve the<br>problem are either unrealistic, non<br>actionable<br>or<br>incoherent<br>with<br>the<br>analysis.<br>3. The report is missing visualisations<br>or<br>fails<br>to<br>provide<br>meaningful<br>insights.<br>4. Assumptions made, if any, are not<br>stated clearly. |
| PPT                                              | 1. Provided a concise overview of the<br>assignment, covering key objectives,<br>methodology, and findings.<br>2. Effectively<br>answered<br>the<br>questions<br>asked<br>in<br>the<br>assignment<br>using<br>appropriate visualisations.<br>3. Used<br>clear,<br>well-structured<br>slides<br>with<br>relevant<br>charts,<br>graphs,<br>and<br>summaries<br>to<br>enhance<br>understanding.                                                        | 1. Failed to provide a clear and concise<br>overview of the assignment.<br>2. Did<br>not<br>effectively<br>answer<br>the<br>questions asked in the assignment<br>or<br>used<br>inappropriate/unclear<br>visualisations.<br>3. PPT<br>lacked<br>structure,<br>clarity,<br>or<br>relevant visual elements, making it<br>difficult to understand key insights.                                                                                                                                                             |
| Conciseness<br>and<br>readability of the<br>code | 1. The code is concise and syntactically<br>correct.<br>Wherever<br>appropriate,<br>built-in<br>functions<br>and<br>standard<br>libraries are used instead of writing<br>long code (if-else statements, loops,<br>etc.).<br>2. Custom<br>functions<br>are<br>used<br>to<br>perform repetitive tasks.<br>3. The<br>code<br>is<br>readable<br>with<br>appropriately<br>named<br>variables<br>and detailed comments are written<br>wherever necessary. | 1. Long<br>and<br>complex<br>code<br>is<br>used<br>instead of shorter built-in functions.<br>2. Custom functions are not used to<br>perform<br>repetitive<br>tasks<br>resulting<br>in<br>the<br>same<br>piece<br>of<br>code<br>being<br>repeated multiple times.<br>3. Code readability is poor because of<br>vaguely named variables or lack of<br>comments wherever necessary.                                                                                                                                        |