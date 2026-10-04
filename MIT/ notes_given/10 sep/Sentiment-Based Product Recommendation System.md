# Sentiment-Based Product Recommendation System  
  
Dead: 22nd April  
## Problem Statement  
  
The e-commerce business is quite popular today. Here, you do not need to take orders by going to each customer. A company launches its website to sell the items to the end consumer, and customers can order the products that they require from the same website. Famous examples of such e-commerce companies are Amazon, Flipkart, Myntra, Paytm and Snapdeal.  
   
Suppose you are working as a Machine Learning Engineer in an e-commerce company named 'Ebuss'. Ebuss has captured a huge market share in many fields, and it sells the products in various categories such as household essentials, books, personal care products, medicines, cosmetic items, beauty products, electrical appliances, kitchen and dining products and health care products.  
   
With the advancement in technology, it is imperative for Ebuss to grow quickly in the e-commerce market to become a major leader in the market because it has to compete with the likes of Amazon, Flipkart, etc., which are already market leaders.  
   
As a senior ML Engineer, you are asked to build a model that will improve the recommendations given to the users given their past reviews and ratings.   
   
In order to do this, you planned to build a **sentiment-based product recommendation system, **which includes the following tasks.  
1. Data sourcing and sentiment analysis  
2. Building a recommendation system  
3. Improving the recommendations using the sentiment analysis model  
4. Deploying the end-to-end project with a user interface  
   
* **Data sourcing and sentiment analysis**  
In this task, you have to analyse product reviews after some text preprocessing steps and build an ML model to get the sentiments corresponding to the users' reviews and ratings for multiple products.   
   
The dataset that you are going to use is inspired by this ++[Kaggle competition](https://www.kaggle.com/datafiniti/grammar-and-online-product-reviews)++. We have made a subset of the original dataset, which has been provided below.  
   
++[Product Reviews Dataset](https://cdn.upgrad.com/uploads/production/c2504c0d-6080-4e1e-8d4c-852b3e68a0ed/sample30.csv)++  
   
This dataset consists of 30,000 reviews for more than 200 different products. The reviews and ratings are given by more than 20,000 users. Please refer to the following attribute description file to get the details about the columns of the Review Dataset.  
   
++[Product Reviews Dataset- Attribute Description](https://cdn.upgrad.com/uploads/production/a2446a81-154b-49cf-8fb2-2e87614496e6/Data+Attribute+Description.csv)++  
   
Phase 1  
  
The steps to be performed for the first task are given below.  
1. **Exploratory data analysis**  
2. **Data cleaning**  
3. **Text preprocessing**  
4. **Feature extraction:** In o**rder to extract features from the text data, you may choose from any of the methods, including bag-of-words, TF-IDF vectorization or word embedding. sklearn tf idf.. naive bayes**  
5. **Training a text classification model: You need to build at least three ML models. You then need to analyse the performance of each of these models and choose the best model. At least three out of the following four models need to be built (Do not forget, if required, handle the class imbalance and perform hyperparameter tuning.).  1  imabalanced 1. Logistic regression 2. Random forest 3. XGBoost 4. Naive Bayes ( Same as assignment 3  fradulent claim detection.. everything)**  
  
  
Out of these four models, you need to select one classification model based on its performance.  
* **Building a recommendation system**  
  
  
  
  
As you learnt earlier, you can use the following types of recommendation systems.  
   
**1. User-based recommendation system**  
**2. Item-based recommendation system**  
   
Your task is to analyse the recommendation systems and select the one that is best suited in this case.   
   
Once you get the best-suited recommendation system, the next task is to recommend 20 products that a user is most likely to purchase based on the ratings. You can use the 'reviews_username' (one of the columns in the dataset) to identify your user.   
   
* **Improving the recommendations using the sentiment analysis model**  
Now, the next task is to link this recommendation system with the sentiment analysis model that was built earlier (recall that we asked you to select one ML model out of the four options). Once you recommend 20 products to a particular user using the recommendation engine, you need to filter out the 5 best products based on the sentiments of the 20 recommended product reviews.   
   
In this way, you will get an** ML model** (for sentiments) and the **best-suited recommendation system**. Next, you need to deploy the entire project publicly.  
   
* **Deployment of this end to end project with a user interface**  
Once you get the ML model and the best-suited recommendation system, you will deploy the end-to-end project. You need to use the **Flask **framework, which is majorly used to create web applications to deploy machine learning models.  
   
Next, you need to include the following features in the user interface.  
1. Take any of the existing usernames as input.  
2. Create a submit button to submit the username.  
3. Once you press the submit button, it should recommend 5 products based on the entered username.  
Note: An important point that you need to consider here is that the number of users and the number of products are fixed in this case study, and you are doing the sentiment analysis and building the recommendation system only for those users who have already submitted the reviews or ratings corresponding to some of the products in the dataset.   
   
Because the dataset that you are going to use is huge, the model training may take time, and hence, you can use ++[Google Colab](https://colab.research.google.com/)++ to directly code or upload the already created notebook.  
   
You can look into the user guide to access the Colab below.  
   
++[Colab User Guide](https://cdn.upgrad.com/uploads/production/54306fb6-8c54-4a02-b39a-f78b2abe6ade/colab_user_guide-converted.pdf)++  
   
**Assumption: No new users or products will be introduced or considered when building or predicting from the models built.**  
   
**What needs to be submitted for the evaluation of the project?**  
1. An end-to-end Jupyter Notebook, which consists of the entire code (data cleaning steps, text preprocessing, feature extraction, ML models used to build sentiment analysis models, two recommendation systems and their evaluations, etc.) of the problem statement defined  
2. The following deployment files  
* One 'model.py' file, which should contain only one ML model and only one recommendation system that you have obtained from the previous steps 	  
The evaluation rubrics are mentioned in the next segment.  
  
  
  
  
  

| Attribute | Attribute Description |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id | Uniques identity number to identify each unique review given by the user to a particular product in the dataset |
| brand | Name of the brand of the product to which user has given review and rating |
| categories | Category of the product like household essentials, books, personal care products, medicines, cosmetic items, beauty products, electrical appliances, kitchen and dining products, health care products and many more. |
| manufacturer | Name of the manufacturer of the product |
| name | Name of the product to which user has added review or rating |
| reviews_date | Date on which the review has been added by the user |
| reviews_didPurchase | Whether a particular user has purchased the product or not |
| reviews_doRecommend | Whether a particular user has recommended the product or not |
| reviews_rating | Rating given by the user to a particular product |
| reviews_text | Review given by the user to a particular product |
| reviews_title | The title of the review given by the user to a particular product |
| reviews_userCity | The residing city of the user |
| reviews_userProvince | The residing province of the user |
| reviews_username | The unique identification for individual user in the dataset |
| user_sentiment | The overall sentiment of the user for a particular product (Positive or Negative) |
  
  
  
  
Your solution will be evaluated based on the following rubrics.  
   

| Criteria | Meet Expectations | Does Not Meet Expectations |
| ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Task 1:
Data Cleaning and Pre-Processing
(10%) | Performed all data quality checks and addressed all data quality issues in the right way (especially the missing value treatment). Provided a clear explanation for missing value removal or imputation
 
 
Provided a well-commented explanation for each step of data processing
 
 
Dropped the variables that were not relevant for the project with a well-commented explanation for each step. Converted all variables to correct datatypes. | Did not handle the missing values efficiently
 
 
 
 
 
Did not perform and explain the necessary steps for data processing in the comments
 
Did not remove unwanted variables from the columns and did not convert the variables to correct datatypes |
| Task 2:
Text Processing
(10%) | Explored all the relevant text preprocessing steps after cleaning the data set.
 
Provided well-commented reasons for every step that was performed in text preprocessing. | Did not perform the relevant text preprocessing steps to clean the text of the reviews. Did not get clean text at the end of this step |
| Task 3:
Feature Extraction
(10 %) | Divided the data into training and testing parts
 
Converted the text to features using the best-suited vectorizer (bag-of-words, TD-IDF, Word2Vec, etc.) for the ML model for sentiment analysis model building. | Did not divide the data into training and testing parts
 
Did not create the appropriate vectorizer for feature extraction to build the ML model |
| Task 4:
Model Building
(20%) | Built at least 3 ML models and did the comparative analysis on why one model is better than the other three models
 
 
Checked whether the data is imbalanced or not and took the necessary steps. If necessary then did the hyperparameter tuning also
 
 
Selected one out of the 3 models based on performance for predicting the sentiments based on the text and title of the reviews. Provided detailed reasons for selecting the model | Did not build the 3 ML models and did not give a satisfactory explanation on why one model is better than the other three models
 
Did not consider the imbalance in the data set
 
Did not select the ML model that performed better than the rest. Did not give reasons for selecting the model chosen |
| Task 5:
Building the Recommendation System
(20%) | Split the data set into train and test data set for the recommendation system
 
 
Built at least two types of recommendation systems: user-based and item-based recommendation systems
 
 
 
Evaluated both the types of recommendation systems and selected one based on performance. Provided detailed reasons for selecting the recommendation system | Did not split the data set into train and test datasets
 
 
Did not build the two types of recommendation systems
 
 
 
Did not evaluate the recommendation systems and did not provide any explanation for selecting the best-suited recommendation system |
| Task 6:
Recommendation of Top 20 Products to a Specified User
(10%) | Recommended the top 20 products for the username selected by the user based on the recommendation system built | Did not recommend the top 20 products for any selected username using the finalised recommendation system |
| Task 7:
Fine-Tuning the Recommendation System and Recommendation of Top 5 Products
(10%) | Predicted the sentiment (positive or negative) of all the reviews in the train data set of the top 20 recommended products for a user. For each of the 20 products recommended, found the percentage of positive sentiments for all the reviews of each product. Filtered out the top 5 products with the highest percentage of positive reviews | Did not predict the sentiment using the ML model of all the reviews of the top 20 recommended products for a user. Did not filter out the top 5 products based on the percentage of positive reviews |
| Task 8:
Deployment Using Flask
(10%) | Build an end-to-end web application using Flask and deploy it in your local system. You need to only include one ML model and one recommendation system to deploy the model.
 
You need to:
	1	Take the username as input, and
	2	Create a submit button, and once you press the submit button, it should recommend the 5 products based on the username entered. | Was not able deploy the project using Flask |
  
  
  
  
  
  
  
  
  
  
  
